words=["кот","пёс","кот","кот","ёж","пёс","кот"]
groups={}
for w in words:
    key=w[0]  #берем первую букву слова
    if key not in groups:
        groups[key]=[]  #создаем пустой список для этой буквы
    groups[key].append(w) #добавляем слово в список
print("1.",groups["к"][0],"-",len(groups["к"]))
print("2.",groups["п"][0],"-",len(groups["п"]))
print("3.",groups["ё"][0],"-",len(groups["ё"]))
