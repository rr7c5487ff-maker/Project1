"""
has logic for storing scores, calculating the best score,
and determining letter grades.
"""

from typing import List, Tuple


class GradeCalculator:
    def __init__(self):
        """Initialize an empty score list."""
        self.scores: List[int] = []

    def add_score(self, score: int) -> None:
        """Add a validated score to the list."""
        self.scores.append(score)

    def clear_scores(self) -> None:
        """Remove all stored scores."""
        self.scores.clear()

    def calculate_best(self) -> int:
        """
        Returns the highest score in the list.
        Raises ValueError if list is empty.
        """
        if not self.scores:
            raise ValueError("No scores available to calculate best score.")
        return max(self.scores)

    def calculate_average(self) -> float:
        """
        Returns the average score.
        Raises ValueError if list is empty.
        """
        if not self.scores:
            raise ValueError("No scores available to calculate average.")
        return sum(self.scores) / len(self.scores)

    def letter_grade(self, score: float) -> str:
        """
        Determine the letter grade for a given score.
        Uses the standard grading logic based on the best score.
        """
        best = self.calculate_best()

        if score >= best - 10:
            return "A"
        elif score >= best - 20:
            return "B"
        elif score >= best - 30:
            return "C"
        elif score >= best - 40:
            return "D"
        else:
            return "F"

    def get_all_grades(self) -> List[Tuple[int, str]]:
        """
        Returns a list of tuples: (score, letter grade) for each student.
        Useful for displaying results in the GUI.
        """
        if not self.scores:
            raise ValueError("No scores available to generate grade list.")

        results = []
        for score in self.scores:
            letter = self.letter_grade(score)
            results.append((score, letter))

        return results
