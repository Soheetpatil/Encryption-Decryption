# 🔐 Caesar Cipher Encryption System

A Python-based command-line application that implements the Caesar Cipher algorithm for text encryption and decryption. This project demonstrates the fundamentals of classical cryptography and secure message transformation using shift-based substitution.

## 📖 Overview

The Caesar Cipher is one of the oldest and simplest encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions in the alphabet.

This application allows users to:

* Encrypt text using a custom shift key
* Decrypt encrypted text using the same key
* Handle uppercase and lowercase letters
* Preserve spaces, numbers, and special characters

## 🚀 Features

* Text Encryption
* Text Decryption
* User-defined Shift Key
* Uppercase & Lowercase Support
* Input Validation
* Menu-Driven Interface
* Preserves Special Characters and Numbers

## 🛠 Technologies Used

* Python 3
* String Manipulation
* ASCII Character Encoding
* Cryptography Fundamentals

## 📂 Project Structure

```text
Caesar-Cipher-Encryption-System/
│
├── main.py
├── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Soheetpatil/Caesar-Cipher-Encryption-System.git
```

Navigate to the project folder:

```bash
cd Caesar-Cipher-Encryption-System
```

## ▶️ Run the Program

```bash
python main.py
```

## 💻 Example

### Encryption

Input:

```text
Hello World
Shift Key: 3
```

Output:

```text
Khoor Zruog
```

### Decryption

Input:

```text
Khoor Zruog
Shift Key: 3
```

Output:

```text
Hello World
```

## 🔑 How Caesar Cipher Works

Each letter is shifted by a fixed number of positions.

Example with Shift Key = 3:

```text
A → D
B → E
C → F
```

The process continues through the alphabet while wrapping around from Z back to A.

## 📚 Learning Outcomes

This project demonstrates:

* Classical Cryptography Concepts
* Encryption & Decryption Logic
* ASCII Character Manipulation
* Python Functions
* User Input Validation
* Command-Line Application Development

## 🔮 Future Improvements

* Brute Force Attack Mode
* File Encryption Support
* GUI Version using Tkinter
* Multiple Cipher Algorithms
* Password-Protected Encryption
* Cryptography Toolkit Integration

## 👨‍💻 Author

Soheet Patil

## 📜 License

This project is intended for educational and learning purposes.
