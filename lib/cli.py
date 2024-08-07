# lib/cli.py

from helpers import (
    exit_program,
    list_clients,
    select_client_by_enumerate_number,
    search_client_by_name
)


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "exit" or choice == "e":
            exit_program()
        elif choice == "view" or choice == "v":
            list_clients()
            view_all_clients_menu()
        elif choice == "select" or choice == "s":
            search_client_by_name()
        else:
            print("Invalid choice")


def main_menu():
    print("Program started, please select an option:")
    print("Type 'exit' or 'e' to exit the program")
    print("Type 'view' or 'v' to view all clients")
    print("Type 'select' or 's' to search for a client")

def view_all_clients_menu():
    print("Please select a client by corresponding number")
    select_client_by_enumerate_number()



if __name__ == "__main__":
    main()
