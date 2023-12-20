from Question_class import Question

question_prompts = [
    "What color are apples?\n(a)red\n(b)black\n(c)eggshell\n",
    "What color are bananas?\n(a)turquoise\n(b)yellow\n(c)black\n",
    "What color are grapes?\n(a)green\n(b)magenta\n(c)purple\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        answer = input("Enter your answer: ")
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)

