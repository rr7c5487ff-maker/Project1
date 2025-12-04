"""
main.py
Entry point of the application.
"""

import sys
from PyQt6.QtWidgets import QApplication
from gui_main import GradeApp


def main() -> None:
    """Start the PyQt application."""
    app = QApplication(sys.argv)
    window = GradeApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
