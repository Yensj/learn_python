#...

def ask_user():
    while True:
        print('Как дела?')
        user_answer = input()
        if user_answer == 'Хорошо':
            break
        elif user_answer == 'Пока':
            break
        else:
            print('Сам ты {}'.format(user_answer))
ask_user()
