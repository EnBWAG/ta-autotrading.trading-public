from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
cypher = f.encrypt(b"A really secret message. Not for prying eyes.")
print(f'Cypher is {cypher}')



