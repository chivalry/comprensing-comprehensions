print({octet
       for line in open('mini-access-log.txt')
       for octet in line.split()[0].split('.')})
