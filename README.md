 # CS50p QUIZ
## Description:
  CS50P Trivia Quiz is a command-line Python application designed to test your knowledge about Harvard’s CS50P course. The quiz features 10 multiple-choice questions covering fundamental concepts, tools, and details from CS50P, making it a fun and educational way to review course material.

## How to Run

  1. Ensure you have Python 3 installed.
  2. In the terminal, navigate to the project folder.
  3. Run the quiz with:
    'python project.py'
  4. To run tests and verify functionality:
    'pytest test_project.py'


# Files and functions

## project.py

  main()
    This is the entry point of the program.It loads questions from the JSON file, iterating through each question to prompt the user, recording the results, and finally calculating and displaying the user’s total score. It ensures the program runs in a clear, linear flow.

  load_questions(filename)
    This function is responsible for reading and parsing the quiz questions stored in a JSON file.

  ask_question(question)
    This function presents a single question to the user. It displays the question text and numbered answer choices, accepts user input, validates it to ensure a number between 1 and 4 is entered, and then determines if the selected answer is correct. It returns a boolean indicating whether the user answered correctly, enabling score tracking.

  calculate_score(results)
    After all questions have been answered, this function takes the list of boolean results and calculates both the total number of correct answers and the corresponding percentage score. This separation of score calculation allows for easy adjustments or extensions (such as weighted scoring) in the future.



## test_project.py

  test_load_questions()
    This test verifies that the 'load_questions()' function correctly reads and parses the JSON file into the expected data structure. It checks that the number of questions and the format of each question match expectations, ensuring the program has valid input data.

  test_ask_question_correct()
    This test simulates a user inputting the correct answer and checks that the 'ask_question()' function returns 'True'.

  test_ask_question_incorrect()
    Similar to the previous test, this one simulates the user choosing an incorrect answer and asserts that 'ask_question()' correctly returns 'False', confirming the program accurately identifies wrong answers.

  test_ask_question_invalid_input()
    This test ensures that if a user inputs invalid data, the Function handles it gracefully by prompting again until valid input is received. It tests the robustness of input validation to prevent crashes or infinite loops

  test_calculate_score()
    This test checks that the 'calculate_score()' function correctly counts the number of 'True' values (correct answers) in the results list and calculates the correct percentage score. It confirms that scoring logic works as expected for different input scenarios.

## questions.json

  This file contains all the quiz questions and their possible answers in JSON Format, each question is represented as an object with three key parts:

  question: The text of the question to be asked.
  choices: A list of four possible answers (strings).
  answer: The string text that corresponds to the correct choice in the list.

  Example of a real question entry:
  {
    "question": "What is the correct way to check if two variables are equal in Python?",
    "choices": ["=", "==", "===", "!="],
    "answer": "=="
  }

## Design and final thoughts
  One key design choice was to separate the quiz questions, choices and answers into a JSON file (questions.json), from the program logic (project.py), this makes it so new questions can be added without touching the main logic, and the program will adapt, this project uses only Python’s standard library, but the project’s tests require the 'pytest' package, which must be installed separately via 'pip install pytest'

  This project strengthened my understanding of Python fundamentals, file I/O, JSON, function design, testing with pytest, and basic user interaction in the terminal, it provided a satisfying opportunity to integrate these concepts into a cohesive, functional program that is now CS50p QUIZ, thanks to Harvard’s CS50P course and David J. Malan for providing the foundational knowledge and inspiration for this project.


