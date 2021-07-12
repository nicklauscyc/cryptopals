#!/bin/python3

from p3SingleByteXORCipher import getFrequency
from p3SingleByteXORCipher import bestScore
from p3SingleByteXORCipher import decodeString

def decrypt(s):
    frequency = getFrequency(s)
    minKey = bestScore(frequency)
    result = decodeString(s, minKey)
    return result


if __name__ == "__main__":

    f = open("4.txt")
    for row in f:
        print(len(row[:-1]))
        result = decrypt(row[:-1])
        print(result)
