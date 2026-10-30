catalog = [
    {"title": "Мастер и Маргарита", "author": "Булгаков", "year": 1967, "genre": "роман", "on_loan": True},
    {"title": "Евгений Онегин", "author": "Пушкин", "year": 1833, "genre": "роман", "on_loan": False},
    {"title": "Стихотворения", "author": "Есенин", "year": 1926, "genre": "поэзия", "on_loan": False},
    {"title": "Вишнёвый сад", "author": "Чехов", "year": 1904, "genre": "пьеса", "on_loan": True},
    {"title": "Руслан и Людмила", "author": "Пушкин", "year": 1820, "genre": "поэма", "on_loan": False},
    {"title": "Три сестры", "author": "Чехов", "year": 1901, "genre": "пьеса", "on_loan": False},
]
def find_by_author(catalog, author):
    result=[]
    for book in catalog:
        if book["author"]==author:
            result.append(book["title"])
    return result
def available_titles(catalog):
    result=[]
    for book in catalog:
        if book["on_loan"]==False:
            result.append(book["title"])
    return result
def books_grouped_by_genre(catalog):
    res={}
    for book in catalog:
        if book["on_loan"]==False:
            genre=book["genre"]
            if genre not in res:
                res[genre]=[]
            res[genre].append(book["title"])
    return res
print("книги Пушкина:", find_by_author(catalog, "Пушкин"))
print("книги Чехова:", find_by_author(catalog, "Чехов"))
print("доступные книги:", available_titles(catalog))
grouped=books_grouped_by_genre(catalog)
for genre in grouped:
    print(genre, ":", grouped[genre])
