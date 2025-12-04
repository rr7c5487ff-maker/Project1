"""
data_storage.py
Handles saving and loading student score data to a CSV file.
"""

import csv
from typing import List


class DataStorage:
    """Handles CSV storage for student scores."""

    FILE_NAME = "scores.csv"

    @staticmethod
    def save_scores(scores: List[float]) -> None:
        """Save list of scores to CSV."""
        with open(DataStorage.FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["score"])
            for s in scores:
                writer.writerow([s])

    @staticmethod
    def load_scores() -> List[float]:
        """Load all scores from CSV file."""
        loaded_scores = []
        try:
            with open(DataStorage.FILE_NAME, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        loaded_scores.append(float(row["score"]))
                    except ValueError:
                        pass
        except FileNotFoundError:
            return []

        return loaded_scores
