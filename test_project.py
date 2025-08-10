from project import load_questions, ask_question, calculate_score

def test_load_questions(tmp_path):
    sample = '[{"question":"Q?","choices":["A","B"],"answer":"A"}]'
    file = tmp_path / "questions.json"
    file.write_text(sample)
    questions = load_questions(str(file))
    assert isinstance(questions, list)
    assert questions[0]["question"] == "Q?"

def test_ask_question_correct():
    question = {
        "question": "What language is CS50P taught in?",
        "choices": ["Python", "C", "Java", "JavaScript"],
        "answer": "Python"
    }
    assert ask_question(question, "1") == True

def test_ask_question_incorrect():
    question = {
        "question": "What language is CS50P taught in?",
        "choices": ["Python", "C", "Java", "JavaScript"],
        "answer": "Python"
    }
    assert ask_question(question, "2") == False

def test_ask_question_invalid_input():
    question = {
        "question": "What language is CS50P taught in?",
        "choices": ["Python", "C", "Java", "JavaScript"],
        "answer": "Python"
    }
    assert ask_question(question, "xyz") == False

def test_calculate_score():
    results = [True, False, True, True]
    total, percent = calculate_score(results)
    assert total == 3
    assert abs(percent - 75.0) < 0.01
