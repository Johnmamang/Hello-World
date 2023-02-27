def caesar_cipher(plaintext, distance):
    ciphertext = ''
    for char in plaintext:
        if char.isprintable():
            # convert the character to its ASCII code, add the distance value, and wrap around if necessary
            cipher_code = (ord(char) + distance - 32) % 95 + 32
            # convert the cipher code back to a character and append it to the ciphertext
            ciphertext += chr(cipher_code)
        else:
            # if the character is not printable, just append it to the ciphertext as-is
            ciphertext += char
    return ciphertext

# example usage
plaintext = input("Enter plaintext: ")
distance = int(input("Enter distance value: "))
ciphertext = caesar_cipher(plaintext, distance)
print("Encrypted text:", ciphertext)
