# 🚀 Compiler Visualization Tool

> An Interactive Compiler Phase Visualization System built using **Python**, **Streamlit**, **Pandas**, **Regular Expressions**, and **Graphviz**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

# 📖 Overview

The **Compiler Visualization Tool** is an educational application designed to help students understand the internal working of a compiler by visually demonstrating each phase of compilation.

Instead of treating the compiler as a black box, this application allows users to observe how source code is transformed step-by-step into intermediate representations and target assembly instructions.

---

# 🎯 Objectives

- Understand the complete compilation process.
- Visualize every compiler phase interactively.
- Demonstrate compiler concepts using simple C-style programs.
- Improve learning through graphical representation.

---

# ✨ Features

✅ Lexical Analysis

✅ Syntax Analysis

✅ Symbol Table Generation

✅ Parse Tree Visualization

✅ Three Address Code (TAC)

✅ Code Optimization

✅ Assembly Code Generation

✅ Interactive Web Interface

---

# 🏗 Compiler Workflow

```
Source Code
      │
      ▼
Lexical Analysis
      │
      ▼
Syntax Analysis
      │
      ▼
Symbol Table
      │
      ▼
Parse Tree
      │
      ▼
Three Address Code
      │
      ▼
Code Optimization
      │
      ▼
Assembly Code
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Logic |
| Streamlit | Web Interface |
| Pandas | Data Display |
| Regex | Lexical & Syntax Analysis |
| Graphviz | Parse Tree Visualization |

---

# 📂 Project Structure

```
COMPILER_PROJECT
│
├── app.py                 # Main Streamlit Application
├── lexer.py               # Lexical Analysis
├── parser.py              # Syntax Analysis
├── parse_tree.py          # Parse Tree Generator
├── symbol_table.py        # Symbol Table
├── tac.py                 # Three Address Code
├── optimizer.py           # Code Optimization
├── codegen.py             # Assembly Code Generation
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/compiler-visualization-tool.git
```

Go to project folder

```bash
cd compiler-visualization-tool
```

Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
streamlit run app.py
```

Application will open automatically at

```
http://localhost:8501
```

---

# 💻 Sample Input

```c
int marks = 85;
int bonus = 5;
int total = marks + bonus;
```

---

# 📸 Output

The application demonstrates:

- Source Code
- Tokens
- Syntax Validation
- Symbol Table
- Parse Tree
- Three Address Code
- Optimized Code
- Assembly Code

---

# 📚 Compiler Phases

## 1️⃣ Lexical Analysis

Converts source code into tokens such as

- Keywords
- Identifiers
- Operators
- Numbers
- Symbols

---

## 2️⃣ Syntax Analysis

Validates whether the program follows the grammar rules.

---

## 3️⃣ Symbol Table

Stores

- Variable Names
- Data Types
- Assigned Values

---

## 4️⃣ Parse Tree

Displays the hierarchical representation of the program.

---

## 5️⃣ Three Address Code

Generates intermediate code for optimization.

Example

```
t1 = a + b
c = t1
```

---

## 6️⃣ Code Optimization

Optimizes intermediate code using compiler optimization techniques.

Example

```
10 + 20
```

↓

```
30
```

---

## 7️⃣ Assembly Code Generation

Produces target assembly instructions.

Example

```
MOV R1,10
ADD R1,20
MOV c,R1
```

---

# 🎯 Applications

- Compiler Design Laboratory
- Educational Visualization
- Programming Language Learning
- Compiler Demonstrations
- Academic Projects

---

# 🚀 Future Enhancements

- Support complete C language
- Semantic Analysis
- Type Checking
- Error Recovery
- Java Compiler Support
- Python Compiler Support
- Machine Code Generation
- AI-Based Code Explanation

---

# 👨‍💻 Team Members

- Syed Musaib
- Yashwanth Shaga
- Venkata Avinash
- Vishnu Vardhan

---

# 👩‍🏫 Project Guide

Faculty Guide

P.Srilakshmi

---

# 📜 License

This project is developed for educational purposes.

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.

---

## Thank You ❤️
