import pykakasi
import regex as re
import pandas as pd
import os 
import unicodedata

path = r'C:\Users\ryona\projects\AII\TCS\codes\words_gathering\src\temp.csv'

kks = pykakasi.kakasi()


# text ="アクティブ運用"
# textdata = ['こんにちは','漢字です','ATM','TMレボリューション','アクティブ運用']
alphabet = re.compile('[a-zA-Z]')
numbers = re.compile('\d')
katakana = re.compile('\p{Katakana}')
kanji = re.compile('\p{Han}')
Japanese = re.compile('(\p{Hiragana}|\p{Katakana}|\p{Han})')
non_japanese = re.compile('[^\p{Hiragana}|\p{Katakana}|\p{Han}|ー]')


def unicode_normalize(cls, s):
        pt = re.compile('([{}]+)'.format(cls))

        def norm(c):
            return unicodedata.normalize('NFKC', c) if pt.match(c) else c
                    
        s = ''.join(norm(x) for x in re.split(pt, s))
        s = re.sub('－', '-', s)
        return s

def remove_extra_spaces(s):
    s = re.sub('[  ]+', ' ', s)
    blocks = ''.join(('\u4E00-\u9FFF',  # CJK UNIFIED IDEOGRAPHS
                    '\u3040-\u309F',  # HIRAGANA
                    '\u30A0-\u30FF',  # KATAKANA
                    '\u3000-\u303F',  # CJK SYMBOLS AND PUNCTUATION
                    '\uFF00-\uFFEF'   # HALFWIDTH AND FULLWIDTH FORMS
                    ))
    basic_latin = '\u0000-\u007F'

    def remove_space_between(cls1, cls2, s):
        p = re.compile('([{}]) ([{}])'.format(cls1, cls2))
        while p.search(s):
            s = p.sub(r'\1\2', s)
        return s

    s = remove_space_between(blocks, blocks, s)
    s = remove_space_between(blocks, basic_latin, s)
    s = remove_space_between(basic_latin, blocks, s)
    return s

def normalize_ja(s):
    s = s.strip()
    s = unicode_normalize('０-９Ａ-Ｚａ-ｚ｡-ﾟ', s)

    def maketrans(f, t):
        return {ord(x): ord(y) for x, y in zip(f, t)}

    s = re.sub('[˗֊‐‑‒–⁃⁻₋−]+', '-', s)  # normalize hyphens
    s = re.sub('[﹣－ｰ—―─━ー]+', 'ー', s)  # normalize choonpus
    # s = re.sub('[~∼∾〜〰～]', '', s)  # remove tildes
    # s = re.sub('[0-9]', '', s)
            
    s = s.translate(
    maketrans('!"#$%&\'()*+,-./:;<=>?@[¥]^_`{|}~｡､･｢｣',
            '！”＃＄％＆’（）＊＋，－．／：；＜＝＞？＠［￥］＾＿｀｛｜｝〜。、・「」'))
    # s = re.sub(re.compile("[!-/:-@[-`{-~]"), '', s)
    # s = re.sub(re.compile('[!"#$%&\'()*+,-./:;<=>?@[¥]^_`{|}~｡､･｢｣]'), '', s)
    # s = re.sub(re.compile('[■□◆◇◯“…【】『』！”＃＄％＆’（）＊＋，－．／：；＜＝＞？＠［￥］＾＿｀｛｜｝〜。、・「」]'), '', s)
    s = remove_extra_spaces(s)
    s = unicode_normalize('！”＃＄％＆’（）＊＋，－．／：；＜＞？＠［￥］＾＿｀｛｜｝〜', s)  # keep ＝,・,「,」
    s = re.sub('[’]', '\'', s)
    s = re.sub('[”]', '"', s)
    # s = s.replace('\n','')
    # s = s.replace('\r','')
    #for ten (・)
    s = re.sub('・', '', s)
    return s
        
def interpret_to_kana(text):
    kana_result=[]
    other_result=[]

    if re.search(non_japanese, text) or re.search(alphabet, text):
        #exception to create dataset including exeptional words
        # write to csv for manual review
        other_result.append(text)
        other_result= ''.join(other_result)
        kana_result=''
    
    else:
        results = kks.convert(text)
        # kks split as per POS so join the text 
        for text_list in results:
            kana_result.append(text_list['kana'])
        kana_result= ''.join(kana_result)
        other_result= ''

    return kana_result,other_result

#parantheses processing start
path = r'C:\Users\ryona\projects\AII\TCS\codes\words_gathering\src\input'

res=[]

for filename in os.listdir(path):
    file_path = os.path.join(path,filename)
    df = pd.read_csv(file_path)
    # indices = df.loc[df.iloc[0].str.contains('\(|\)')].index.tolist()
    for i, row in df.iterrows():
        text=normalize_ja(row.iloc[0])
        if re.search('\(|\)',text):
            # for get contents including parantheses
            # if re.search('\(|\)',text)
            all = (re.search('(\(|（).*(）|\))',text))
            # between = (re.sub('\(|\)|（|）','',all[0]))
            # # for get rid of parentheses with contents inside
            # row['other'] = re.sub('(\(.*\))','',row['other'])
            res.append(re.sub('\(|\)|（|）','',all[0]))
            res.append(re.sub('(\(.*\))','',text))
        else:
            res.append(str(row.iloc[0]))

with open('temp.csv','a',encoding='UTF-8') as f:
    for item in res:
        f.write(f'{item}\n')

# end parantheses processing

# words to katakana
f_kana=[]
f_others=[]
f_orig=[]

df1 = pd.DataFrame()
df2 = pd.DataFrame()

output_index=0

df = pd.read_csv(path)

for index, row in df.iterrows():
    # kana,others = interpret_to_kana(normalize_ja("text"))
    output_index+=1

    # preprocess ()
    
    kana,others = interpret_to_kana(normalize_ja(str(row.iloc[0])))

    # print(type(kana))
    if not kana=="":
        df1.loc[output_index,'orig'] = str(row.iloc[0])
        df1.loc[output_index,'Kana'] = str(kana) 

    if not others=="":
        df2.loc[output_index, 'other'] = str(others)

# df1.drop_duplicates()
# df2.drop_duplicates()

df1.to_csv(f'output.csv', index=False, header=False, encoding='utf-8')
df2.to_csv(f'output_need_manual_review.csv', index=False,header=False,encoding='utf-8')
