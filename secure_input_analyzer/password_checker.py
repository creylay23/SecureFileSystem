import math
import re

class PasswordChecker:
    def __init__(self, dictionary_file="dictionary.txt"):
        self.dictionary = self._load_dictionary(dictionary_file)
        self.common_patterns = [
            "1234567890", "0987654321",
            "abcdefghijklmnopqrstuvwxyz", "zyxwutsrqponmlkjihgfedcba",
            "qwertyuiop", "poiuytrewq",
            "asdfghjkl", "lkjhgfdsa",
            "zxcvbnm", "mnbvcxz"
        ]

    def _load_dictionary(self, dictionary_file):
        try:
            with open(dictionary_file, "r") as f:
                return {line.strip().lower() for line in f}
        except FileNotFoundError:
            return set()

    def analyze(self, password):
        score = 0
        feedback = []

        # 1. Length Score
        length = len(password)
        if length < 8:
            score += 1
            feedback.append("Very short (less than 8 characters)")
        elif length < 12:
            score += 2
            feedback.append("Short (8-11 characters)")
        else:
            score += 4
            feedback.append("Good length (12+ characters)")

        # 2. Character Variety Score
        has_lower = re.search(r"[a-z]", password)
        has_upper = re.search(r"[A-Z]", password)
        has_digit = re.search(r"\d", password)
        has_symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

        variety = sum([1 for check in [has_lower, has_upper, has_digit, has_symbol] if check])
        if variety == 4:
            score += 4
            feedback.append("Excellent character variety")
        elif variety == 3:
            score += 2
            feedback.append("Good character variety")
        else:
            score += 1
            feedback.append("Low character variety (use a mix of letters, numbers, and symbols)")

        # 3. Entropy-based score contribution (bonus points)
        charset_size = 0
        if has_lower: charset_size += 26
        if has_upper: charset_size += 26
        if has_digit: charset_size += 10
        if has_symbol: charset_size += 32  # Approximate

        if charset_size > 0:
            entropy = length * math.log2(charset_size)
            if entropy > 100:
                score += 2
            elif entropy > 60:
                score += 1

        # 4. Deductions for weaknesses
        # Dictionary word check
        if any(word in password.lower() for word in self.dictionary if len(word) > 3):
            score = max(1, score - 4)
            feedback.append("Contains a common dictionary word")

        # Pattern check
        for pattern in self.common_patterns:
            if pattern in password.lower():
                score = max(1, score - 3)
                feedback.append("Contains a common keyboard pattern")
                break

        # Clamp score to 1-10 range
        final_score = max(1, min(10, score))

        return final_score, ", ".join(feedback)

if __name__ == '__main__':
    # Example usage for testing
    checker = PasswordChecker()
    test_passwords = ["password", "Password123", "P@ssw0rd!", "CorrectHorseBatteryStaple123!"]
    for p in test_passwords:
        score, feedback = checker.analyze(p)
        print(f"Password: '{p}'\nScore: {score}/10\nFeedback: {feedback}\n")
