n = int(input())

for i in range(n):

    sentence = input()

    alphabet = set(filter(lambda x: x.isalpha(), set(sentence.lower())))

    print(len(alphabet) == 26)