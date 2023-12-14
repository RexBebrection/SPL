"""Runner module to demonstrate the usage of the menu system."""
from UI.Menu.menuBuilder import MenuBuilder
def facade():
    """Facilitates user interaction with the menu system."""
    menu_builder = MenuBuilder()
    main_menu = menu_builder.build_menu()

    while True:
        main_menu.display()
        choice = int(input(f"Enter the number of the program to run (1-{main_menu.get_length()-2}): "))

        if 1 <= choice <= main_menu.get_length():
            main_menu.menu_items[choice-1].action()
        else:
            print("Invalid choice. Please enter a number within the specified range.")

if __name__ == "__main__":
    facade()
