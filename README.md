# ASK Me Project (Console Application)

## 📌 Project Idea
#“This project is developed by a team.
#Each member is responsible for specific modules.”
خهننمmple console-based application similar to Ask.fm. Users can sign up, log in, ask questions (anonymous or not), answer questions, and view feeds. The project is built using Python and Object-Oriented Programming (OOP) with file-based storage instead of a database.

---

## 📂 Project Structure

```
ask_me_project/
│
├── main.py
├── utils.py
│
├── models/
│   ├── user.py
│   ├── question.py
│   └── answer.py
│
├── managers/
│   ├── user_manager.py
│   └── question_manager.py
│
├── data/
│   ├── users.txt
│   └── questions.txt
│
├── requirements.txt
└── README.md
```

---

## 🧠 File & Folder Explanation

### 🔹 main.py

* Entry point of the application
* Displays menus (Login / Signup)
* Calls functions from utils and managers
* Controls application flow

---

### 🔹 utils.py

Contains helper (utility) functions:

* Input validation loops (re-prompting until valid input)
* Safe integer input with optional range checks
* Menu display functions
* String handling helpers

Used by main.py and managers to keep the code clean.

---

### 🔹 models/

Contains data models (OOP classes only):

#### user.py

* User class
* Stores user information (id, name, email, password, anonymous setting)

#### question.py

* Question class
* Stores question data (from user, to user, text, answer, anonymous flag, parent_id)

#### answer.py

* Answer class (optional)
* Represents answers separately if needed

---

### 🔹 managers/

Handles application logic and data synchronization:

#### user_manager.py

* User signup & login
* Load/save users from file
* Sync user data for multi-user scenarios

#### question_manager.py

* Ask, answer, delete questions
* Handle threaded questions (parent-child)
* Load/save questions
* Generate global feed

---

### 🔹 data/

Stores application data (file-based system):

* users.txt → stores users data
* questions.txt → stores questions data

Uses manual serialization instead of databases.

---

## 💾 Serialization & Deserialization

* Objects are converted to text using custom formats
* Each class supports:

  * to_line() → object → string
  * from_line() → string → object

This allows saving and loading data easily.

---

## 🔄 Syncing Data for Multi-User Scenarios

* Data is loaded at program start
* Data is saved after every change
* Ensures consistency between users and questions

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🎯 Concepts Used

* Object-Oriented Programming (OOP)
* Input validation loops
* File handling (read/write)
* Manual serialization
* Modular project structure
* Multi-user data synchronization

---

## ✅ Notes

* No database is used
* Project is suitable for learning OOP and clean code
* Easy to extend and maintain

