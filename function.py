
# Задание 1

# Измените функцию get_summ() чтобы результат выводился заглавными буквами использйте метод 'строка'.upper()
# Вызовите функцию, пердав в нее два аргумента "Learn" и "python"
# Сохраните результат вызова функции в переменную sum_string
# Выведите на экран значение переменной

# def get_summ(one, two, delimiter='&'):
#     return str(one) + str(delimiter) + str(two)
                        
def get_summ(one, two, delimiter='&'):
	result = str(one) + str(delimiter) + str(two)
	return result.upper()

sum_string = get_summ('Learn', 'python')
print(sum_string)
