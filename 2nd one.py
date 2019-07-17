# Caesar Cipher





# the string to be encrypted/decrypted


print('Select your option')
print('Option1: To encrypt enter 1')
print('Option2: To decrypt enter 2')
Option1 = 'ENCRYPT'
Option2 = 'DECRYPT'
Selection = input()
print('Enter the password:')
message = input()

import cryptology
mode = 'encrypt' if Selection == '1' else 'decrypt'
print('mode', mode)
translated = cryptology.caesar(message, mode=mode)

print(translated)


from cryptology import caesar
translated = caesar(message)





