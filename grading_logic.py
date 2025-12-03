"""Business logic for calculating grades based on scores and best score."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class GradeCalculator:
    """
    Class that stores student scores and calculates letter grades.

    The grading scheme is:
    - A: score >= best - 10
    - B: score >= best - 20
    - C: score >= best - 30
    - D: score >= best - 40
    - F: otherwise
    """
