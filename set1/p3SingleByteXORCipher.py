#!/bin/python3

import p1ConvertHexToBase64

# englishFrequency:
#
#     Just a dictionary mapping characters to their relative frequencies
englishFrequency = { "a" : 0.082,
                     "b" : 0.015,
                     "c" : 0.028,
                     "d" : 0.043,
                     "e" : 0.130,
                     "f" : 0.022,
                     "g" : 0.02,
                     "h" : 0.061,
                     "i" : 0.07,
                     "j" : 0.0015,
                     "k" : 0.0077,
                     "l" : 0.04,
                     "m" : 0.024,
                     "n" : 0.067,
                     "o" : 0.075,
                     "p" : 0.019,
                     "q" : 0.00095,
                     "r" : 0.06,
                     "s" : 0.063,
                     "t" : 0.091,
                     "u" : 0.028,
                     "v" : 0.0098,
                     "w" : 0.024,
                     "x" : 0.0015,
                     "y" : 0.02,
                     "z" : 0.00074
                     }

# getFrequency():
#
#     Takes in a hexadecimal string, and for each byte in that string that
#     represents a character, calculate its frequency and return a dictionary.
def getFrequency(hexString):
    byteArray = bytearray.fromhex(hexString)
    frequency = {}
    for byte in byteArray:
        if byte in frequency:
            frequency[byte] += 1
        else:
            frequency[byte] = 1
    return frequency

# printFrequency
#
#     Takes in a dictionary where the keys are bytes and values are counts
#     of those bytes that appear, and prints them out nicely
def printFrequency(frequency):
    for byte in frequency:
        count = frequency[byte]
        print("{} -> {}".format(byte.to_bytes(1,'big'), count))


def totalCount(frequency):
    total = 0
    for byte in frequency:
        total += frequency[byte]
    return total

# bestScore():
#
#     We take advantage of the fact that when we XOR a bit twice, we always
#     get back the same bit (TODO why though). We then iteratively try each
#     byte to XOR, and compare it to the frequency of letters in english
def bestScore(frequency):
    total = totalCount(frequency)
    minDiff = -1
    minCipher = ""
    for cipher in range(256):

        # this is a dictionary mapping ascii characters to their frequencies
        asciiToCounts = {}
        for encryptedByte in frequency:
            decryptedByte = cipher ^ encryptedByte

            # add to decrypted frequency, so we can compare each character's
            # frequency to the english language text
            asciiToCounts[chr(decryptedByte)] = frequency[encryptedByte] / total

        # now check the percentage differences for each frequency
        diff = 0
        for letter in englishFrequency:
            if letter not in asciiToCounts:
                diff += englishFrequency[letter]
            else:
                diff += abs(englishFrequency[letter] - asciiToCounts[letter])

        for letter in asciiToCounts:
            if letter not in englishFrequency:
                diff += asciiToCounts[letter]

        if minDiff == -1:
            minDiff = diff
            minCipher = cipher
        else:
            if diff < minDiff:
                minDiff = diff
                minCipher = cipher

    return minCipher


# decodeString():
#
#     with the given key byte, decode it with XOR
def decodeString(s, minCipher):
    if len(s) % 2 != 0:
        raise ValueError("Given string must have even number of 4-bit words!")

    result = ""
    totalBytes = len(s) / 2
    byteArray = bytearray.fromhex(s)
    for byte in byteArray:
        decoded = byte ^ minCipher
        result += chr(decoded)
    return result

if __name__ == "__main__":
    s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    frequency = getFrequency(s)
    minCipher = bestScore(frequency)
    print(minCipher)
    print(decodeString(s, minCipher))


