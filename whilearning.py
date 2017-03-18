#...

names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
size_names = len(names)
while size_names > 0:
    size_names = size_names - 1
    find_name = names.pop(size_names)
    if find_name == 'Валера':
        print('Валера нашелся')
        break