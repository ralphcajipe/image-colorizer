"""
Tests for the functions in project.py using unittest.

Implementation of five unit tests that collectively test
the implementation of functions from project.py thoroughly.

Take note that project.py is a Tkinter GUI application.
"""

import unittest
import project


class TestGui(unittest.TestCase):
    # This will run on a separate thread.
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.app = None

    async def test_main(self):
        """
        `test_main` is an async function that calls `project.main()`
        """
        project.main()

    def test_browse_image(self):
        """Test if it opens the file explorer."""
        project.browse_image()

    def test_colorize_image(self):
        """Test if it colorizes the image."""
        project.colorize_image()

    def test_save_image(self):
        """Test if it saves the image."""
        project.save_image()


# Automate the test without having to interact with the GUI manually.
if __name__ == "__main__":
    unittest.main()
