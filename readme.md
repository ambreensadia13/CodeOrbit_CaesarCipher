# Caesar Cipher Encryption Tool

**Cybersecurity Internship Task — CodeOrbit**

**Prepared by:** Ambreen Sadia  
**Submission Date:** 21 October 2026  
**Programming Language:** Python 3

## 1. Project Overview

The Caesar Cipher Encryption Tool is a beginner-friendly cybersecurity project developed using Python. It implements a classical encryption technique that shifts letters in the alphabet by a specified number of positions.

The program supports both encryption and decryption through an interactive command-line menu.

## 2. Project Objectives

- Understand the fundamentals of encryption and decryption.
- Learn how a classical substitution cipher works.
- Implement character manipulation using Python.
- Apply modular arithmetic to handle alphabet wraparound.
- Build an interactive command-line cybersecurity tool.

## 3. Features

- **Message encryption:** Converts plaintext into ciphertext.
- **Message decryption:** Converts ciphertext back into plaintext using the same shift key.
- **Custom shift key:** Allows the user to specify the number of alphabet positions to shift.
- **Case preservation:** Maintains uppercase and lowercase letters.
- **Punctuation preservation:** Keeps spaces, numbers, and punctuation unchanged.
- **Input validation:** Handles invalid menu choices and non-integer shift keys.
- **Interactive menu:** Allows repeated operations until the user exits.

## 4. Technologies Used

- **Python 3:** Main programming language.
- **Visual Studio Code:** Development environment.
- **Python standard library:** Built-in functions for character processing and arithmetic.

No third-party packages are required.

## 5. Project Structure

```text
CodeOrbit_CaesarCipher/
├── caesar_cipher.py
├── README.md
└── Testing the code/
```

The `screenshots` folder is optional but recommended for documenting actual test results.

## 6. Requirements

- Python 3 installed on your computer.
- Visual Studio Code or another Python-compatible editor.


## 7. How the Caesar Cipher Works

The Caesar cipher shifts each alphabetic character by a fixed number of positions.

For example, using a shift key of `3`:

| Plaintext | Ciphertext |
|---|---|
| A | D |
| B | E |
| C | F |
| X | A |
| Y | B |
| Z | C |

The program uses modular arithmetic with `% 26` because the English alphabet contains 26 letters. This ensures that letters wrap around to the beginning of the alphabet when necessary.

During decryption, the program reverses the shift to recover the original message.

## 8. Test Cases

The following test cases can be used to verify the program.

| Operation | Input message | Shift key | Expected output |
|---|---|---:|---|
| Encrypt | `HELLO` | 3 | `KHOOR` |
| Decrypt | `KHOOR` | 3 | `HELLO` |
| Encrypt | `Hello, World!` | 3 | `Khoor, Zruog!` |
| Encrypt | `XYZ` | 3 | `ABC` |

Run each test in your local environment and save screenshots of the actual output for your submission.

## 9. Cybersecurity Significance

Encryption helps protect information by transforming readable data into a different representation. The Caesar cipher is a useful introductory example of this principle.

However, its small key space and predictable substitution pattern make it easy to break using brute-force testing or frequency analysis.

**Security warning:** The Caesar cipher is intended for educational purposes only. It must not be used to protect passwords, personal information, confidential files, or real communications.

Modern applications should use established cryptographic algorithms and secure implementations.

## 10. Limitations

- Only alphabetic characters are shifted.
- Spaces, digits, and punctuation remain unchanged.
- The cipher offers no meaningful protection against modern attackers.
- The program does not save encrypted messages to files.
- It does not provide a graphical user interface.

## 11. Future Improvements

Possible enhancements include:

- Adding a graphical user interface.
- Supporting file-based encryption and decryption.
- Implementing automated unit tests.
- Adding brute-force analysis to demonstrate how classical ciphers can be broken.
- Comparing classical encryption with modern cryptographic techniques.

## 12. Conclusion

The Caesar Cipher Encryption Tool demonstrates fundamental cryptography concepts through a simple Python implementation. It provides practical experience with functions, loops, conditional statements, character manipulation, input validation, and modular arithmetic.

This project serves as an introductory exercise in cybersecurity programming and classical cryptography.

## 14. Submission Checklist

- [ ] `caesar_cipher.py` runs without errors.
- [ ] Encryption and decryption produce the expected results.
- [ ] Alphabet wraparound has been tested.
- [ ] Screenshots of actual program output have been captured.
- [ ] `README.md` is saved in the project folder.
- [ ] CodeOrbit submission requirements have been reviewed.

---

**Project:** Caesar Cipher Encryption Tool  
**Internship:** CodeOrbit Cybersecurity  
**Prepared by:** Ambreen Sadia  
**Submission Date:** 23 October 2026
