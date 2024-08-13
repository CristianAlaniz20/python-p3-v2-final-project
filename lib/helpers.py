# lib/helpers.py

from models.client import Client

spacing = "-----------------------------"

def exit_program():
    print("Program closed, goodbye!")
    exit()

def show_client_info(client):
    print(f"Client Name: {client.first_name} {client.last_name}")
    print(f"Phone Number: {client.phone_number}")

def list_clients():
    clients = Client.get_all()
    print(spacing)
    print("Clients list:")
    for i, client in enumerate(clients, start=1):
        print(f"{i}. {client.first_name} {client.last_name}")
    print(spacing)

def select_client_by_enumerate_number(choice):
    try:
        clients = Client.get_all()
        client = clients[int(choice) - 1]
        print(spacing)
        show_client_info(client)
        print(spacing)
        return client
    except:
        print(f"Error: no client found for {choice}")
        print(spacing)

def update_client(client):
    print("HINT: first name as 'first_name', last name as 'last_name', or phone number as 'phone_number'")
    attribute = input("Enter the client detail to update: ")
    if attribute == "first_name" or attribute == "last_name" or attribute == "phone_number":
        new_value = input("Enter the new name or phone number: ")
        try:  
            setattr(client, attribute, new_value)
            client.update()
            print(spacing)
            print("Succesfully updated!")
            show_client_info(client)
            print(spacing)
        except Exception as exc:
            print(f"Error: ", exc)
            print(spacing)
    else:
        print("Seems you had a typo typing in the client detail to update. Please try again.")
        print(spacing)
        
def delete_client(client):
    print("""
    Are you sure you want to delete this client?
    Enter 'yes' or 'no'""")
    _input = input("> ")
    if _input == "yes":
        client.delete()
        print(f"Client: {client.first_name} {client.last_name} succesfully deleted")
    elif _input == "no":
        print(spacing)
        print("Client NOT deleted")
        show_client_info(client)
        print(spacing)
    else:
        print("Invalid input. Please try again.")
        print(spacing)

def add_client():
    first_name = input("Enter the new client's first name: ")
    last_name = input("Enter the new client's last name: ")
    phone_number = input("Enter the new client's phone number: ")
    try:
        new_client = Client.create(first_name, last_name, phone_number)
        print(spacing)
        print("Client successfully added!")
        show_client_info(new_client)
        print(spacing)
    except Exception as exc:
        print("Error: ", exc)
        print(spacing)

def search_client_by_name():
    client = input("Type in client first and last name: ")
    pass

def list_trailers():
    pass

def search_trailer():
    trailer = input("Type in trailer number: ")
    pass