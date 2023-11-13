rus_to_eng = {"Привет": "Hello", "Я": "I'm", "Компьютер": "Computer"}

rus = input("Введите строку").split(" ")
rus = [_.capitalize() for _ in rus]

eng = [rus_to_eng.get(x.capitalize()) if rus_to_eng.get(x) else x for x in rus]
print(eng)
