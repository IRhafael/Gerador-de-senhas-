import random
from string import digits
from string import ascii_letters

symbols = ascii_letters + digits
secure_random = random.SystemRandom()
password = "".join(secure_random.choice(symbols)
                  for i in range (20))
print("sua nova senha é:", password)    