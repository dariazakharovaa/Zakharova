# ВВОД ДАННЫХ
name = input("Введите ваше имя: ")
anxiety_score = int(input("Введите ваш балл по шкале тревоги (целое число от 20 до 80): "))
user_text = input("Опишите, как вы себя чувствуете (ответьте на вопрос «Как вы себя чувствуете?»): ").lower()

print("\n" + "=" * 40)
print("РЕЗУЛЬТАТ АНАЛИЗА СОСТОЯНИЯ")
print("=" * 40)
print(f"Имя: {name}")

# АНАЛИЗ УРОВНЯ ТРЕВОГИ
if anxiety_score <= 30:
    anxiety_level = "низкий"
elif 31 <= anxiety_score <= 44:
    anxiety_level = "умеренный"
else:
    anxiety_level = "высокий"

print(f"Балл тревоги: {anxiety_score} -> {anxiety_level}")

# АНАЛИЗ ТЕКСТА НА МАРКЕРЫ
anxiety_keywords = ["тревога", "страх", "боюсь", "паника"]
positive_keywords = ["надежда", "спокойствие", "радость"]

has_anxiety = any(word in user_text for word in anxiety_keywords)
has_positive = any(word in user_text for word in positive_keywords)

print("АНАЛИЗ ЭМОЦИОНАЛЬНЫХ МАРКЕРОВ")

if has_anxiety and not has_positive:
    print("Обнаружены признаки тревоги")
elif has_positive and not has_anxiety:
    print("Текст имеет позитивную окраску")
else:
    print("Смешанные или нейтральные эмоции")

# КОМПЛЕКСНАЯ ОЦЕНКА
print("ИТОГ")

if anxiety_level == "высокий" or (has_anxiety and not has_positive):
    print("Рекомендуется срочная психологическая поддержка")
else:
    print("Состояние в пределах ожидаемого. Продолжайте наблюдение.")