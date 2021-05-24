from person import Person


def main():
    new_person = Person(name="Ibarbo", age=31)
    quote = new_person.introduce()
    print(quote)


if __name__ == '__main__':
    main()
