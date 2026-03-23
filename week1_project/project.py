import random
questions=[{'question':'Who was the first president of the republic of Kenya?','choices':['A.Uhuru Kenyatta','B.Raila Odinga','C.Mwai Kibaki','D.Jommo Kenyatta'],'answer':'D'},{'question':'Which year did Kenya gain independence?','choices':['A.1863','B.1964','C.1963','D.1984'],'answer':'C'},{'question':'How long does a president of Kenya serve?','choices':['A.5','B.10','C.2','D.3'],'answer':'A'},{'question':'Which year did Kenya become a republic?','choices':['A.1936','B.1946','C.1983','D.1964'],'answer':'D'}]
#shuffle the questions randomly
random.shuffle(questions)

score=0

print('Welcome to week 1 project quiz')

# Loop through each question
for i, q in enumerate(questions, start=1):
    print(f"Question {i}: {q['question']}")
    
    # choices
    for choice in q["choices"]:
        print(choice)

    while True:
        try:
            user_answer = input("Your answer (A/B/C/D): ")
            
            # Validate input
            if user_answer not in ["A", "B", "C", "D"]:
                raise ValueError("Invalid choice. Please enter A, B, C, or D.")
            
            break  # exit loop if input is valid
        
        except ValueError as e:
            print(e)
    
    

    
    # Check answer
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong!  {q['answer']}.")

#  final score
print(f"Your final score is {score} out of {len(questions)}.")

# feedback
if score == len(questions):
    print("Excellent! ")
elif score >= len(questions) // 2:
    print("Good! You can do better")
else:
    print("Read your notes")


