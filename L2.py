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


encodeOrDecodeFlag = input('Encode/decode? ')

if encodeOrDecodeFlag.upper() != 'ENCODE' and encodeOrDecodeFlag.upper() != 'DECODE':
    print('Expected ENCODE or DECODE value')
    exit(1)

text = input('Phrase to encode/decode: ');

key = input('Key to encode/decode: ')


if encodeOrDecodeFlag.upper() == 'ENCODE':
    encodedText = encode(text, key)
    print('Encoded text: "{}"'.format(encodedText))

elif encodeOrDecodeFlag.upper() == 'DECODE':
    decodedText = decode(text, key)
    print('Decoded text: "{}"'.format(decodedText))







