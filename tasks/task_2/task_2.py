def get_cats_info(path):
    """
    Читає файл з інформацією про котів та повертає список словників.
    
    Args:
        path (str): Шлях до текстового файлу з даними про котів
        
    Returns:
        list: Список словників, де кожен словник містить інформацію про одного кота
              з ключами "id", "name", "age"
        
    Raises:
        FileNotFoundError: Якщо файл не знайдено
        ValueError: Якщо файл містить некоректні дані
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        cats_info = []
        
        for line in lines:
            line = line.strip()
            if not line:  # Пропускаємо порожні рядки
                continue
                
            try:
                # Розділяємо рядок по комі
                parts = line.split(',')
                if len(parts) != 3:
                    raise ValueError(f"Некоректний формат рядка: {line}")
                
                # Створюємо словник з інформацією про кота
                cat_info = {
                    "id": parts[0].strip(),
                    "name": parts[1].strip(),
                    "age": parts[2].strip()
                }
                
                cats_info.append(cat_info)
                
            except (ValueError, IndexError) as e:
                raise ValueError(f"Помилка обробки рядка '{line}': {e}")
        
        return cats_info
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{path}' не знайдено")
    except Exception as e:
        raise Exception(f"Помилка при читанні файлу: {e}")


# Приклад використання
if __name__ == "__main__":
    # Тестуємо функцію
    try:
        cats_info = get_cats_info("cats.txt")
        print("Інформація про котів:")
        for cat in cats_info:
            print(f"ID: {cat['id']}, Ім'я: {cat['name']}, Вік: {cat['age']}")
    except Exception as e:
        print(f"Помилка: {e}")
