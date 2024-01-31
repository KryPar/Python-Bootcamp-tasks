import time
questions = ["What's capiatal city of Germany?","What's population of Czech Republic?", "What's favorite sport in UK?"]

possible_answers = {"What's capiatal city of Germany?": ["1. Berlin","2. Paris","3. London","4. Rome"],"What's population of Czech Republic?": ["1. 5 milions", "2. 15 milions ", "3. 10 milions", "4. 12 milions"], "What's favorite sport in UK?": ["1. Hockey", "2. Football", "3. Basketball", "4. Cricket"]}

answers = ["1", "3", "2"]

i = 0

score_x = 0

start_time = time.time()
right_questions = []

wrong_questions = []

for key in possible_answers:
    print()
    print(f"{key}")

    for answer in possible_answers[key]:
        
        print (f"{answer}")

    print()

    x = input ("What is the answer (1/2/3/4): ")     

    if x == answers[i]:
     score_x = score_x + 1
     right_questions.append(key)
     print()
     print("Your answer is right")
    else:
     
     wrong_questions.append(key)
     print()
     print("Your answer is wrong")
     

    i += 1
      
print() 
end_time = time.time()
print(f"Your score is: {score_x}/3 ")
    
print()

print(f"Your right questions are:")
for right_question in right_questions:
  print(right_question) 

print()

print(f"Your wrong questions are: ")
for wrong_question in wrong_questions:
  print(wrong_question) 
  
print()
elapsed_time = round(end_time - start_time)
print(f"Time druration: {elapsed_time} s")