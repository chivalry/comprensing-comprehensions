print([(line.split(':')[0], line.split(':')[2])
       for line in open('linux-etc-passwd.txt')
       if not line.startswith('#')
          and len(line) > 2])