import csv
from typing import List


class DataStorage:
    def __init__(self, filename: str = "scores.csv"):
        self.filename = filename

    def save_scores(self, names: List[str], scores: List[int], grades: List[str]) -> None:
        """
        Saves names, scores, and grades to CSV.
        """
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Score", "Grade"])

            for n, s, g in zip(names, scores, grades):
                writer.writerow([n, s, g])
