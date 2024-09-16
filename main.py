from abc import ABC, abstractmethod

class UserView(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass
    
    @abstractmethod
    def display_help(self):
        pass

class ConsoleUserView(UserView):
    def display_contacts(self, contacts):
        print("Список контактів:")
        for contact in contacts:
            print(f"Ім'я: {contact['name']}, Телефон: {contact['phone']}")
    
    def display_help(self):
        print("Доступні команди:")
        print("1. add - Додати контакт")
        print("2. list - Показати контакти")
        print("3. exit - Вихід з програми")

if __name__ == "__main__":
    contacts = [
        {"name": "Іван", "phone": "123-456"},
        {"name": "Марія", "phone": "987-654"},
    ]

    user_view = ConsoleUserView()
    
    while True:
        user_view.display_help()
        command = input("Введіть команду: ")
        
        if command == "list":
            user_view.display_contacts(contacts)
        elif command == "add":
            name = input("Введіть ім'я контакту: ")
            phone = input("Введіть телефон контакту: ")
            contacts.append({"name": name, "phone": phone})
        elif command == "exit":
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")