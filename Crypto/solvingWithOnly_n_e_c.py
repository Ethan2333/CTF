from Crypto.Util.number import long_to_bytes
from pwn import *
from decimal import *

# The challenge will provide us the values for n, e and c

n = "long_number"
e = "number"
c = "long_number"

# So the challenge takes in any ciphertext provided by us (except the actual ciphertext that we need to decrypt) and return the deciphered text to us
# Hence, we can modify the ciphertext given to us. We know ciphertext = (message)**e mod n
# We can generate a new ciphertext as following:
ciphertext = Decimal(c) * ((2 ** Decimal(e)) % Decimal(n)) % Decimal(n)
conn.send(str(ciphertext), '\r\n')

# If we are getting back the diphered text from a remote server program then we have to use .decode() function to convert bytes to plain numbers
received = conn.recv().decode()

# We can print out the long int numbers for us to see
print(received)

decrypted = Decimal("long_int_number") / 2
answer = long_to_bytes(decrypted)
