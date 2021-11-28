poker = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

card1 = input()
card2 = input()
card3 = input()
card4 = input()
card5 = input()

print((poker.index(card1) + 1) + (poker.index(card2) + 1) + (poker.index(card3) + 1) + (poker.index(card4) + 1) + (poker.index(card5) + 1))



# poker = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# cards = []

# for i in range(5):
#     cards.append(input())

# print(list(map(lambda x: poker.index(x) + 1, cards)))



# cards = [input() for i in range(5)]

# print(sum(map(lambda x: poker)))