# Caesar Cipher

  
def caesar(message, key=6, mode='encrypt'):
    




    # every possible symbol that can be encrypted

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+/-()ÄÖÜß'


    # stores the encrypted/decrypted form of the message

    translated = ''

    # capitalize the string in message

    message = message.upper()



    # run the encryption/decryption code on each symbol in the message string

    for symbol in message:

        if symbol in LETTERS:

            # get the encrypted (or decrypted) number for this symbol

            num = LETTERS.find(symbol) # get the number of the symbol

            if mode == 'encrypt':

                num = num + key
         
            elif mode == 'decrypt':

                num = num - key
            
            encrypted_symbol = LETTERS[num % len(LETTERS)]
            
            translated += encrypted_symbol   
             
        else:
            translated = translated + symbol

    return translated

