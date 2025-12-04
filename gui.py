"""
gui_main.py
PyQt6 User Interface for the grading application.
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QLineEdit, QListWidget, QMessageBox
)
from PyQt6.QtCore import Qt
from grading_logic import GradeCalculator
from data_storage import DataStorage
import styles


class GradeApp(QWidget):
    """Main window for grade calculation interface."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Grading System")
        self.setStyleSheet(f"background-color: {styles.BACKGROUND};")

        self.scores: list[float] = []

        self.layout = QVBoxLayout()

        # Input Label
        self.label = QLabel("Enter a score:")
        self.layout.addWidget(self.label)

        # Textbox
        self.score_input = QLineEdit()
        self.score_input.setStyleSheet(f"background-color: {styles.TEXTBOX};")
        self.layout.addWidget(self.score_input)

        # Add Button
        self.add_button = QPushButton("Add Score")
        self.add_button.setStyleSheet(f"background-color: {styles.BUTTON}; color: white;")
        self.add_button.clicked.connect(self.add_score)
        self.layout.addWidget(self.add_button)

        # Score Display
        self.score_list = QListWidget()
        self.layout.addWidget(self.score_list)

        # Calculate Grades Button
        self.calc_button = QPushButton("Calculate Grades")
        self.calc_button.setStyleSheet(f"background-color: {styles.BUTTON}; color: white;")
        self.calc_button.clicked.connect(self.calculate_grades)
        self.layout.addWidget(self.calc_button)

        self.setLayout(self.layout)

    def add_score(self) -> None:
        """Validate and add a score."""
        text = self.score_input.text().strip()

        if not text.isdigit():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")
            return

        score = float(text)
        self.scores.append(score)
        self.score_list.addItem(f"Score: {score}")

        self.score_input.clear()
        DataStorage.save_scores(self.scores)

    def calculate_grades(self) -> None:
        """Calculate grades and show result."""
        if not self.scores:
            QMessageBox.warning(self, "Error", "No scores available.")
            return

        grades = GradeCalculator.get_all_grades(self.scores)

        msg = "Grades:\n\n"
        for i, g in enumerate(grades, start=1):
            msg += f"Student {i}: {g}\n"

        QMessageBox.information(self, "Grade Results", msg)
