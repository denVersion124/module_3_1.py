calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()  # Считаем вызов
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (length, upper_case, lower_case)

def is_contains(string, list_to_search):
    count_calls()  # Считаем вызов
    # Проверяем, содержится ли строка в списке, игнорируя регистр
    return string.lower() in (item.lower() for item in list_to_search)
result1 = string_info("Пример строки")
result2 = string_info("Тестовая строка")
contains_result = is_contains("urban", ["Urban", "City", "Town"])

# Вывод результатов
print("Результат string_info для 'Пример строки':", result1)
print("Результат string_info для 'Тестовая строка':", result2)
print("Результат is_contains для 'urban':", contains_result)

# Вывод количества вызовов
print("Количество вызовов функций:", calls)


