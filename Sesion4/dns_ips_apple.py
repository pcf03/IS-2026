import dns.resolver

print("--- IPs asignadas a apple.com ---")
respuesta = dns.resolver.query('apple.com', 'A')

for ip in respuesta:
    print(ip.address)