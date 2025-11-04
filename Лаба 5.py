print("Регистрация участника конференции")
print("=" * 40)

# Ввод и проверка фамилии
while True:
    last_name = input("Введите фамилию: ").strip()
    if len(last_name) == 0:
        print("Ошибка: Фамилия не может быть пустой!")
        continue
    if len(last_name) < 2:
        print("Ошибка: Фамилия должна содержать минимум 2 буквы!")
        continue
    if not last_name.isalpha():
        print("Ошибка: Фамилия должна содержать только буквы!")
        continue
    break

# Ввод и проверка имени
while True:
    first_name = input("Введите имя: ").strip()
    if len(first_name) == 0:
        print("Ошибка: Имя не может быть пустой!")
        continue
    if len(first_name) < 2:
        print("Ошибка: Имя должно содержать минимум 2 буквы!")
        continue
    if not first_name.isalpha():
        print("Ошибка: Имя должно содержать только буквы!")
        continue
    break

# Ввод и проверка возраста
while True:
    age_input = input("Введите возраст: ").strip()
    if not age_input.isdigit():
        print("Ошибка: Возраст должен быть числом!")
        continue
    
    age = int(age_input)
    if age < 18:
        print("Ошибка: Минимальный возраст участия - 18 лет!")
        continue
    if age > 90:
        print("Ошибка: Максимальный возраст участия - 90 лет!")
        continue
    break

# Ввод и проверка формата участия
while True:
    format_input = input("Введите формат участия (онлайн/оффлайн): ").strip().lower()
    if format_input not in ['онлайн', 'оффлайн']:
        print("Ошибка: Формат участия должен быть 'онлайн' или 'оффлайн'!")
        continue
    break

# Формирование билета
print("\n" + "=" * 40)
print("БИЛЕТ УЧАСТНИКА КОНФЕРЕНЦИИ")
print("=" * 40)
print(f"Фамилия: {last_name.upper()}")
print(f"Имя: {first_name.upper()}")
print(f"Возраст: {age} лет")
print(f"Формат участия: {format_input.upper()}")
print("=" * 40)