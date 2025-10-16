1. Project Awareness & Context 

•  Always read  before starting any new task. 

•  Always check  before coding. If the task isn’t listed, add it with today’s date. 

•  Use consistent naming conventions, file structure, and architecture patterns as defined in . 

•  Never exceed 500 lines per file. Split into modules when needed. 

  

🔐 2. Privacy & Security First 

•  All encryption must happen locally on the user’s device. 

•  No plaintext messages, keys, or sensitive data may be sent or stored on any server. 

•  No telemetry, analytics, or tracking by default. If logging is added, it must be opt-in and anonymized. 

•  Use vetted crypto libraries only (, , , ). No custom cryptography. 

•  Secrets (keys, credentials) must never be committed to GitHub. Store them in environment variables or secure local configs. 

  

🧱 3. Code Structure & Modularity 

•  Separate modules by responsibility: 

•   → Authentication & roles 

•   → Encryption/decryption 

•   → File upload/download 

•   → Secure text messaging 

•   → Logging & compliance 

•   → User interface 

•  Avoid tight coupling: UI should not directly call low-level crypto functions. Use abstractions/interfaces. 

•  Each module must have unit tests covering success, edge, and failure cases. 

  

🧪 4. Testing & Reliability 

•  Every new function or feature must include Pytest unit tests. 

•  Tests must live in  and mirror the main app structure. 

•  Always mock sensitive operations (encryption, DB, file I/O) in tests. 

•  After updating logic, check if existing tests need updates. 

  

⚠️ 5. Fail Safely 

•  On errors (e.g., corrupted ciphertext, dropped connection), fail securely without exposing sensitive data. 

•  Provide clear, user-friendly error messages (e.g., “Could not decrypt message”). 

•  Avoid partial success states (e.g., some data decrypted, some not). 

  

📂 6. Version Control & GitHub Rules 

•  Use Git for version control. 

•  Maintain a  to exclude keys, logs, and build artifacts. 

•  Push to GitHub at the end of each phase milestone (see ). 

•  Tag stable versions (e.g., , , ). 

•  Create backup branches for stable checkpoints (e.g., , ). 

•  Commit messages must reference the feature or task (e.g., ). 

  

📚 7. Documentation & Clarity 

•  Every module must include docstrings and inline comments for non-obvious logic. 

•  Use  comments to explain design decisions. 

•  Update , , and  after each feature. 

•  Provide a Quick Start Guide in  for non-technical users. 

  

🔁 8. Continuous Review & Refactoring 

•  Revisit core modules (auth, crypto, networking) every sprint for cleanup and hardening. 

•  Refactor if design becomes overly complex or no longer fits requirements. 

•  Optimize for maintainability and readability over premature optimization. 

  

⚖️ 9. Ethical Use & Limits 

•  The app is intended for secure healthcare and private communication. 

•  It must not be used to facilitate illegal activity. 

•  If a vulnerability is found, disclose responsibly and fix before public release. 

•  No hidden logging, backdoors, or “trust” overrides. 

  

🧠 10. AI Assistant Behavior Rules 

•  Never assume missing context — ask clarifying questions. 

•  Never hallucinate libraries or functions — only use verified Python packages. 

•  Always confirm file paths and module names exist before referencing. 

•  Never overwrite or delete existing code unless explicitly instructed or listed in . 

•  Always update  after completing or discovering new tasks. 
