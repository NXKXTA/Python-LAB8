library = {
    "Булгаков": ["Собачье сердце", "Мастер и Маргарита", "Белая гвардия"],
    "Пушкин": ["Евгений Онегин", "Капитанская дочка", "Дубровский"],
    "Гоголь": ["Мертвые души"],
}


def add_book(author):
    while True:
        book = input("Введите названия добавляемых произведений через запятую:").split(
            sep=","
        )
        if author not in library:
            library[author] = book
            return 0
        library[author].extend(book)
        break


def get_author():
    while True:
        choice = input(
            f"Введите фамилию нужного автора из списка:{[_ for _ in library.keys()]} либо нажмите Enter для выхода в меню\n"
        )
        if library.get(choice):
            print(f"Книги по запросу {choice}: {[_ for _ in library.get(choice)]}\n")
        else:
            print("Выбранного вами автора нет в библиотеке\n")
            break


print(
    "///////////////////////////////////////////\n"
    "//       Программа для взаимодействия    //\n"
    "//              со словарём:             //\n"
    "//     end - выход из программы          //\n"
    "//     get - получить список книг автора //\n"
    "//     add - добавить книги автора       //\n"
    "//                                       //\n"
    "///////////////////////////////////////////\n"
)
while True:
    x = input("Выйти/дополнить/получить список : end/add/get: ")
    if x == "end":
        break
    elif x == "add":
        auth = input("Введите фамилию нужного автора:")
        add_book(auth)
        print(f"Книги в библиотеке:{library}\n")
    elif x == "get":
        get_author()
    else:
        print("Такой команды нет\n")
