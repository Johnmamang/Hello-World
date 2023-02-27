def caesar_decipher(ciphertext, distance):
    plaintext = ''
    for char in ciphertext:
        if char.isprintable():
            # convert the character to its ASCII code, subtract the distance value, and wrap around if necessary
            plain_code = (ord(char) - distance - 32) % 95 + 32
            # convert the plain code back to a character and append it to the plaintext
            plaintext += chr(plain_code)
        else:
            # if the character is not printable, just append it to the plaintext as-is
            plaintext += char
    return plaintext

# example usage
ciphertext = input("Enter ciphertext: ")
distance = int(input("Enter distance value: "))
plaintext = caesar_decipher(ciphertext, distance)
print("Decrypted text:", plaintext)
