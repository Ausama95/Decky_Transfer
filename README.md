#Decky Transfer - Secure File Transfer from Windows PC to the steam deck or Linux

Decky Transfer is a user-friendly graphical user interface (GUI) application designed to facilitate secure file transfers between a Windows PC and The Steam Deck or remote Linux system using the SSH protocol. This program provides a simple and secure way to transfer files while ensuring data confidentiality and integrity.

##Features
Easy Configuration: Enter the remote Linux system's IP address, your username, and password.
File Selection: Choose the local file you want to transfer using the "Select File" button.
Secure Transfer: Utilizes the SSH protocol via the Paramiko library to establish a secure connection.
User-Friendly Interface: Intuitive GUI layout guides users through the file transfer process step by step.
Error Handling: Provides error messages for common issues, enhancing the user experience.
Helpful Instructions: Access instructions through the menu bar to learn how to use the program effectively.

##Usage

1. Enter the IP address of the remote Linux system, your username, and password.
2. Click "Select File" to choose the local file you want to transfer.
3. Specify the remote path (e.g., /home/username/) where you want to place the transferred file.
4. Click "Transfer File" to initiate the secure transfer.

##Getting Started

1. Clone the repository: git clone https://github.com/Ausama95/Decky_Transfer
2. Install required dependencies: pip install paramiko
3. Run the program: python decky_transfer.py

##Author
Created by Ausama95
