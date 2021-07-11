#!/bin/python3

# Convert hex to base64

# hexToBitArray():
#
#     Converts hexadecimal string to an array of bits
def hexToBitArray(s):
    bitArray = []
    s = s.lower()
    for letter in s:
        if letter == "0":
            bitArray.extend([0,0,0,0])
        elif letter == "1":
            bitArray.extend([0,0,0,1])
        elif letter == "2":
            bitArray.extend([0,0,1,0])
        elif letter == "3":
            bitArray.extend([0,0,1,1])
        elif letter == "4":
            bitArray.extend([0,1,0,0])
        elif letter == "5":
            bitArray.extend([0,1,0,1])
        elif letter == "6":
            bitArray.extend([0,1,1,0])
        elif letter == "7":
            bitArray.extend([0,1,1,1])
        elif letter == "8":
            bitArray.extend([1,0,0,0])
        elif letter == "9":
            bitArray.extend([1,0,0,1])
        elif letter == "a":
            bitArray.extend([1,0,1,0])
        elif letter == "b":
            bitArray.extend([1,0,1,1])
        elif letter == "c":
            bitArray.extend([1,1,0,0])
        elif letter == "d":
            bitArray.extend([1,1,0,1])
        elif letter == "e":
            bitArray.extend([1,1,1,0])
        elif letter == "f":
            bitArray.extend([1,1,1,1])
        else:
            raise ValueError("Input not hexadecimal, letter: '{}'".format(letter))
    return bitArray

# bitArrayToBase64():
#
#     Converts bit array to a base64 string
def bitArrayToBase64(arr):
    s = ""
    for start in range(0, len(arr), 6):
        end = start + 6

        # sometimes we need padding for the last sextet
        diff = 0
        if end > len(arr):
            diff = end - len(arr)
            end = len(arr)

        # create the digit of 6 bits, pad if necessary
        digit = arr[start:end]
        for i in range(diff):
            digit.append(0)

        if digit ==   [0,0,0,0,0,0]:
            s += "A"
        elif digit == [0,0,0,0,0,1]:
            s += "B"
        elif digit == [0,0,0,0,1,0]:
            s += "C"
        elif digit == [0,0,0,0,1,1]:
            s += "D"
        elif digit == [0,0,0,1,0,0]:
            s += "E"
        elif digit == [0,0,0,1,0,1]:
            s += "F"
        elif digit == [0,0,0,1,1,0]:
            s += "G"
        elif digit == [0,0,0,1,1,1]:
            s += "H"
        elif digit == [0,0,1,0,0,0]:
            s += "I"
        elif digit == [0,0,1,0,0,1]:
            s += "J"
        elif digit == [0,0,1,0,1,0]:
            s += "K"
        elif digit == [0,0,1,0,1,1]:
            s += "L"
        elif digit == [0,0,1,1,0,0]:
            s += "M"
        elif digit == [0,0,1,1,0,1]:
            s += "N"
        elif digit == [0,0,1,1,1,0]:
            s += "O"
        elif digit == [0,0,1,1,1,1]:
            s += "P"
        elif digit == [0,1,0,0,0,0]:
            s += "Q"
        elif digit == [0,1,0,0,0,1]:
            s += "R"
        elif digit == [0,1,0,0,1,0]:
            s += "S"
        elif digit == [0,1,0,0,1,1]:
            s += "T"
        elif digit == [0,1,0,1,0,0]:
            s += "U"
        elif digit == [0,1,0,1,0,1]:
            s += "V"
        elif digit == [0,1,0,1,1,0]:
            s += "W"
        elif digit == [0,1,0,1,1,1]:
            s += "X"
        elif digit == [0,1,1,0,0,0]:
            s += "Y"
        elif digit == [0,1,1,0,0,1]:
            s += "Z"
        elif digit == [0,1,1,0,1,0]:
            s += "a"
        elif digit == [0,1,1,0,1,1]:
            s += "b"
        elif digit == [0,1,1,1,0,0]:
            s += "c"
        elif digit == [0,1,1,1,0,1]:
            s += "d"
        elif digit == [0,1,1,1,1,0]:
            s += "e"
        elif digit == [0,1,1,1,1,1]:
            s += "f"
        elif digit == [1,0,0,0,0,0]:
            s += "g"
        elif digit == [1,0,0,0,0,1]:
            s += "h"
        elif digit == [1,0,0,0,1,0]:
            s += "i"
        elif digit == [1,0,0,0,1,1]:
            s += "j"
        elif digit == [1,0,0,1,0,0]:
            s += "k"
        elif digit == [1,0,0,1,0,1]:
            s += "l"
        elif digit == [1,0,0,1,1,0]:
            s += "m"
        elif digit == [1,0,0,1,1,1]:
            s += "n"
        elif digit == [1,0,1,0,0,0]:
            s += "o"
        elif digit == [1,0,1,0,0,1]:
            s += "p"
        elif digit == [1,0,1,0,1,0]:
            s += "q"
        elif digit == [1,0,1,0,1,1]:
            s += "r"
        elif digit == [1,0,1,1,0,0]:
            s += "s"
        elif digit == [1,0,1,1,0,1]:
            s += "t"
        elif digit == [1,0,1,1,1,0]:
            s += "u"
        elif digit == [1,0,1,1,1,1]:
            s += "v"
        elif digit == [1,1,0,0,0,0]:
            s += "w"
        elif digit == [1,1,0,0,0,1]:
            s += "x"
        elif digit == [1,1,0,0,1,0]:
            s += "y"
        elif digit == [1,1,0,0,1,1]:
            s += "z"
        elif digit == [1,1,0,1,0,0]:
            s += "0"
        elif digit == [1,1,0,1,0,1]:
            s += "1"
        elif digit == [1,1,0,1,1,0]:
            s += "2"
        elif digit == [1,1,0,1,1,1]:
            s += "3"
        elif digit == [1,1,1,0,0,0]:
            s += "4"
        elif digit == [1,1,1,0,0,1]:
            s += "5"
        elif digit == [1,1,1,0,1,0]:
            s += "6"
        elif digit == [1,1,1,0,1,1]:
            s += "7"
        elif digit == [1,1,1,1,0,0]:
            s += "8"
        elif digit == [1,1,1,1,0,1]:
            s += "9"
        elif digit == [1,1,1,1,1,0]:
            s += "+"
        elif digit == [1,1,1,1,1,1]:
            s += "/"
        else:
            raise ValueError("Should not come here")
    return s
















if __name__ == "__main__":
    a=hexToBitArray("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
    s=bitArrayToBase64(a)
    if s == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t":
        print("All tests passed!")


