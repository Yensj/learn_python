#...

names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
def find_person(name):
	names_delta = names
    size_names = len(names_delta)
    while size_names > 0:
        size_names = size_names - 1
        find_name = names_delta.pop(size_names)
        if find_name == name:
            print('{} нашелся'.format(name))
            break
name = input('Введите имя для поиска: ')
find_person(name)