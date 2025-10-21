#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізуємо colorama для кольорового виведення
init(autoreset=True)

def visualize_directory_structure(directory_path, prefix="", is_last=True):
    """
    Рекурсивно візуалізує структуру директорії з кольоровим виведенням.
    
    Args:
        directory_path (Path): Шлях до директорії
        prefix (str): Префікс для відступу
        is_last (bool): Чи є це останній елемент
    """
    try:
        # Отримуємо список елементів у директорії
        items = sorted(Path(directory_path).iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        
        for i, item in enumerate(items):
            is_last_item = i == len(items) - 1
            
            # Визначаємо символ для поточного елемента
            if is_last_item:
                current_prefix = "┗ "
                next_prefix = prefix + "   "
            else:
                current_prefix = "┣ "
                next_prefix = prefix + "┃ "
            
            # Визначаємо колір та символ залежно від типу
            if item.is_dir():
                # Директорія - синій колір
                color = Fore.BLUE
                icon = "📂"
                name = item.name
            else:
                # Файл - зелений колір
                color = Fore.GREEN
                icon = "📜"
                name = item.name
            
            # Виводимо поточний елемент
            print(f"{prefix}{current_prefix}{color}{icon} {name}{Style.RESET_ALL}")
            
            # Рекурсивно обробляємо піддиректорії
            if item.is_dir():
                visualize_directory_structure(item, next_prefix, is_last_item)
                
    except PermissionError:
        print(f"{prefix}┗ {Fore.RED}📁 [Доступ заборонено]{Style.RESET_ALL}")
    except Exception as e:
        print(f"{prefix}┗ {Fore.RED}📁 [Помилка: {e}]{Style.RESET_ALL}")

def main():
    """
    Головна функція скрипта.
    """
    # Перевіряємо кількість аргументів
    if len(sys.argv) != 2:
        print(f"{Fore.RED}❌ Помилка: Неправильна кількість аргументів{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Використання: python hw03.py <шлях_до_директорії>{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Приклад: python hw03.py /шлях/до/вашої/директорії{Style.RESET_ALL}")
        sys.exit(1)
    
    # Отримуємо шлях до директорії
    directory_path = sys.argv[1]
    
    # Перевіряємо, чи існує шлях
    if not os.path.exists(directory_path):
        print(f"{Fore.RED}❌ Помилка: Шлях '{directory_path}' не існує{Style.RESET_ALL}")
        sys.exit(1)
    
    # Перевіряємо, чи це директорія
    if not os.path.isdir(directory_path):
        print(f"{Fore.RED}❌ Помилка: '{directory_path}' не є директорією{Style.RESET_ALL}")
        sys.exit(1)
    
    # Конвертуємо в Path об'єкт
    path_obj = Path(directory_path)
    
    # Виводимо заголовок
    print(f"{Fore.MAGENTA}📦 {path_obj.name}{Style.RESET_ALL}")
    
    # Візуалізуємо структуру директорії
    try:
        visualize_directory_structure(path_obj)
        print(f"\n{Fore.GREEN}✅ Структура директорії успішно відображена{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}❌ Помилка при візуалізації: {e}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()
