import pykakasi
import regex as re
import pandas as pd
import romkan
import os 
path = r'C:\Users\ryona\projects\AII\TCS\codes\words_gathering\pre_interpreted'

kks = pykakasi.kakasi()


# text ="アクティブ運用"
# textdata = ['こんにちは','漢字です','ATM','TMレボリューション','アクティブ運用']
alphabet = re.compile('[a-zA-Z]')
numbers = re.compile('\d')
katakana = re.compile('\p{Katakana}')
kanji = re.compile('\p{Han}')
Japanese = re.compile('(\p{Hiragana}|\p{Katakana}|\p{Han})')
non_japanese_alpha = re.compile('[^\p{Hiragana}|\p{Katakana}|\p{Han}|a-zA-Z| |・|ー|（|）|)]')

def interpret_to_kana(text):
    text = text

    f=[]
    if re.search(non_japanese_alpha, text):
        #exception to create dataset including exeptional words
        print(re.findall(non_japanese_alpha, text))
        pass
        
    
    elif re.search(alphabet, text):
        text = romkan.to_katakana(text)
        results = kks.convert(text)
        for r in results:
        #アクティブATM
        #
            f.append(r['kana'])
        f= ''.join(f)
        return f
    
    elif re.search(Japanese, text):
        results = kks.convert(text)
        for r in results:
        #アクティブ
        #運用
            f.append(r['kana'])
        f= ''.join(f)
        return f
    #add kana to dataframe to the same index
    
for filename in os.listdir(path):
    join_path = os.path.join('pre_interpreted',filename)
    df= pd.read_csv(join_path)
    df2 = pd.DataFrame(columns=df.columns)
    for i in range(len(df)):
        row_index = df.index[i]
        textdata =df.loc[row_index, "words"]
        kana = interpret_to_kana(textdata)
        if kana:
            df.loc[row_index, 'Kana'] = str(kana)
        else:
            row = df.loc[row_index]
            df2 = df2.append(row, ignore_index=True)

    df.to_csv(f'{filename}_with_kana.csv', index=False,encoding='utf-8')
    df2.to_csv(f'{filename}_needmodified.csv', index=False,encoding='utf-8')


## FOR MULTIPLE TEXT DATA
    # for text in textdata:
    #     #アクティブ運用
    #     if re.search(pattern, text):
    #         pass
    #     else:
    #         results = kks.convert(text)
    #         f = []
    #         for r in results:
    #         #アクティブ
    #         #運用
    #             f.append(r['kana'])
    #         f= ''.join(f)
    #         fullwords.append(f)
    # return fullwords