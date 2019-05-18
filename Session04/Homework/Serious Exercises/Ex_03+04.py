########## Question 01 ############

print("Answer the following algebra question:")
question1 = "If x = 8, then what is the value of 4(x + 3)"
options1 = "1. 35\n2. 36\n3. 40\n4. 44\n"
print(question1)
print(options1)
correct_answer = 0


while True:
    response = input("Your choice: ")

    if response == "4":
        print('Bingo')
        correct_answer += 1
        break
    else:
        print(": (,")
        break

########## Question 02 ############

print("Estimate this answer (exact calculation not needed): ")
question2 = "Jack scored these marks in 5 math testS: 49, 81, 72, 66 and 52. What is the mean"
options2 = "1. About 55\n2. About 65\n3. About 75\n4. About 85\n"
print(question2)
print(options2)

while True:
    response = input("Your choice: ")

    if response == "2":
        print('Bingo')
        correct_answer += 1
        break
    else:
        print(": (")
        break

########## Total right answer ############

question = [question1,question2]

print("You correctly answer",correct_answer,"out of",len(question),"questions")

########## End programn ############