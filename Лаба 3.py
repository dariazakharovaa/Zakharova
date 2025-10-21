# Анализ журнала сессий психолога

# 1. Создать список эмоциональных состояний пациентов
states = [
    "чувствую тревогу и беспокойство",
    "состояние паники",
    "чувствую подавленность и грусть",
    "сильная тревога перед выходом из дома",
    "ощущение пустоты",
    "тревога из-за работы",
    "чувствую себя лучше после сессии"
]

print("1. Список эмоциональных состояний:")
for i, state in enumerate(states, 1):
    print(f"{i}. {state}")

# 2. Добавить новое состояние
new_state = "чувствую тревогу в общественных местах"
states.append(new_state)
print(f"\n2. Добавлено новое состояние: '{new_state}'")
print(f"Всего состояний: {len(states)}")

# 3. Вывести каждое третье состояние
print("\n3. Каждое третье состояние:")
for i in range(0, len(states), 3):
    print(f"{i+1}. {states[i]}")

# 4. Найти самое длинное описание состояния
longest_state = max(states, key=len)
print(f"\n4. Самое длинное описание: '{longest_state}'")
print(f"Длина: {len(longest_state)} символов")

# 5. Посчитать, сколько раз встречалось слово "тревога"
anxiety_count = 0
anxiety_states = []

for state in states:
    if 'тревог' in state.lower():
        anxiety_count += 1
        anxiety_states.append(state)

print(f"\n5. Слово 'тревога' встречается: {anxiety_count} раз(а)")
if anxiety_states:
    print("В этих состояниях:")
    for state in anxiety_states:
        print(f"- {state}")

# 6. Вывести все состояния начинающиеся со слова "чувствую"
print("\n6. Состояния, начинающиеся со слова 'чувствую':")
feeling_states = []

for state in states:
    if state.startswith('чувствую'):
        feeling_states.append(state)

if feeling_states:
    for i, state in enumerate(feeling_states, 1):
        print(f"{i}. {state}")
else:
    print("Таких состояний нет")

# Сводка для психолога
print("\n" + "="*50)
print("СТАТИСТИКА ДЛЯ ПСИХОЛОГА:")
print(f"Всего записей в журнале: {len(states)}")
print(f"Состояний с тревогой: {anxiety_count}")
print(f"Состояний, начинающихся с 'чувствую': {len(feeling_states)}")
print(f"Самое подробное описание: '{longest_state}'")