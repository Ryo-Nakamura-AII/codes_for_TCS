import regex

p = regex.compile('[〇一二三四五六七八九十百千万億兆]{3,}')

with open('number.txt', 'r',encoding="UTF-8") as f:
    with open('train.txt', 'w',encoding="UTF-8") as newfile:
        Lines = f.readlines()
        for line in Lines:
            if p.search(line):
                while p.search(line):
                    line = regex.sub('[〇]','0',line)
                    line = regex.sub('[一]','1',line)
                    line = regex.sub('[二]','2',line)
                    line = regex.sub('[三]','3',line)
                    line = regex.sub('[四]','4',line)
                    line = regex.sub('[五]','5',line)
                    line = regex.sub('[六]','6',line)
                    line = regex.sub('[七]','7',line)
                    line = regex.sub('[八]','8',line)
                    line = regex.sub('[九]','9',line)
                    newfile.write(line)
            else:
                newfile.write(line)
            
            
        
        
        
        
#     p = regex.compile('[〇一二三四五六七八九十百千万億兆]{5,}')
# numbers = p.findall('商品番号一二三四五 電話番号〇九〇五五三七八二〇六')



# for n in numbers:
#     for j_n in n:
#         if j_n == "〇":
#             print(regex.sub('[〇]','0',j_n))
#         if j_n == "一":
#             print(regex.sub('[一]','1',j_n))
#         if j_n == "二":
#             print(regex.sub('[二]','2',j_n))
#         if j_n == "三":
#             print(regex.sub('[三]','3',j_n))