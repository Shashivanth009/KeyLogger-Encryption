TITLE : Keylogger with Encrypted Data Exfiltration

Project Overview:
This project is a proofofconcept keylogger created for educational and ethical cybersecurity learning. It demonstrates how keylogging, encryption, and simulated data exfiltration techniques work together. The tool captures keystrokes, encrypts them using Fernet symmetric encryption, and simulates data transmission to a remote server (localhost).

Features:
 - Captures all keyboard input
 - Encrypts logs using Fernet (cryptography module)
 - Timestamps each log entry
 - Simulates exfiltration via localhost socket server
 - Optional startup persistence (Windows only)
 - ESC key acts as a kill switch

Tools & Technologies:
 Python 3
 [pynput](https://pynput.readthedocs.io/en/latest/) for capturing keystrokes
 [cryptography](https://cryptography.io/en/latest/) for Fernet encryption
 Builtin socket, datetime, threading, os, and winreg modules


Getting Started:

 1. Clone the Repository
bash
git clone https://github.com/yourusername/KeyloggerEncrypted.git
cd KeyloggerEncrypted

 2. Install Dependencies

bash
pip install pynput cryptography

 3. Start the Listener Server

In one terminal:

bash
python server.py

 4. Run the Keylogger

In a separate terminal:

bash
python keylogger.py

Encrypted logs will be saved locally and sent to the server every few seconds.

File Structure:

KeyloggerEncrypted/
├── keylogger.py
├── server.py 
├── persistence.py
├── key.key
├── encrypted_logs.txt
├── README.md
└── Keylogger_Project_Report.docx

Important Notes:

 key.key is generated once and must be preserved to decrypt logs.
 Do not run persistence on a production system — test only in a virtual machine or sandbox.


Ethical Disclaimer:

This keylogger is developed strictly for educational purposes under a cybersecurity internship.
Do not deploy or use this tool on systems without explicit written permission.
Misuse of such tools may be illegal and unethical.


Author:

Name: Munnanuru Shashivanthu,
Email: vj08655@gmail.com,
Internship: Elevate Labs Cybersecurity Internship,
Project: Keylogger with Encrypted Data Exfiltration

License:

This project is licensed for academic and ethical testing use only. All misuse is strictly discouraged.
