import ipaddress

ip = '192.168.0.0/24'

endereco = ipaddress.ip_network(ip, strict=False)

for ip in endereco:
    print(ip)