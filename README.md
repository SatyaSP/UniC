UniC: A C Compiler Frontend
=====================================
UniC is a C compiler frontend implemented in Python, comprising a Lexer, Parser, Semantic Analyzer, and Symbol Table Manager.

Overview
------------
This project was developed as part of the Compiler Design lab sessional during my BTech IT undergraduate course. UniC aims to provide a basic C compiler frontend, demonstrating the fundamental concepts of compiler design.

Features
------------
- Lexer: Tokenizes C source code into lexical units
- Parser: Parses tokens into an Abstract Syntax Tree (AST)
- Semantic Analyzer: Performs semantic checks on the AST
- Symbol Table Manager: Manages symbol tables for identifier storage

Implementation Details
-------------------------
- Programming Language: Python
- Libraries : anytree
- Compiler Components: Lexer, Parser, Semantic Analyzer, Symbol Table Manager

Getting Started
-------------------
To explore UniC, follow these steps:

1. Clone the repository:
   ```git clone https://github.com/SatyaSP/UniC.git```
2. Navigate to the project directory:
   ```cd UniC```
3. Activate the ```unic_venv``` virtual environment.   
4. Run the compiler frontend using Python:
   ```python unic.py```

If you are on windows you can use unic.cmd or unic.ps1 to directly run commands on command prompt or powershell to provide the C file path. (```.\unic <path/to/c/file.c>```). Alternatively you can add this directory to you environment variables to use this command globally in your terminal.

