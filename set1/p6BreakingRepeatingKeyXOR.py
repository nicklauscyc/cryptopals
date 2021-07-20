#!/bin/python3

# Breaks a repeating key XOR. We first guess through key sizes from 2 to 40.
# For each key size KEYSIZE, take the first KEYSIZE number of bytes, and 
# second KEYSIZE number of bytes, and find the hamming distance between them,
# but we normalize this result by dividing the hamming distance by KEYSIZE
#
# The KEYSIZE with the smallest hamming distance is probably the actual 
# key size (prove why)

# hammingDistance():
# 
#     Calculates the hamming distance i.e. number of differing bits
#     between two strings, a and b
def hammingDistance(a, b):
    if len(a) != len(b): 
        raise ValueError("Strings must be equal length")

    totalDifferingBits = 0
    for i in range(len(a)):
        aLetter = a[i]
        bLetter = b[i]
        abXOR = ord(aLetter) ^ ord(bLetter)

        oneBits = 0
        while abXOR != 0:
            oneBits += abXOR % 2
            abXOR = abXOR // 2 
        totalDifferingBits += oneBits

    return totalDifferingBits

# getSmallesetKEYSIZE():
#
#     Assumes that we can have 4 blocks in the cipher text
def getSmallestKEYSIZE(cypher):

    # check key sizes between 2 and 40 inclusive
    for KEYSIZE in range(2,41):
        if len(cypher) > 4 * KEYSIZE: raise ValueError("Not at least 4 blocks")
        block1 = cypher[0:KEYSIZE]
        block2 = cypher[KEYSIZE:2*KEYSIZE]
        block3 = cypher[2*KEYSIZE:3*KEYSIZE]
        block4 = cypher[3*KEYSIZE:4*KEYSIZE]

if __name__ == "__main__":
    dist = hammingDistance("this is a test", "wokka wokka!!!")
    print(dist)


