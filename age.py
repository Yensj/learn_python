#...

user_age = float(input("Укажите ваш возраст: "))
if user_age < 7:
    print('Скорее всего вы посещаете детский сад')
elif 7 <= user_age < 18:
    print('Скорее всего вы ходите в школу')
elif 18 <= user_age < 23:
    print('Скорее всего вы учитесь в институте')
else:
    print('Скорее всего вы работаете')

#n_check = float.is_integer(user_age)
#if n_check = 'True':
#    print('correct')
#    else:
#        print('wrong')