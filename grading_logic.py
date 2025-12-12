class GradingLogic:
    """
    Handles grade calculations based on the highest score.
    """

    def get_best_score(self, scores: list[float]) -> float:
        """
        Returns the highest score from a list.
        """
        return max(scores) if scores else 0.0

    def calculate_letter_grade(self, score: float, best: float) -> str:
        """
        Determines letter grade relative to best score.
        """
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
