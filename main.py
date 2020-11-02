# welcome
print('Here is a simple quiz game.\n')

# read questions file and append each line into a list
questions = open('questions.txt', 'r')
# create array of questions
# use .strip() to remove line break \n that is added after each item
question_list = [line.strip() for line in questions.readlines()]

# close the questions file
questions.close()
 
# initialize score
score = 0
# set total score
total = len(question_list)

# run quiz 
for line in question_list:
    # split each question into Q and A parts
    q, a = line.split('=')
    # give Q and take answer input
    ans = input('{}='.format(q))
    # if answer correct, increase score by 1
    if a == ans:
        score += 1

# record results
result = open('result.txt', 'w')
result.write('Your final score is {}/{}'.format(score, total))
result.close()

# display results
print(f'Your final score is {score}/{total}.')