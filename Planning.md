Phase 1: Planning & Setup 

• 	Always read  before starting any task. 
• 	Check  before coding. Add missing tasks with today’s date. 
• 	Use consistent naming conventions and file structure. 
• 	Never exceed 500 lines per file. Split into modules as needed. 

📤 Push to GitHub when: 

• 	Initial folder structure is created 
• 	, , and  are drafted 
• 	Project roles and architecture are defined 

🟨 Phase 2: Authentication & Role Management 
• 	Use  or  for password hashing. 
• 	Implement role-based access control (Doctor, Nurse, Admin). 
• 	Store credentials securely in SQLite using parameterized queries. 

📤 Push to GitHub when: 
• 	Login form and role logic are implemented 
• 	Password hashing is functional 
• 	Role-based access is enforced in backend and GUI 
• 	Basic unit tests for login and access control are written 


🟧 Phase 3: Encryption & File Handling 

• 	Use AES-256 for encryption of files and messages. 
• 	Generate secure keys per session or user. 
• 	Add SHA-256 hash for file integrity checks. 
• 	Validate file size and type before uploading. 

📤 Push to GitHub when: 

• 	Encryption and decryption functions are working 
• 	File upload/download logic is in place 
• 	Integrity checks are implemented 
• 	Encryption tests are added 


🟩 Phase 4: Messaging System 

• 	Encrypt messages before storing or sending. 
• 	Display message history per user. 
• 	Limit message length and sanitize input. 


📤 Push to GitHub when: 

• 	Messaging module is functional 
• 	GUI displays messages with timestamps 
• 	Message encryption and retrieval are tested 
• 	Input validation is added 


🟫 Phase 5: GUI Development 

• 	Use Tkinter or PyQt5 for the GUI. 
• 	Implement error handling and alerts. 
• 	Ensure GUI responsiveness and usability. 

📤 Push to GitHub when: 

• 	GUI layout includes login, file transfer, messaging, and logs 
• 	All buttons and forms are wired to backend logic 
• 	GUI tested on multiple screen sizes 
• 	Visual polish and error handling are added 
 

🟪 Phase 6: Audit Logging & Compliance 

• 	Log all user actions with timestamps. 
• 	Store logs in SQLite and make them tamper-resistant. 
• 	Add log filtering by user, date, and action. 

📤 Push to GitHub when: 

• 	Audit logging is implemented across modules 
• 	Logs are stored and retrievable 
• 	Compliance notes are drafted in  
• 	GUI includes log viewer 


🟥 Phase 7: Testing & Documentation 

• 	Write Pytest unit tests for every module. 
• 	Mock sensitive operations during testing. 
• 	Update , , and  after each feature. 
• 	Comment non-obvious logic with  explanations. 

📤 Push to GitHub when: 

• 	All modules have basic test coverage 
• 	Documentation is updated 
• 	Project is stable enough for internal review or demo 

 
⚫ Phase 8: Final Polish & Deployment 

• 	Run full system tests and simulate hospital workflows. 
• 	Record a demo walkthrough. 
• 	Prepare resume bullet points and LinkedIn summary. 

📤 Final GitHub Push: 

• 	After full system test passes 
• 	Demo is recorded and linked in  
• 	Project is tagged with a release version (e.g., ) 
• 	Backup branch is created (e.g., ) 
• 	Final documentation and compliance notes are complete 
