contacts = [
    {"name": "John", "phones": ["123456"]},
    {"name": "Jane", "phones": ["564321"]},
    {"name": "Bob", "phones": ["+1234"]}
]

def list_contacts(contact_list):
    print("Имя       Номер")
    print("--------------------")
    for contact in contact_list:
        print(f"{contact['name']}    {contact['phones']}") 

def find_contact(contact_list):
    search_name = input('Имя: ')
    for contact in contact_list:
        if search_name == contact['name']:
            print(f">> Контакт найден:  {contact['name']}")
            for i in range(len(contact['phones'])):
                print(f"{i + 1}. {contact['phones'][i]}")
            return
    print(f">> Извините, у вас нет контакта с именем {search_name}")

def add_contact(contact_list):
    name = input(">> Введите имя нового контакта: ")
    for contact in contact_list:
        if name == contact['name']:
            print(f">> Контакт {name} уже существует")
            return
    phone = input(">> Введите номер телефона: ")
    contact_list.append({"name": name, "phones": [phone]}) 
    print(f">> Контакт {name} добавлен успешно")

def edit_contact(contact_list):
    name = input(">> Введите имя контакта для редактирования: ")
    for contact in contact_list:
        if name == contact['name']:
            print(f">> Редактирование контакта: {contact['name']}")
            for index, phone in enumerate(contact['phones']):
                print(f"{index + 1}. {phone}")  
            old_phone = input(">> Введите номер телефона, который вы хотите редактировать: ")
            if old_phone in contact['phones']:
                new_phone = input("Введите новый номер телефона: ")
                phone_index = contact['phones'].index(old_phone)  
                contact['phones'][phone_index] = new_phone  
                print(f">> Контакт обновлён: {contact['name']} - {contact['phones']}")
            else:
                print(f">> Номер телефона {old_phone} не найден.")
            return
    print(f"Контакт {name} не найден.")

def add_phone_to_contact(contact_list):
    name = input(">> Введите имя контакта, к которому нужно добавить номер: ")
    for contact in contact_list:
        if name == contact['name']:
            new_phone = input("Введите новый номер телефона: ")
            contact['phones'].append(new_phone)
            print(f"Номер телефона добавлен к контакту {name}.")
            return
    print(f">> Контакт {name} не найден.")

def delete_phone_from_contact(contact_list):
    name = input(">> Введите имя контакта, из которого нужно удалить номер: ")
    for contact in contact_list:
        if name == contact['name']:
            print(f">> Текущие номера телефонов для {name}:")
            for index, phone in enumerate(contact['phones']):
                print(f"{index + 1}. {phone}")
            phone_index = int(input(">> Какой номер телефона вы хотите удалить (введите номер): ")) - 1
            if 0 <= phone_index < len(contact['phones']):
                removed_phone = contact['phones'].pop(phone_index)
                print(f">> Номер телефона {removed_phone} удалён из контакта {name}.")
            else:
                print(">> Недопустимый индекс.")
            return
    print(f">> Контакт {name} не найден.")

def delete_contact(contact_list):
    name = input(">> Введите имя контакта для удаления: ")
    for contact in contact_list:
        if name == contact['name']:
            confirm = input(f">> Вы уверены, что хотите удалить {name}? (Да/Нет): ")
            if confirm.lower() == "да":  
                contact_list.remove(contact)
                print(f">> Контакт {name} удалён.")
            else:
                print(">> Удаление отменено.")
            return
    print(f">> Контакт {name} не найден.")

def sort_contacts(contact_list):
    contact_list.sort(key=lambda contact: contact['name'])
    print(">> Контакты отсортированы!")

while True:
    print(">> 1. List contacts")
    print(">> 2. Find contact")
    print(">> 3. Add contact")
    print(">> 4. Edit contact")
    print(">> 5. Add phone to contact")
    print(">> 6. Delete phone from contact")
    print(">> 7. Delete contact")
    print(">> 8. Sort contacts")
    print(">> 9. Exit")
    
    choice = input(">> Выберите опцию (цифру): ")
    
    if choice == "1":
        list_contacts(contacts)
    elif choice == "2":
        find_contact(contacts)
    elif choice == "3":
        add_contact(contacts)
    elif choice == "4":
        edit_contact(contacts)
    elif choice == "5":
        add_phone_to_contact(contacts)
    elif choice == "6":
        delete_phone_from_contact(contacts)
    elif choice == "7":
        delete_contact(contacts)
    elif choice == "8":
        sort_contacts(contacts)
    elif choice == "9":
        print(">> До свидания!")
        break
    else:
        print('>> Error')
