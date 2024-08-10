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
    first_name = input("Enter the new first name: ")
    client.first_name = first_name
    last_name = input("Enter the new last name: ")
    client.last_name = last_name
    phone_number = input("Enter the new phone number: ")
    client.phone_number = phone_number
    try:
        client.update()
        print("Succesfully updated!")
        show_client_info(client)
    except Exception as exc:
        print("Error: ", exc)
        print(spacing)

def delete_client(client):
    print("""
    Are you sure you want to delete this client?
    Enter 'yes' or 'no'""")
    _input = input("> ")
    if _input == "yes":
        client.delete()
    elif _input == "no":
        print("Client NOT deleted")
        show_client_info(client)
    else:
        print("Invalid input")

    

def search_client_by_name():
    client = input("Type in client first and last name: ")
    pass

def list_trailers():
    pass

def search_trailer():
    trailer = input("Type in trailer number: ")
    pass