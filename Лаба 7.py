# Ввод цитаты от пользователя
quote = input("Введите цитату: ")

# Инициализация переменных
corrected_quote = ""
has_errors = False
punctuation_marks = ['.', ',', '!', '?']

# Анализ текста посимвольно с помощью цикла for
for i in range(len(quote)):
    current_char = quote[i]
    corrected_quote += current_char
    
    # Проверяем, является ли текущий символ знаком препинания
    if current_char in punctuation_marks:
        # Если это не последний символ и следующий символ не пробел
        if i < len(quote) - 1 and quote[i + 1] != ' ':
            corrected_quote += ' '  # Добавляем пробел после знака препинания
            has_errors = True

# Вывод исправленной цитаты
print("\nИсправленная цитата:")
print(corrected_quote)

# Вывод предупреждения, если были обнаружены ошибки
if has_errors:
    print("\n⚠ Внимание: обнаружены пропущенные пробелы после знаков препинания и исправлены.")
else:
    print("\nОшибок в расстановке пробелов после знаков препинания не обнаружено.")