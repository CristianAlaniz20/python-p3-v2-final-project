# lib/cli.py

from helpers import (
    create_db_tables,
    invalid_input_message,
    add_spacing,
    exit_program,
    list_clients,
    select_client_by_number,
    update_client,
    delete_client,
    add_client,
    search_for_client,
    search_for_trailer,
    delete_trailer,
    list_trailers,
    add_trailer,
    is_empty,
    print_list,
    filter_trailers_by_client,
    check_for_exisiting_client,
    change_client_from_trailer,
    remove_client_from_trailer,
    create_trailer_with_client,
    show_client_info
)

def main():
    create_db_tables()
    while True:
        add_spacing()
        main_menu_options()
        choice = input("> ")
        if choice == "e":
            exit_program()
        elif choice == "vc":
            view_all_clients_menu()
        elif choice == "sc":
            search_client_menu()
        elif choice == "vt":
            list_trailers_menu()
        elif choice == "st":
            search_for_trailer_menu()
        else:
            invalid_input_message()

def view_all_clients_menu(filtered_clients=None):
    list_clients(filtered_clients)
    while True:
        add_spacing()
        if filtered_clients:
            search_client_options()
        else:
            view_all_clients_options()
        choice = input("> ")
        if choice == "p":
            main()
        elif choice == "e":
            exit_program()
        elif choice == 'a':
            add_client()
            list_clients(filtered_clients)
        elif (client := select_client_by_number(choice)):
            client_menu(client)
        else:
            invalid_input_message()
    
def search_client_menu():
    (client_search_results := search_for_client())
    if client_search_results:
        list_clients(client_search_results)
        while True:
            add_spacing()
            search_client_options()
            choice = input("> ")
            if choice == "p":
                main()
            elif choice == "e":
                exit_program()
            elif (client := select_client_by_number(choice)):
                client_menu(client, client_search_results)
            else:
                invalid_input_message()

def client_menu(client, filtered_clients=None):
    while True:
        add_spacing()
        client_options()
        choice = input("> ")
        if choice == "p":
            view_all_clients_menu(filtered_clients)
        elif choice == "e":
            exit_program()
        elif choice == "u":
            update_client(client)
        elif choice == "d":
            delete_client(client)
            main()
        elif choice == "v":
            filtered_trailer_list = filter_trailers_by_client(client)
            list_trailers_of_client_menu(filtered_trailer_list, client)
        else:
            invalid_input_message()

def search_for_trailer_verification_menu():
    while True:
        add_spacing()
        search_for_trailer_verification_options()
        choice = input("> ")
        if choice == "p":
            main()
        elif choice == "s":
            search_for_trailer_menu()
        else:
            invalid_input_message()

def search_for_trailer_menu():
    (searched_trailer := search_for_trailer())
    if searched_trailer:
        while True:
            add_spacing()
            search_for_trailer_options()
            choice = input("> ")
            if choice == "p":
                main()
            elif choice == "e":
                exit_program()
            elif choice == "u":
                update_trailer_client_menu(searched_trailer)
            elif choice == "d":
                delete_trailer(searched_trailer)
                main()
            else:
                invalid_input_message()

def list_trailers_menu():
    while True:
        add_spacing()
        trailer_list = list_trailers()
        if is_empty(trailer_list):
            empty_trailer_list_menu()
        else:
            list_trailers_options()
            choice = input("> ")
            if choice == "p":
                main()
            elif choice == "e":
                exit_program()
            elif choice == "all":
                print_list(trailer_list)
                search_for_trailer_verification_menu()
            elif choice == "rented":
                is_rented = lambda trailer: trailer.client_renting_trailer is not None
                filtered_trailer_list = list_trailers(is_rented)
                if is_empty(filtered_trailer_list):
                    print("There are no trailers currently being rented")
                    list_trailers_menu()
                else:
                    print_list(filtered_trailer_list)
                    search_for_trailer_verification_menu()
            elif choice == "available":
                is_available = lambda trailer: trailer.available is not False
                filtered_trailer_list = list_trailers(is_available)
                if is_empty(filtered_trailer_list):
                    print("There no trailers currently available")
                    list_trailers_menu()
                else:
                    print_list(filtered_trailer_list)
                    search_for_trailer_verification_menu()
            elif choice == "add":
                add_trailer()
            else:
                invalid_input_message()

def empty_trailer_list_menu():
    while True:
        add_spacing()
        empty_trailer_list_options()
        choice = input("> ")
        if choice == "p":
            main()
        elif choice == "a":
            add_trailer()
            main()
        else:
            invalid_input_message()

def update_trailer_client_menu(trailer):
    while True:
        update_trailer_client_options()
        choice = input("> ")
        if choice == "remove":
            remove_client_from_trailer(trailer)
            main()
        elif choice == "change":
            change_client_from_trailer(trailer)
            main()
        else:
            invalid_input_message()

def list_trailers_of_client_menu(trailer_list, client):
    if is_empty(trailer_list):
        print(f"{client.first_name} {client.last_name} is currently not renting any trailers")
        add_trailer_to_client_menu(client)
    else:
        print_list(trailer_list)

def add_trailer_to_client_menu(client):
    while True:
        add_spacing()
        add_trailer_to_client_options()
        choice = input("> ")
        if choice == "p":
            show_client_info(client)
            client_menu(client)
        elif choice == "a":
            create_trailer_with_client(client)
            client_menu(client)
        else:
            invalid_input_message()


def main_menu_options():
    print("""
    Welcome, please select an option:
    Enter 'e' to exit the program
    Enter 'vc' to view list of clients
    Enter 'sc' to search for a client
    Enter 'vt' to view list of trailers
    Enter 'st' to search for a trailer
    """)

def view_all_clients_options():
    print("""
    Enter 'p' to go to the previous menu
    Enter 'e' to exit the program
    Enter 'a' to add a client
    Or select a client by entering their corresponding number
    """)

def search_client_options():
    print("""
    Enter 'p' to go to the previous menu
    Enter 'e' to exit the program
    Or select a client by entering their corresponding number
    """)

def client_options():
    print("""
    Enter 'p' to go to the previous menu
    Enter 'e' to exit the program
    Enter 'u' to update client details
    Enter 'd' to delete this client
    Enter 'v' to view all the trailers this client has rented
    """)

def search_for_trailer_verification_options():
    print("""
    Enter 'p' to go to the previous menu
    Enter 's' if you want to select a trailer
    """)

def search_for_trailer_options():
    print("""
    Enter 'p' to go to the previous menu
    Enter 'e' to exit the program
    Enter 'u' to update client renting this trailer
    Enter 'd' to delete this trailer
    """)

def list_trailers_options():
    print("""
    Enter 'p' to go to the previous menu
    Enter 'e' to exit the program
    Enter 'all' to view a list of all trailers
    Enter 'rented' to view a list of trailers being rented
    Enter 'available' to view a list of trailers available
    Enter 'add' to add a trailer
    """)

def empty_trailer_list_options():
    print("""
    HINT: It appears there are no trailers. Please select an option:
    Enter 'p' to go to the previous menu
    Enter 'a' to add a trailer
    """)

def update_trailer_client_options():
    print("""
    Enter 'change' to change trailer client to another client
    Enter 'remove' to remove any client renting this trailer
    """)

def add_trailer_to_client_options():
    print("""
    Enter 'p' to go to the previous menu
    Enter 'a' to create a new trailer with this client assigned to it
    """)

if __name__ == "__main__":
    main()
