from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox
)
from grading_logic import GradingLogic
from data_storage import DataStorage

# USED AI FOR A BIT OF GUI CODE, NOT FOR OTHER FILES
class GradeGUI(QWidget):
    """
    GUI for collecting student scores and finalizing grades.
    """

    def __init__(self) -> None:
        super().__init__()

        self.logic = GradingLogic()
        self.storage = DataStorage()

        self.students: list[dict] = []

        self.score_inputs: list[QLineEdit] = []

        self._setup_ui()

    def _setup_ui(self) -> None:
        self.setWindowTitle("Grade Calculator")
        self.setFixedSize(350, 440)

        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel("Student Name"))
        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_input)

        self.layout.addWidget(QLabel("Number of Scores (1–4)"))
        self.attempts_input = QLineEdit()
        self.attempts_input.textChanged.connect(self.generate_score_inputs)
        self.layout.addWidget(self.attempts_input)

        self.scores_label = QLabel("Scores")
        self.layout.addWidget(self.scores_label)

        self.add_button = QPushButton("Add to Score Sheet")
        self.add_button.clicked.connect(self.add_student)

        self.finalize_button = QPushButton("Finalize Grades")
        self.finalize_button.clicked.connect(self.finalize_grades)

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.finalize_button)

        self.setLayout(self.layout)

    def generate_score_inputs(self) -> None:
        """
        Creates score input boxes based on number entered (1–4 only).
        """
        for box in self.score_inputs:
            self.layout.removeWidget(box)
            box.deleteLater()

        self.score_inputs.clear()

        try:
            count = int(self.attempts_input.text())

            if count < 1 or count > 4:
                return

            for i in range(count):
                box = QLineEdit()
                box.setPlaceholderText(f"Score {i + 1}")
                self.score_inputs.append(box)
                self.layout.insertWidget(self.layout.count() - 2, box)

        except ValueError:
            pass

    def add_student(self) -> None:
        """
        Adds student data to memory without grading yet.
        """
        name = self.name_input.text().strip()

        if not name:
            QMessageBox.warning(self, "Error", "Please enter a student name.")
            return

        if not self.score_inputs:
            QMessageBox.warning(
                self, "Error", "Please enter a number of scores between 1 and 4."
            )
            return

        try:
            scores = [float(box.text()) for box in self.score_inputs]
            final_score = max(scores)

            self.students.append({
                "name": name,
                "score": final_score
            })

            QMessageBox.information(self, "Added", f"{name} added.")

            self.name_input.clear()
            self.attempts_input.clear()
            self.generate_score_inputs()

        except ValueError:
            QMessageBox.warning(self, "Error", "Scores must be numeric values.")

    def finalize_grades(self) -> None:
        """
        Calculates grades AFTER all students are entered.
        """
        if not self.students:
            QMessageBox.warning(self, "Error", "No students entered.")
            return

        scores = [student["score"] for student in self.students]
        best = self.logic.get_best_score(scores)

        for student in self.students:
            grade = self.logic.calculate_letter_grade(student["score"], best)
            self.storage.save_record(student["name"], student["score"], grade)

        QMessageBox.information(self, "Done", "Grades finalized and saved.")
        self.students.clear()
