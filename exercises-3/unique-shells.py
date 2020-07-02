print({line.split(':')[-1].split('/')[-1].strip()
       for line in open('linux-etc-passwd.txt')
       if 'false' not in line
          and not line.startswith('#')})