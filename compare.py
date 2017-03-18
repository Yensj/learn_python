#...

first_str = input("Введите первую строку: ")
second_str = input("Введите вторую строку: ")
if str(first_str) == str(second_str):
    print('1')
elif str(first_str) > str(second_str):
    if second_str == 'learn':
        print('3')
    else: 
        print('2')