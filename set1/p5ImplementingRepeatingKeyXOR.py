#!/bin/python3

# Implements repeating-key XOR

# applyKey();
#
#    Applies the key one letter at a time and repeats modulo the key 
#    length
def applyKey(key, message):
    keyLen = len(key)
    code = ""
    for i in range(len(message)):

        # get relevant letters and XOR
        letter = message[i]
        keyIndex = i % keyLen
        keyLetter = key[keyIndex]
        encrypted = ord(keyLetter) ^ ord(letter)
        byte = str(hex(encrypted))[2:]

        # 0 pad if necessary
        if len(byte) < 2: byte = "0" + byte

        # append to code
        code += byte

    return code

if __name__ == "__main__":
    s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    print(s)

    code = applyKey("ICE", s)
    print(code)
    print("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")

