def total_salary(path):
    """
    Аналізує файл з заробітними платами розробників і повертає загальну та середню суму.
    
    Args:
        path (str): Шлях до текстового файлу з даними про заробітні плати
        
    Returns:
        tuple: Кортеж із двох чисел (загальна сума, середня заробітна плата)
        
    Raises:
        FileNotFoundError: Якщо файл не знайдено
        ValueError: Якщо файл містить некоректні дані
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        if not lines:
            return 0, 0
            
        total = 0
        count = 0
        
        for line in lines:
            line = line.strip()
            if not line:  # Пропускаємо порожні рядки
                continue
                
            try:
                # Розділяємо рядок по комі
                parts = line.split(',')
                if len(parts) != 2:
                    raise ValueError(f"Некоректний формат рядка: {line}")
                
                # Отримуємо заробітну плату (друга частина після коми)
                salary = float(parts[1])
                total += salary
                count += 1
                
            except (ValueError, IndexError) as e:
                raise ValueError(f"Помилка обробки рядка '{line}': {e}")
        
        if count == 0:
            return 0, 0
            
        average = total / count
        return int(total), int(average)
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{path}' не знайдено")
    except Exception as e:
        raise Exception(f"Помилка при читанні файлу: {e}")


# Приклад використання
if __name__ == "__main__":
    # Тестуємо функцію
    try:
        total, average = total_salary("salaries.txt")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception as e:
        print(f"Помилка: {e}")
