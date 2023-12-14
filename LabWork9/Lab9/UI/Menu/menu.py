"""
Module for the Menu class.
"""
import logging

class MenuItem:
    """
    Represents an item in the menu.
    """
    def __init__(self, label, action):
        """
        Initialize a MenuItem.
        Parameters:
        - label (str): The label for the menu item.
        - action (callable): The function to be executed when the menu item is selected.
        """
        self.label = label
        self.action = action

class Menu:
    """
    Represents a menu.
    """
    def __init__(self):
        """
        Initialize a Menu.

        Parameters:
        - log_file_path (str): The path to the log file. Default is 'menu.log'.
        """
        self.menu_items = []



    def add_item(self, menu_item):
        """
        Add a menu item to the menu.

        Parameters:
        - menu_item (MenuItem): The menu item to be added.
        """
        self.menu_items.append(menu_item)

    def display(self):
        """
        Display the menu.
        """
        for index, item in enumerate(self.menu_items, start=1):
            print(f"{index}. {item.label}")

    def get_length(self):
        """
        Get the length of the menu.
        Returns:
        - int: The length of the menu.
        """
        return len(self.menu_items) + 1
