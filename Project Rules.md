# Project Rules & Guidelines

These rules are set to keep the project secure, manageable, and easy to understand for both technical and non-technical contributors.

---

## 🎯 Purpose

This document lays out the **principles, policies, and constraints** we adhere to while building our secure messaging app. Everyone working (now or in the future) should follow them.

---

## 1. Privacy First

- All encryption happens **on the user’s device**. This project shall never send or store plaintext messages or keys on any server.  
- No telemetry, analytics, or usage tracking by default. If we do ever add any reporting/logging, it must be opt-in and anonymized.  
- We minimize metadata: only the bare minimum needed to make messaging work (e.g. delivery status), and only encrypted or obfuscated where possible.

---

## 2. Simplicity & Transparency

- We avoid hidden features: if a user loses their device or uninstalls the app, *all data is lost*. That is clearly documented.  
- No accounts, no logins, no registration. The app must be usable out-of-the-box.  
- All UI text should be in plain language. Avoid technical jargon in the user experience.

---

## 3. Security Discipline

- Use well-known, vetted crypto libraries (no custom cryptography).  
- Every security-sensitive change (e.g. changes in key handling, encryption modes, storage) must be code-reviewed by both team members.  
- Because this is a small team, pair-review any critical code (crypto, networking).  
- Secrets (private keys, etc.) must never be committed to the repository or exposed in logs or error messages.

---

## 4. Clear Ownership

- Each feature or task must have a clear owner (Person A or Person B).  
- If someone changes a component owned by the other (for example, UI touches crypto data), they must communicate and coordinate first.  
- Document in commit messages which feature/task the change is for.

---

## 5. Modular & Testable Components

- Crypto, networking, storage, and UI must be separated into modules.  
- Each module should have unit tests. For crypto and networking especially, include test cases covering correct behavior and error/failure cases.  
- Avoid tight coupling: e.g., UI should not directly invoke low-level encryption calls; instead use interfaces/abstractions.

---

## 6. Fail Safely

- Whenever an error or unexpected input occurs (e.g. corrupted ciphertext, connection drop), fail in a secure way: do not crash exposing private data.  
- Provide clear error messages to the user (in simple terms: “Failed to send message,” “Couldn’t decrypt message,” etc.).  
- Avoid partial success states where some data is plaintext while other parts are encrypted.

---

## 7. Version Control & Secrets

- Use Git for version control.  
- Add a `.gitignore` with rules to exclude keys, debug logs, build artifacts.  
- Any secret keys (for testing only) must be stored in environment variables or a secure local config not tracked by Git.

---

## 8. Documentation & User Clarity

- Every module must have a README or comments explaining its purpose, inputs, and outputs.  
- The main `README.md` for the project must include a clear **“What the app does (and what it doesn’t)”** section.  
- Provide a **Quick Start Guide** so a non-technical user can install and start using without reading code.

---

## 9. Continuous Review & Refactoring

- Every few sprints, revisit core modules (crypto, networking) for code cleanup, security hardening, and performance improvements.  
- If a part of the design no longer fits or is overly complex, be willing to refactor even if it’s worked so far.

---

## 10. Ethical Use & Limits

- The app’s intended use is private, peer-to-peer messaging. It should not be used to facilitate illegal activity.  
- If you find a security flaw or vulnerability, **do not publish it publicly** before responsibly disclosing it to the team and planning a fix.  
- Respect user privacy. Do not add hidden logging or backdoors, even “for trust”.

---

_By following these rules, we maintain trust, security, clarity, and consistency as we build._  
