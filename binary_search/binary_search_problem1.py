# PROBLEM 1:
# Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
# and lays them out face down in a sequence on a table. She challenges Bob to pick out the card
# containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

def solution(cards, given_number):
    
    start_index = 0
    end_index = len(cards) - 1
    
    while start_index <= end_index:
        
        middle = (start_index + end_index) // 2
        
        if cards[middle] == given_number:
            return print(given_number, "Found!")
        elif cards[middle] > given_number:
            start_index = middle + 1
        elif cards[middle] < given_number:
            end_index = middle - 1

    print("--- Element not present in the array ---")

solution([99,82,71,63,55,48,39,25,11,8], 71)