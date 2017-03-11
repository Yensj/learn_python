#...

first_var = input('Введите первую переменную: ')
second_var = input('Введите вторую переменную: ')
def get_summ(first_var, second_var):
	result = str(first_var) + '...' + str(second_var)
	return result.upper()

print(get_summ(first_var, second_var))