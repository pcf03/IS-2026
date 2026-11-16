import dns.resolver

respuesta = dns.resolver.query('en.wikipedia.org', 'A')
print("IP principal:", respuesta[0].address)

# Acceso de bajo nivel a la respuesta completa
print("\n--- Respuesta completa ---")
print(respuesta.response)