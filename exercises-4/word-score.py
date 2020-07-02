words = input().split()
print({word: sum([ord(c) - ord('a') + 1
                  for c in word])
       for word in words
       if len(word) >= 3 and len(word) <= 7})