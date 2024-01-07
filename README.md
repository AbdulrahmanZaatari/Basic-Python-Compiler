# Code Analysis and Error Checker 👩‍💻🔍

This Python script is designed to read code from files, analyze it, and check for various syntax and style errors. It provides functionalities to display the code, identify errors, count errors, and exit the file.

## Features 📝

- **readFromFile(file_name):** Reads code from a file and returns a list of lines.
- **storeVariables(L):** Extracts and stores variables from the code.
- **oneEqual(L, EL):** Identifies lines with a single equal sign, which might indicate assignment instead of equality check.
- **floatError(L, EL):** Detects errors where commas are used instead of periods for floating-point numbers.
- **multiplicationError(L, EL):** Flags the use of 'x' instead of '*' for multiplication.
- **equalError(L, EL):** Checks for missing equal signs in assignments.
- **printChecker(L, EL):** Notifies if the 'Print' statement is written with an uppercase 'P'.
- **variableChecker(L, EL):** Identifies lines where variables are used without being defined.
- **ifCondition(L, EL):** Flags 'if' statements missing a colon at the end.
- ... and many more functions for different types of errors.

## Usage 🚀

1. Enter your name.
2. The script reads and analyzes multiple code files (file1.txt, file2.txt, file3.txt, file4.txt).
3. It allows you to display the code, display errors, count errors, and exit the file.
4. Various error checks are performed, and detailed error messages are displayed.

## Additional Tips 🤔

- Emphasis on code readability, with messages in curly braces.
- Encouraging and motivational messages to the user.
- Interactive menus to choose actions.

## How to Run 🏃‍♂️

Simply run the `main()` function.

Follow the prompts to analyze and check errors in the provided code files.

Feel free to contribute or customize the script according to your needs! Happy coding! 🚀👨‍💻
