import numpy as np

letters = [chr(ord('a') + letter) for letter in range(26)]\
          + [chr(ord('A') + letter) for letter in range(26)]\
          + [' ']


def index(char):
    for i in range(len(letters)):
        if letters[i] == char:
            return i
    return -1


def encode(stringToEncode, key):
    N = len(stringToEncode)
    M = len(key)
    result = list()
    for i in range(N):
        inputIndex = index(stringToEncode[i])
        keyIndex = index(key[i % M])
        newIndex = inputIndex + keyIndex

        while newIndex >= len(letters):
            newIndex -= len(letters)

        result.append(letters[newIndex])
    return ''.join(result)


def decode(stringToEncode, key):
    result = []
    N = len(stringToEncode)
    M = len(key)
    for i in range(N):
        inputIndex = index(stringToEncode[i])
        keyIndex = index(key[i % M])
        newIndex = inputIndex - keyIndex

        result.append(letters[newIndex])

    return ''.join(result)

text = 'World would run better if it runnaway'

key = 'John Siena'

encodedText = encode(text, key)

print('Encoded text: "{}"'.format(encodedText))

decodedText = decode(encodedText, key)

print('Decoded text: "{}"'.format(decodedText))