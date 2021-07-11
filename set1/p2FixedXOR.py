#!/bin/python3

from p1ConvertHexToBase64 import hexToBitArray

def bitArrayToHex(arr):
    s = ""
    for start in range(0, len(arr), 4):
        end = start + 4

        digit = arr[start:end]

        if digit ==   [0,0,0,0]:
            s += "0"
        elif digit == [0,0,0,1]:
            s += "1"
        elif digit == [0,0,1,0]:
            s += "2"
        elif digit == [0,0,1,1]:
            s += "3"
        elif digit == [0,1,0,0]:
            s += "4"
        elif digit == [0,1,0,1]:
            s += "5"
        elif digit == [0,1,1,0]:
            s += "6"
        elif digit == [0,1,1,1]:
            s += "7"
        elif digit == [1,0,0,0]:
            s += "8"
        elif digit == [1,0,0,1]:
            s += "9"
        elif digit == [1,0,1,0]:
            s += "a"
        elif digit == [1,0,1,1]:
            s += "b"
        elif digit == [1,1,0,0]:
            s += "c"
        elif digit == [1,1,0,1]:
            s += "d"
        elif digit == [1,1,1,0]:
            s += "e"
        elif digit == [1,1,1,1]:
            s += "f"
        else:
            raise ValueError("Should not come here")
    return s

def fixedXOR(hex1, hex2):
    bitArray1 = hexToBitArray(hex1)
    bitArray2 = hexToBitArray(hex2)

    if len(bitArray1) != len(bitArray2):
        raise ValueError("unequal string lengths")

    outputArray = []
    for i in range(len(bitArray1)):
        bit1 = bitArray1[i]
        bit2 = bitArray2[i]
        bitXOR = bit1 ^ bit2
        outputArray.append(bitXOR)

    return bitArrayToHex(outputArray)


if __name__ == "__main__":
    res = fixedXOR("1c0111001f010100061a024b53535009181c",
                   "686974207468652062756c6c277320657965")
    print(res)
    assert res == "746865206b696420646f6e277420706c6179"


