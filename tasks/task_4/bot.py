#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def parse_input(user_input):
    """
    Парсер команд - розбирає введений користувачем рядок на команду та її аргументи.
    
    Args:
        user_input (str): Введений користувачем рядок
        
    Returns:
        tuple: (команда, список аргументів)
    """
    parts = user_input.split()
    if not parts:
        return "", []
    cmd, *args = parts
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    """
    Додає новий контакт до словника контактів.
    
    Args:
        args (list): Список аргументів [ім'я, телефон]
        contacts (dict): Словник контактів
        
    Returns:
        str: Повідомлення про результат операції
    """
    if len(args) != 2:
        return "Invalid command format. Use: add <name> <phone>"
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Змінює номер телефону для існуючого контакту.
    
    Args:
        args (list): Список аргументів [ім'я, новий_телефон]
        contacts (dict): Словник контактів
        
    Returns:
        str: Повідомлення про результат операції
    """
    if len(args) != 2:
        return "Invalid command format. Use: change <name> <new_phone>"
    
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    """
    Показує номер телефону для зазначеного контакту.
    
    Args:
        args (list): Список аргументів [ім'я]
        contacts (dict): Словник контактів
        
    Returns:
        str: Номер телефону або повідомлення про помилку
    """
    if len(args) != 1:
        return "Invalid command format. Use: phone <name>"
    
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    """
    Показує всі збережені контакти.
    
    Args:
        contacts (dict): Словник контактів
        
    Returns:
        str: Список всіх контактів або повідомлення про відсутність
    """
    if not contacts:
        return "No contacts found."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    
    return "\n".join(result)

def main():
    """
    Головна функція бота-помічника.
    Управляє основним циклом обробки команд.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
