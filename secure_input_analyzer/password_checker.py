import re
import math

# Sample dictionary words (expand as needed)
common_words = {"password", "123456", "qwerty", "admin", "letmein", "welcome", "monkey"}

def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"\d", password): charset += 10
    if re.search(r"\W", password): charset += 32
    entropy = len(password) * math.log2(charset) if charset else 0
    return round(entropy, 2)

def check_strength(password):
    entropy = calculate_entropy(password)
    if entropy < 28:
        return "Very Weak", entropy
    elif entropy < 36:
        return "Weak", entropy
    elif entropy < 60:
        return "Moderate", entropy
    else:
        return "Strong", entropy

def estimate_crack_time(entropy):
    guesses = 2 ** entropy
    guesses_per_second = 1e9
    seconds = guesses / guesses_per_second
    if seconds < 60:
        return f"{round(seconds)} seconds"
    elif seconds < 3600:
        return f"{round(seconds / 60)} minutes"
    elif seconds < 86400:
        return f"{round(seconds / 3600)} hours"
    elif seconds < 31536000:
        return f"{round(seconds / 86400)} days"
    else:
        return f"{round(seconds / 31536000)} years"

def is_dictionary_word(password):
    return password.lower() in common_words