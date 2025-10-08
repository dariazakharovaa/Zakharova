def main():
    print("Добро пожаловать в универсальный конвертер величин!")
    print("=" * 50)
    
    while True:
        print("\nГлавное меню:")
        print("1. Метры ↔ Километры")
        print("2. Цельсий ↔ Фаренгейт")
        print("3. Килограммы ↔ Фунты")
        print("4. м/с ↔ км/ч")
        print("5. Сантиметры ↔ Дециметры")
        print("0. Выход")
        
        choice = input("\nВыберите операцию (0-5): ")
        
        if choice == '0':
            print("Спасибо за использование! До свидания!")
            break
            
        elif choice == '1':
            print("\n--- Метры ↔ Километры ---")
            dir_choice = input("1 - Метры в Километры\n2 - Километры в Метры\nВыберите: ")
            
            try:
                value = float(input("Введите значение: "))
                if dir_choice == '1':
                    result = value / 1000
                    print(f"{value} м = {result} км")
                elif dir_choice == '2':
                    result = value * 1000
                    print(f"{value} км = {result} м")
                else:
                    print("Неверный выбор!")
            except:
                print("Ошибка! Введите число.")
                
        elif choice == '2':
            print("\n--- Цельсий ↔ Фаренгейт ---")
            dir_choice = input("1 - Цельсий в Фаренгейт\n2 - Фаренгейт в Цельсий\nВыберите: ")
            
            try:
                value = float(input("Введите значение: "))
                if dir_choice == '1':
                    result = (value * 9/5) + 32
                    print(f"{value}°C = {result}°F")
                elif dir_choice == '2':
                    result = (value - 32) * 5/9
                    print(f"{value}°F = {result}°C")
                else:
                    print("Неверный выбор!")
            except:
                print("Ошибка! Введите число.")
                
        elif choice == '3':
            print("\n--- Килограммы ↔ Фунты ---")
            dir_choice = input("1 - Килограммы в Фунты\n2 - Фунты в Килограммы\nВыберите: ")
            
            try:
                value = float(input("Введите значение: "))
                if dir_choice == '1':
                    result = value * 2.20462
                    print(f"{value} кг = {result} фунтов")
                elif dir_choice == '2':
                    result = value / 2.20462
                    print(f"{value} фунтов = {result} кг")
                else:
                    print("Неверный выбор!")
            except:
                print("Ошибка! Введите число.")
                
        elif choice == '4':
            print("\n--- м/с ↔ км/ч ---")
            dir_choice = input("1 - м/с в км/ч\n2 - км/ч в м/с\nВыберите: ")
            
            try:
                value = float(input("Введите значение: "))
                if dir_choice == '1':
                    result = value * 3.6
                    print(f"{value} м/с = {result} км/ч")
                elif dir_choice == '2':
                    result = value / 3.6
                    print(f"{value} км/ч = {result} м/с")
                else:
                    print("Неверный выбор!")
            except:
                print("Ошибка! Введите число.")
                
        elif choice == '5':
            print("\n--- Сантиметры ↔ Дециметры ---")
            dir_choice = input("1 - Сантиметры в Дециметры\n2 - Дециметры в Сантиметры\nВыберите: ")
            
            try:
                value = float(input("Введите значение: "))
                if dir_choice == '1':
                    result = value / 10
                    print(f"{value} см = {result} дм")
                elif dir_choice == '2':
                    result = value * 10
                    print(f"{value} дм = {result} см")
                else:
                    print("Неверный выбор!")
            except:
                print("Ошибка! Введите число.")
                
        else:
            print("Неверный выбор! Введите число от 0 до 5.")
        
        if choice != '0':
            input("\nНажмите Enter чтобы продолжить...")

if __name__ == "__main__":
    main()