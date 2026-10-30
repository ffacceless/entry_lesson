text=input().replace(",", "").replace(".", "").replace("—", "").lower()
words=text.split()
print(f"всего слов: {len(words)} ,из них уникальных: {len(set(words))}")
counts={}
for w in words:
    if w in counts:
      counts[w]+=1
    else:
      counts[w]=1
top=sorted(counts,key=counts.get,reverse=True)[:5]
print("топ-5 слов:",", ".join(f"{w} ({counts[w]})" for w in top))
maxlen=0
for w in words:
    if len(w)>maxlen:
        maxlen=len(w)
longwords=[]
for w in words:
    if len(w)==maxlen and w not in longwords:
        longwords.append(w)
print("самое длинное слово:",", ".join(longwords))
lengths={}
for w in words:
    if len(w) in lengths:
        lengths[len(w)]+=1
    else:
        lengths[len(w)]=1
print("слова по длинам:",lengths)
