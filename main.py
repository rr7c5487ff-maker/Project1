import sys
from PyQt6.QtWidgets import QApplication
from gui_main import GradeGUI
"""
Starts main app.
"""

def main() -> None:
    app = QApplication(sys.argv)
    window = GradeGUI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
