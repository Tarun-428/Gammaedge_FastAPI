import hashlib

password = "Tarun123"
hashed_pass = hashlib.sha256(password.encode()).hexdigest()

print(password)
print(str(hashed_pass))

import bcrypt 
user_input = "Tarun123"
salt = bcrypt.gensalt(rounds=14)
# salt2 = bcrypt.gensalt()
bcrypted = bcrypt.hashpw(password.encode(),salt)
# bcrypted_check = bcrypt.hashpw(user_input.encode(),salt2)

# for i in range(7,23):
#     if bcrypted[i] == bcrypted_check[i]:
#         pass
#     else:
#         print("Not matched")
print(salt.decode())
print(bcrypted.decode())




from argon2 import PasswordHasher

ph = PasswordHasher()
hashed_pass = ph.hash("user_input")
print(hashed_pass)