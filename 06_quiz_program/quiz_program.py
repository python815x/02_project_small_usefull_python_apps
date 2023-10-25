# a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key values pairs
# display each question to the user and allow them to answer
# tell them if they were right or wrong
# show the final result when quiz is completed

quiz = {
    'question1': {
        'question': 'What is the capital of France?',
        'answer': 'Paris'
    },
    'question2': {
        'question': 'What is the capital of Germany?',
        'answer': 'Berlin'
    },
    'question3': {
        'question': 'What is the capital of Italy?',
        'answer': 'Rome'
    },
    'question4': {
        'question': 'What is the capital of Spain?',
        'answer': 'Madrid'
    },
    'question5': {
        'question': 'What is the capital of Portugal?',
        'answer': 'Lisbon'
    },
    'question6': {
        'question': 'What is the capital of Australia?',
        'answer': 'Canberra'
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    player_answer = input('Answer ?')
    print('\n')

    if player_answer.lower().strip() == value['answer'].lower():
        score += 1
        print('Correct!', end='\n')
        print(f'Your score is {score}', end='\n')
    else:
        print('Wrong!', end='\n')
        print(f'The correct answer is {value["answer"]}', end='\n')
        print(f'Your score is {score}', end='\n')

percent_performance = (score / len(quiz)) * 100

print(f'You got {score} points out of {len(quiz)}!')
print(f'Your percentage is {percent_performance:.2f}%!')