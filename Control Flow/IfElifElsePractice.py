points = 174

if points <= 1:
    result = "You need to at least score 1 point!"
elif points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "COngratulations ! You won a wafer - thin mint!"
else:
    result = "Congratulations! You won a penguin!"
print(result)

answer = 12
guess = 12

if guess < answer:
    result = "Oops! Your guess was too low"
elif guess > answer:
    result = "Oops! Your guess was too high"
elif guess == answer:
    result = "Nice! Your guess matched the answer!"

print(result)

state = 'NY'
purchase_amount = 5500

if state == 'CA':
    tax_amount = .75
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)