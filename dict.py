
# Создайте такой словарь:
# {"city": "Москва", "temperature": "20"}
# Выведите на экран значение по ключу city
# Уменьшите значение "temperature" на 5
# Выведите на экран весь словарь

weather = {"city": "Москва", "temperature": "20"}
print(weather['city'])
weather['temperature'] = str(int(weather['temperature']) - 5)
print(weather)


# Проверьте, есть ли в словаре ключ country
# Выведите значение по-умолчанию "Россия" для ключа country
# Добавьте в словарь элемент date со значением '27.05.2017'
# Выведите на экран длину словаря

print(weather.get('country', 'Россия'))
weather['date'] = '27.05.2017'
print(weather)
