# lib/helpers.py

from models.client import Client

spacing = "-----------------------------"

def exit_program():
    print("Program closed, goodbye!")
    exit()

def list_clients():
    clients = Client.get_all()
    print("Clients list:")
    print(spacing)
    for i, client in enumerate(clients, start=1):
        print(f"{i}. {client.first_name} {client.last_name}")
    print(spacing)

def select_client_by_enumerate_number():
    number = input("client number> ")
    try:
        client = Client.find_by_id(int(number))
        print(client.first_name) 
    except:
        print(f"Error: no client for number {number}")
        select_client_by_enumerate_number()

