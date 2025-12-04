from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QLineEdit, QHBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox
)
from grading_logic import GradingLogic
from data_storage import DataStorage


class GradeGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Grade Calculator")
        self.setGeometry(400, 200, 600, 400)

        # Logic + storage
        self.logic = GradingLogic()
        self.storage = DataStorage()

        # Data list
        self.names = []
        self.scores = []

        # Layout
        layout = QVBoxLayout()

        # Name input
        name_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Student Name")
        name_layout.addWidget(QLabel("Name:"))
        name_layout.addWidget(self.name_input)
        layout.addLayout(name_layout)

        # Score input
        score_layout = QHBoxLayout()
        self.score_input = QLineEdit()
        self.score_input.setPlaceholderText("Score (0-100)")
        score_layout.addWidget(QLabel("Score:"))
        score_layout.addWidget(self.score_input)
        layout.addLayout(score_layout)

        # Add student button
        add_button = QPushButton("Add Student")
        add_button.clicked.connect(self.add_student)
        layout.addWidget(add_button)

        # Calculate grades button
        calc_button = QPushButton("Calculate Grades")
        calc_button.clicked.connect(self.calculate_grades)
        layout.addWidget(calc_button)

        # Save CSV button
        save_button = QPushButton("Save to CSV")
        save_button.clicked.connect(self.save_csv)
        layout.addWidget(save_button)

        # Table display
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Score", "Grade"])
        layout.addWidget(self.table)

        self.setLayout(layout)

    # ---------------- ACTIONS BELOW ---------------- #

    def add_student(self):
        name = self.name_input.text().strip()
        score_text = self.score_input.text().strip()

        if not name:
            QMessageBox.warning(self, "Error", "Please enter a student name.")
            return

        if not score_text.isdigit():
            QMessageBox.warning(self, "Error", "Score must be a number.")
            return

        score = int(score_text)
        if score < 0 or score > 100:
            QMessageBox.warning(self, "Error", "Score must be between 0 and 100.")
            return

        self.names.append(name)
        self.scores.append(score)

        self.name_input.clear()
        self.score_input.clear()

        QMessageBox.information(self, "Added", f"{name} added.")

    def calculate_grades(self):
        if not self.scores:
            QMessageBox.warning(self, "Error", "No student scores added.")
            return

        grades = self.logic.get_all_grades(self.scores)

        self.table.setRowCount(len(self.scores))

        for i, (name, score, grade) in enumerate(zip(self.names, self.scores, grades)):
            self.table.setItem(i, 0, QTableWidgetItem(name))
            self.table.setItem(i, 1, QTableWidgetItem(str(score)))
            self.table.setItem(i, 2, QTableWidgetItem(grade))

    def save_csv(self):
        if not self.scores:
            QMessageBox.warning(self, "Error", "No data to save.")
            return

        grades = self.logic.get_all_grades(self.scores)
        self.storage.save_scores(self.names, self.scores, grades)

        QMessageBox.information(self, "Saved", "Scores saved to scores.csv")
