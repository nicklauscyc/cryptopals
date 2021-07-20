#!/bin/python3

import p3SingleByteXORCipher 

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
#     between two byte literals a and b
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

    # first we convert from base64 to hex
    import base64
    print(cypher)
    cypher = base64.b64decode(cypher)
    print(cypher)
    byteArray = cypher.hex()

    print("====")
    print(byteArray)

    minKEYSIZE = -1
    # check key sizes between 2 and 40 inclusive
    for _KEYSIZE in range(2,41):
        KEYSIZE = 2*_KEYSIZE
        #print(len(byteArray))
        #print(KEYSIZE)
        if len(byteArray) < 4 * KEYSIZE: raise ValueError("Not at least 4 blocks")

        # Get the first 4 blocks
        block1 = byteArray[0:KEYSIZE]
        block2 = byteArray[KEYSIZE:2*KEYSIZE]
        block3 = byteArray[2*KEYSIZE:3*KEYSIZE]
        block4 = byteArray[3*KEYSIZE:4*KEYSIZE]

        # Derive their average hamming distance
        dist1and2 = hammingDistance(block1, block2)
        dist3and4 = hammingDistance(block3, block4)
        avgDist = (dist1and2 + dist3and4) / 2

        # Update KEYSIZE if this has a lower average hamming distance
        if minKEYSIZE == -1:
            minDist = avgDist
            minKEYSIZE = _KEYSIZE
        else:
            if avgDist < minDist:
                minDist = avgDist
                minKEYSIZE = _KEYSIZE

    return minKEYSIZE

# transposeBlocks():
#
# Break the cipher text byteArray into blocks of KEYSIZE length, and transpose 
# the blocks by making a block that is the first byte of every block, second byte of 
# every block 
def transposeBlocks(cypher, _KEYSIZE):
    KEYSIZE = 2*_KEYSIZE
    import base64
    print(cypher)
    cypher = base64.b64decode(cypher)
    byteArray = cypher.hex()
    print(byteArray)

    outputBlocks = []
    for i in range(0,len(byteArray),KEYSIZE):
        if i + KEYSIZE > len(byteArray): 
            new = byteArray[i:]
            outputBlocks.append(new)
        else:
            new = byteArray[i:i+KEYSIZE]
            outputBlocks.append(new)

    print(outputBlocks)

    transposed = []
    for col in range(KEYSIZE):
        newBlock = ""
        for row in outputBlocks:
            if col < len(row):
                newBlock += row[col]
        transposed.append(newBlock)

    print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
    for row in transposed:
        print(row)
    return transposed
        
def getCharsFromBase64(cypher):
    import base64
    cypher = base64.b64decode(cypher)
    byteArray = cypher.hex()

    s = "" 
    for i in range(0,len(byteArray),2):
        c = int(byteArray[i:i+2],base=16)
        s += chr(c)

    print("+++++++++++++++++++++++++++++++++")
    print(s) 
    return s
        
    





if __name__ == "__main__":

    f = open("6.txt","r")
    rawCipher = f.read()
    keySize = getSmallestKEYSIZE(rawCipher)
    print(keySize)
    t = transposeBlocks(rawCipher, keySize)
    s1 = t[0]
    s2 = t[1]
    freq1 = p3SingleByteXORCipher.getFrequency(s1)
    freq2 = p3SingleByteXORCipher.getFrequency(s2)
    min1 = p3SingleByteXORCipher.bestScore(freq1)
    min2 = p3SingleByteXORCipher.bestScore(freq2)
    print(freq1)
    print(freq2)
    print("key:",chr(min1),chr(min2))
    key = chr(min1)+chr(min2)
    print(key)
    import p5ImplementingRepeatingKeyXOR
    s = p5ImplementingRepeatingKeyXOR.applyKey('ef', getCharsFromBase64(rawCipher))
    print(s)





