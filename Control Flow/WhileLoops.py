card_deck = [4, 11, 8, 5, 13, 2, 9, 10]
hand = []

while sum(hand) <= 17:
    hand.append(card_deck.pop())

print(hand)

number = 42

product = 1

current = 1

while current <= number:
    product *= current
    current += 1


print(product)

start_num = 5
end_num = 100
count_by = 2

break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)
