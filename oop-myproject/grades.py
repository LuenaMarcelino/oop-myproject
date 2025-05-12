class Grades:
    def __init__(self, grades):
        self.subject_scores = {}
        self.subject_scores = {}

    def add_score(self, subject: str, score: float) -> None:
        self.subject_scores[subject] = score

    def calculate_average(self) -> float:
        if not self.subject_scores:
            return 0.0
        return sum(self.subject_scores.values()) / len(self.subject_scores)

    def check_pass_fail(self, passing_score: float = 10.0) -> bool:
        return self.calculate_average() >= passing_score

    def __str__(self) -> str:
        subjects = "\n  ".join([f"{subj}: {score}" for subj, score in self.subject_scores.items()])
        return (f"Subjects & Scores:\n  {subjects}\n"
                f"Average: {self.calculate_average():.2f}, "
                f"Pass: {'Yes' if self.check_pass_fail() else 'No'}")