words = {word.strip() for word in open('words')}
inpt = input().split()
print({word: word.lower() in words for word in inpt})
