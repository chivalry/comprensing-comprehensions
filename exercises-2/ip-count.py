ips = [line.split()[0] for line in open('mini-access-log.txt')]
print({ip: ips.count(ip) for ip in ips})
