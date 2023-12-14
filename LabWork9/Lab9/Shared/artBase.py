"""Module for ASCII art generation."""

import logging

class ArtBase:
    """Base class for ASCII art generation."""

    def __init__(self, message=' '):
        """Initialize the ArtBase object with a default message."""
        # Initialization of the ArtBase object with the specified message
        self._message = message
        # Field to store the generated ASCII art
        self._ascii_art = None

    def create(self):
        """Abstract method for creating ASCII art."""
        pass

    def save(self, filename):
        """Save the generated ASCII art to a file."""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                self.create()
                file.write(self._ascii_art)
        except Exception as e:
            logging.error("An error occurred in ArtBase.save(): %s", e)
