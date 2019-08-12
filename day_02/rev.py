# example = 'test'

# 'a' -> 'b'
# # ord()


# String -> 'test'
# ASCII -> ord('a') = 97
# for Loop
# chr(97) = a

#userInput = input("String to encrypt: ")
userInput = 'abc'
encryptedOutput = ''

incBy = input("Increment by? ")

incBy = '1'
# isDig = '22'.isdigit()

# print(isDig)

key = int(incBy)

print("actualInput:", userInput)
for ch in userInput:
    asc = ord(ch)
    asc = asc + key
    newCh = chr(asc)
    encryptedOutput = encryptedOutput + newCh

print("Encrypted user input:", encryptedOutput)

# Receiving End

decryptedOutput = ''

for ch in encryptedOutput:
    asc = ord(ch)
    asc = asc - key
    newCh = chr(asc)
    decryptedOutput = decryptedOutput + newCh

print("Receiver Output: ", decryptedOutput)

# def encrypt(text, key, mode):
# place function content here!


choice = input("e/d?")
if True:
  # decrypt
else:
    pass
