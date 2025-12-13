import csv


class DataStorage:
    """
    CSV file storage.
    """

    def __init__(self, filename: str = "scores.csv") -> None:
        self.filename = filename
        self._initialize_file()

    def _initialize_file(self) -> None:
        """
        Clears file on each run of the application and writes header.
        """
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Final Score", "Grade"])

    def save_record(self, name: str, score: float, grade: str) -> None:
        """
        Saves one student record.
        """
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, score, grade])
