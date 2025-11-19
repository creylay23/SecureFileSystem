import re

class BruteForceSimulator:
    def estimate_crack_time(self, password, attempts_per_second):
        if not password:
            return "N/A"

        # Determine the character set size
        charset_size = 0
        if re.search(r"[a-z]", password):
            charset_size += 26
        if re.search(r"[A-Z]", password):
            charset_size += 26
        if re.search(r"\d", password):
            charset_size += 10
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            charset_size += 32  # Approximate common symbols

        if charset_size == 0:
            return "N/A"

        # Calculate the number of possible combinations
        combinations = charset_size ** len(password)

        # Calculate the time to crack in seconds
        seconds_to_crack = combinations / attempts_per_second

        # Convert to a human-readable format
        if seconds_to_crack < 60:
            return f"{seconds_to_crack:.2f} seconds"
        elif seconds_to_crack < 3600:
            return f"{seconds_to_crack / 60:.2f} minutes"
        elif seconds_to_crack < 86400:
            return f"{seconds_to_crack / 3600:.2f} hours"
        elif seconds_to_crack < 31536000:
            return f"{seconds_to_crack / 86400:.2f} days"
        else:
            return f"{seconds_to_crack / 31536000:.2f} years"

if __name__ == '__main__':
    simulator = BruteForceSimulator()
    test_password = "Password123!"
    attempts = 1_000_000_000  # 1 billion attempts per second
    time_estimate = simulator.estimate_crack_time(test_password, attempts)
    print(f"Password: '{test_password}'")
    print(f"Attempts per second: {attempts:,}")
    print(f"Estimated time to crack: {time_estimate}")
