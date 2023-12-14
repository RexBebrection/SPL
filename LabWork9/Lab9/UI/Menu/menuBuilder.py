"""
Menu builder module.
"""
import os
import logging
from colorama import Fore
from UI.Menu.menu import Menu, MenuItem
from Labs.Classes.Lab1.Calculator import Calculate
from Labs.Classes.Lab2.ClassBasedCalc import ClassBasedCalculator
from Labs.Classes.Lab3.ArtConsole import ArtConsole
from Labs.Classes.Lab4.CustomArtConsole import CustomArtConsole
from Labs.Classes.Lab5.CubeDrawer import CubeDrawer
from Labs.Classes.Lab6.Utest import TestClassBasedCalculator
from Labs.Classes.Lab7.DogAPI import DogAPI, DisplayDogApi, ConsoleInterface
from Labs.Classes.Lab8.csv_visual import DataVisualizer

class MenuBuilder:
    """
    Class to build menus and handle user choices.
    """

    log_dir = os.path.join('Data', 'Log')
    log_file_path = os.path.join(log_dir, 'usage.log')

    # Check for the existence of the directory and create it if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Initialize logger
    logging.basicConfig(filename=log_file_path, level=logging.INFO)
    logger = logging.getLogger(__name__)

    @staticmethod
    def build_menu():
        """
        Build the main menu.

        Returns:
        - Menu: The main menu.
        """
        main_menu = Menu()

        main_menu.add_item(MenuItem("Run Lab1 - Calculator", MenuBuilder.run_lab1_calculator))
        main_menu.add_item(MenuItem("Run Lab2 - ClassBased Calculator", MenuBuilder.run_lab2_calculator))
        main_menu.add_item(MenuItem("Run Lab3 - ASCII Art Generator", MenuBuilder.run_ascii_art_generator))
        main_menu.add_item(MenuItem("Run Lab4 - Custom ASCII Art Generator", MenuBuilder.run_custom_ascii_art_generator))
        main_menu.add_item(MenuItem("Run Lab5 - 3D Cube Drawer", MenuBuilder.run_cube_drawer))
        main_menu.add_item(MenuItem("Run Lab6 - ClassBased Calculator Tests", MenuBuilder.run_class_based_calculator_tests))
        main_menu.add_item(MenuItem("Run Lab7 - DogAPI", MenuBuilder.run_lab7_dogapi))
        main_menu.add_item(MenuItem("Run Lab8 - CSV Visualizer", MenuBuilder.run_lab8_csv_visual))
        main_menu.add_item(MenuItem("Exit", MenuBuilder.exit_action))

        return main_menu

    @staticmethod
    def run_lab1_calculator():
        """
        Run Lab1 - Calculator.
        """
        MenuBuilder.logger.info("User selected: Run Lab1 - Calculator")
        calculate = Calculate()
        calculate.run()

    @staticmethod
    def run_lab2_calculator():
        """
        Run Lab2 - ClassBased Calculator.
        """
        MenuBuilder.logger.info("User selected: Run Lab2 - ClassBased Calculator")
        class_based_calculator = ClassBasedCalculator()
        class_based_calculator.run_class_based_calculator()

    @staticmethod
    def run_ascii_art_generator():
        """
        Run Lab3 - ASCII Art Generator.
        """
        MenuBuilder.logger.info("User selected: Run Lab3 - ASCII Art Generator")
        art_console = ArtConsole()
        art_console.run()

    @staticmethod
    def run_custom_ascii_art_generator():
        """
        Run Lab4 - Custom ASCII Art Generator.
        """
        MenuBuilder.logger.info("User selected: Run Lab4 - Custom ASCII Art Generator")
        custom_art_console = CustomArtConsole()
        custom_art_console.run()

    @staticmethod
    def run_cube_drawer():
        """
        Run Lab5 - 3D Cube Drawer.
        """
        MenuBuilder.logger.info("User selected: Run Lab5 - 3D Cube Drawer")
        cube_drawer = CubeDrawer()
        cube_drawer.run_cube_drawer()

    @staticmethod
    def run_class_based_calculator_tests():
        """
        Run Lab6 - ClassBased Calculator Tests.
        """
        MenuBuilder.logger.info("User selected: Run Lab6 - ClassBased Calculator Tests")
        test_runner = TestClassBasedCalculator()
        test_runner.run_tests()

    @staticmethod
    def run_lab7_dogapi():
        """
        Run Lab7 - DogAPI.
        """
        MenuBuilder.logger.info("User selected: Run Lab7 - DogAPI")
        api_key = "live_erHxdDaDlKKkhVAn0IpEIPT9trh9HzJx"
        dog_api = DogAPI(api_key)
        interface = ConsoleInterface()

        breeds = DisplayDogApi.get_all_breeds()

        color = MenuBuilder.choose_color()
        format_choice = MenuBuilder.choose_display_format()

        if format_choice == "1":
            interface.display_table(breeds, color)
        elif format_choice == "2":
            interface.display_list(breeds, color)

        save_choice = input("Do you want to save the data? (y/n): ")
        if save_choice.lower() == 'y':
            save_format = input("Choose a save format:\n1. JSON\n2. CSV\n3. TXT\nEnter the number of the save format: ")
            save_filename = input("Enter the filename: ")
            if save_format == "1":
                interface.save_to_json(breeds, save_filename)
            elif save_format == "2":
                interface.save_to_csv(breeds, save_filename)
            elif save_format == "3":
                interface.save_to_txt(breeds, save_filename)
            else:
                print("Invalid save format. Please enter 1, 2, or 3.")

    @staticmethod
    def run_lab8_csv_visual():
        """
        Run Lab8 - CSV Visualizer.
        """
        MenuBuilder.logger.info("User selected: Run Lab8 - CSV Visualizer")
        csv_file_path = 'D:/Labs/Спец. мови програмування/Lab9/Data/Lab8/mock_data.csv'
        output_folder = 'D:/Labs/Спец. мови програмування/Lab9/Data/Lab8'  # Updated path for storage
        output_path = 'D:/Labs/Спец. мови програмування/Lab9/Data/Lab8'  # Path for saving graphs

        data_visualizer = DataVisualizer(csv_file_path, output_folder, output_path)
        data_visualizer.explore_data()

        user_choice = input(
            "1. Кругова діаграма \n2. Діаграма розсіювання \n3. Стовпцева діаграма \n4. Вивести всі діаграми \nВведіть номер діаграми (1-4) або 'x' для виходу: ")

        if user_choice.lower() == 'x':
            return

        data_visualizer.visualize_data(user_choice)

    @staticmethod
    def exit_action():
        """
        Exit the program.
        """
        MenuBuilder.logger.info("User selected: Exit")
        print("Exiting the program.")
        exit()

    @staticmethod
    def choose_display_format():
        """
        Choose a display format.

        Returns:
        - str: The chosen display format.
        """
        while True:
            print("Choose a display format:")
            print("1. Table")
            print("2. List")
            format_choice = input("Enter the number of the display format: ")

            if format_choice in ("1", "2"):
                return format_choice
            else:
                print("Invalid display format. Please enter 1 or 2.")

    @staticmethod
    def choose_color():
        """
        Choose a color.

        Returns:
        - str: The chosen color.
        """
        while True:
            print("Choose a color:")
            print("1. Red")
            print("2. Green")
            print("3. Yellow")
            color_choice = input("Enter the number of the color: ")

            if color_choice == "1":
                return Fore.RED
            elif color_choice == "2":
                return Fore.GREEN
            elif color_choice == "3":
                return Fore.YELLOW
            else:
                print("Invalid color choice. Please enter 1, 2, or 3.")

    @staticmethod
    def get_user_choice(options):
        """
        Get the user's choice from a list of options.

        Parameters:
        - options (list): The list of options.

        Returns:
        - int: The user's choice.
        """
        print("\n".join(f"{i + 1}. {option}" for i, option in enumerate(options)))
        while True:
            try:
                choice = int(input("Enter the number of the program to run (1-{}): ".format(len(options))))
                if 1 <= choice <= len(options):
                    return choice
                else:
                    print("Invalid choice. Please enter a number within the specified range.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
