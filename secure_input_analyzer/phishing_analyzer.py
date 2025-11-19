import re

class PhishingAnalyzer:
    def analyze_email(self, email_content):
        red_flags = []

        # 1. Sense of urgency
        urgent_keywords = [
            "urgent", "immediate", "action required", "account suspended",
            "security alert", "unusual sign-in", "verify your account"
        ]
        for keyword in urgent_keywords:
            if re.search(keyword, email_content, re.IGNORECASE):
                red_flags.append("Urgent language detected.")
                break

        # 2. Suspicious links (basic check for non-standard domains)
        links = re.findall(r"https?://[^\s/$.?#].[^\s]*", email_content)
        for link in links:
            if not any(domain in link for domain in [".com", ".org", ".net", ".gov", ".edu"]):
                red_flags.append(f"Suspicious link found: {link}")

        # 3. Generic greetings
        generic_greetings = ["dear user", "dear customer", "dear account holder"]
        for greeting in generic_greetings:
            if re.search(greeting, email_content, re.IGNORECASE):
                red_flags.append("Generic greeting used.")
                break

        # 4. Mismatched sender information
        from_header = re.search(r"From:.*<(.+)>", email_content)
        return_path_header = re.search(r"Return-Path:.*<(.+)>", email_content)

        if from_header and return_path_header and from_header.group(1) != return_path_header.group(1):
            red_flags.append("Mismatched 'From' and 'Return-Path' headers.")

        # 5. Requests for sensitive information
        sensitive_info_keywords = ["password", "credit card", "social security number", "ssn"]
        for keyword in sensitive_info_keywords:
            if re.search(keyword, email_content, re.IGNORECASE):
                red_flags.append("Request for sensitive information.")
                break

        if not red_flags:
            return "No obvious red flags found."

        return "\n".join(f"- {flag}" for flag in red_flags)

if __name__ == '__main__':
    analyzer = PhishingAnalyzer()
    sample_email = """
    From: "Trusted Bank" <support@trustedbank.com>
    Return-Path: <suspicious-address@phishing.com>
    Subject: Urgent: Action Required on Your Account

    Dear User,

    We have detected an unusual sign-in to your account. Please verify your account details immediately to avoid suspension. Click here: http://security-update-totaly-not-a-scam.biz/login

    You will be asked to provide your password and credit card information.

    Thanks,
    The Security Team
    """
    analysis_result = analyzer.analyze_email(sample_email)
    print("--- Phishing Analysis ---")
    print(analysis_result)
