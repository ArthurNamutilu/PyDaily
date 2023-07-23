#!/usr/bin/python3
from question_class import Question

question_list = [
	"What is the capital city of Kenya?\n(a) Kisumu\n(b) Nairobi\n(c) Mombasa\n\n",
	"What is the capital city of Uganda?\n(a) Kampala\n(b) Jinja\n(c) Tororo\n\n",
	"What is the capital city of Burundi?\n(a) Kigali\n(b) Dodoma\n(c) Bujumbura\n\n",
]

# array of questions Question object
questions = [
	Question(question_list[0], 'b'),
	Question(question_list[1], 'a'),
	Question(question_list[2], 'c'),
]

def testquiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score += 1
    print(f"You got {score} / " + str(len(questions)) + " correct")

testquiz(questions)
