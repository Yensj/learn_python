#...

def ask_user():
    while True:
        print('Как дела?')
        user_answer = input()
        if user_answer == 'Хорошо':
            break
ask_user()
