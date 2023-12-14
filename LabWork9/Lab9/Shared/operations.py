"""Module for basic mathematical operations."""
import logging
class Operators:
    """Class representing basic mathematical operations."""

    def __init__(self):
        """Initialize the Operators class."""
        # Configure logging system with INFO level.
        logging.basicConfig(level=logging.INFO)
        # Create a logger object for the Operators class.
        self.logger = logging.getLogger(__name__)

    def add(self, x, y):
        """Add two numbers and log the result."""
        result = x + y
        self.logger.info("Addition: %s + %s = %s", x, y, result)
        return result

    def subtract(self, x, y):
        """Subtract one number from another and log the result."""
        result = x - y
        self.logger.info("Subtraction: %s - %s = %s", x, y, result)
        return result

    def multiply(self, x, y):
        """Multiply two numbers and log the result."""
        result = x * y
        self.logger.info("Multiplication: %s * %s = %s", x, y, result)
        return result

    def divide(self, x, y):
        """Divide one number by another, log the result, and handle division by zero."""
        if y != 0:
            result = x / y
            self.logger.info("Division: %s / %s = %s", x, y, result)
            return result
        else:
            self.logger.error("Division by zero is undefined.")
            return None
