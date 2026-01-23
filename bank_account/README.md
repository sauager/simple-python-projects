# Python Bank Account System 🏦

A **Python-based banking system** project built with advanced **object-oriented programming (OOP)** concepts.  
This project demonstrates core banking functionalities like deposits, withdrawals, transfers, PIN management, and operations history — all implemented in a secure and modular way.  

---

## Features ✨

- **User account management**: Create accounts with unique IDs, names, balances, and PIN codes.  
- **Secure PIN verification**: Ensure only authorized access to deposits and withdrawals.  
- **Deposits & Withdrawals**: Support for regular and admin operations.  
- **Transfers**: Safely transfer funds between accounts with validation.  
- **Operations History**: Track all deposits and withdrawals with timestamps.  
- **PIN management**: Change your PIN manually or generate a new random one.  
- **Equality checks**: Compare account balances easily.  
- **JSON Support**: Retrieve account info and operations history in JSON format.  

---

## Project Structure 🏗️

- `BankInit` — Initializes user data and sets up the account.  
- `BankAccount` — Core class implementing all banking operations and validations.  
- `AbstractBankClass` — Abstract base class defining the banking interface.  
- `Errors` — Centralized error handling for all operations.  
- `Dunder` — Implements equality check for account balances.  
- **Operations history** — Stores a detailed log of deposits and withdrawals with timestamps.  

---

## Technologies 🛠️

- **Python 3.11+**  
- Object-Oriented Programming (OOP)  
- Abstract Base Classes (ABC)  
- `datetime` for timestamping operations  
- `json` for exporting account data  
- Randomized PIN generation for enhanced security  
