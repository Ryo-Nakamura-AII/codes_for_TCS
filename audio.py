import regex
import requests

p = regex.compile('(mp3)')


# with open('audio.txt' ,'r',encoding="UTF-8") as f:
#     with open('mp3s.txt', 'w',encoding="UTF-8") as fw:
#         Lines = f.readlines()
#         for line in Lines:
#             if p.search(line):
#                 fw.write(line)

with open('audio.txt' ,'r',encoding="UTF-8") as f:
    Lines = f.readlines()
    for i, line in enumerate(Lines):
        if p.search(line):
            doc = requests.get(line)
            with open("myfile_"+str(i)+".mp3" ,'wb') as fw:
                fw.write(doc.content)