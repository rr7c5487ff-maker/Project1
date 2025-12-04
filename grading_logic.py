from typing import List


class GradingLogic:
    """
    Handles grade calculation based on the highest score.
    """

    def get_best_score(self, scores: List[int]) -> int:
        """
        Returns the highest score.
        """
        if not scores:
            return 0
        return max(scores)

    def calculate_letter_grade(self, score: float, best: float) -> str:
        """
        Determines a letter grade based on score and best score.
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

    def get_all_grades(self, scores: List[int]) -> List[str]:
        """
        Returns a list of letter grades for all scores.
        """
        if not scores:
            return []

        best = self.get_best_score(scores)
        return [self.calculate_letter_grade(s, best) for s in scores]
