lecture=["Аня","Борис","Вика","Гоша","Аня"]
seminar=["Вика","Дима","Борис","Ева"]
print(f"всего уникальных студентов:{len(set(lecture+seminar))}")
print(f"на обеих парах:{list(set(lecture)&set(seminar))}")
print(f"только на лекции:{list(set(lecture)-set(seminar))}")
print(f"хотя бы на одной:{list(set(lecture)|set(seminar))}")
