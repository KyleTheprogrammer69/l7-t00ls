import subprocess
import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def execute_file(file_path):
    try:
        subprocess.run(["python", file_path], check=True)
    except FileNotFoundError:
        print("File not found.")

def print_logo():
    logo = """
 █████       ██████████    ███████████                   ████         
░░███       ░███░░░░███   ░█░░░███░░░█                  ░░███         
 ░███       ░░░    ███    ░   ░███  ░   ██████   ██████  ░███   █████ 
 ░███             ███         ░███     ███░░███ ███░░███ ░███  ███░░  
 ░███            ███          ░███    ░███ ░███░███ ░███ ░███ ░░█████ 
 ░███      █    ███           ░███    ░███ ░███░███ ░███ ░███  ░░░░███
 ███████████   ███            █████   ░░██████ ░░██████  █████ ██████ 
░░░░░░░░░░░   ░░░            ░░░░░     ░░░░░░   ░░░░░░  ░░░░░ ░░░░░░   created by dscord5721
                                                                      
                                                                      
                                                                      
"""

    print(logo)

def draw_menu():
    while True:
        clear_screen()
        print_logo()
        print("1. HTTP GET Request")
        print("2. HTTP POST Request")
        print("3. HTTP bypass")
        print("4. Kill (IP)")
        print("5. Snake game :D")
        print("0. Quit")

        option = input("Select an option (0-4): ")

        if option == '0':
            return
        elif option == '1':
            file_name = "Https_get.py"
        elif option == '2':
            file_name = "Http-POST.py"
        elif option == '3':
            file_name = "Http-bypass.py"
        elif option == '4':
            file_name = "Kill.py"
        elif option == '5':
            file_name = "snake.py"
        else:
            print("Invalid option. Please select a valid option (0-5).")
            input("Press Enter to continue...")
            continue

        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, file_name)
        execute_file(file_path)

        input("Press Enter to continue...")

        clear_screen()

draw_menu()
