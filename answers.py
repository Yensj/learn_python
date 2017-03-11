#...

question = input()
def get_answer(question):
	answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
	result = answers.get(question, 'invalid key')
	return result.lower()

print(get_answer(question))