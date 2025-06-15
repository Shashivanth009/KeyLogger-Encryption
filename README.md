TITLE : Keylogger with Encrypted Data Exfiltration

Project Overview
This project is a proof-of-concept keylogger built for educational purposes. It captures user keystrokes, encrypts them securely using the Fernet encryption scheme, stores them locally with timestamps, and simulates data exfiltration to a localhost-based listener. It also includes a startup persistence mechanism and a kill switch.


Features
- Keystroke logging using `pynput`
- Fernet encryption of logs (`cryptography` module)
- Timestamped storage in `encrypted_logs.txt`
- Simulated data exfiltration using Python `socket`
- Startup persistence for Windows (via `winreg`)
- Kill switch: Press `ESC` to stop the keylogger


How to Run

1. Start the Listener Server
bash
python server.py

This will listen for logs on `localhost:9999`.


2. Run the Keylogger
bash
python keylogger.py

- Logs will be encrypted and saved locally.
- Every few seconds, data is sent to `localhost`.


3. Add to Startup (Optional)
For Windows users who want the logger to run on startup:
bash
python persistence.py


Project Structure


Keylogger-Encrypted/
├── keylogger.py
├── server.py
├── persistence.py
├── key.key                Encryption key
├── encrypted_logs.txt     Encrypted logs with timestamp
├── Keylogger_Project_Report.docx
└── README.md


Ethical Notice
This keylogger is created strictly for educational and ethical testing purposes.  
Do not deploy this tool on any machine without explicit authorization.


--Author--
Intern: Munnanuru Shashivanthu
Email: vj08655@gmail.com
Internship: Elevate Labs Cyber Security Intern
Project: Encrypted Keylogger with Exfiltration Simulation
