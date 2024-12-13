data = open('Poems.txt', encoding="utf8").read() 
line_by_line = data.split('\n')
titles = []
texts = []
text = []
for idx, line in enumerate(line_by_line):
    print(line)
    completed = False
    if line.startswith('\"'):
        titles.append(line)
        completed = True
        if completed == True and idx != 0:
            texts.append(text)
            text = []
    elif not line.startswith('by'):
        text.append(line)  

    if idx > 70:
        break     

print(titles)
print(texts)