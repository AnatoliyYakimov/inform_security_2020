letters = [chr(ord('a') + letter) for letter in range(26)]\
          + [chr(ord('A') + letter) for letter in range(26)]\
          + [' ']


def index(char):
    for i in range(len(letters)):
        if letters[i] == char:
            return i
    return -1


def encode(stringToEncode, key, N):
    return [(index(m) ** key) % N for m in stringToEncode]


def decode(stringToDencode, key, N):
    return ''.join([letters[(c ** key) % N] for c in stringToDencode])


def getOpenKey(phi):
    e = 2
    for i in range(2, phi):
        if (phi % i == 0) and (e % i == 0):
            e += 1
    return e


def getCloseKey(e, mod):
    d = 1
    while True:
        f = (e * d) % mod
        if f == 1 and e != d:
            return d
        d += 1

P = 7
Q = 13

N = P * Q
f = (P - 1) * (Q - 1)

print("P = {}\nQ = {}\nN = {}\nf = {}\n".format(P, Q, N, f))

openKey = getOpenKey(f)

print("Open Key = {}".format(openKey))

closeKey = getCloseKey(openKey, f)

print("Close Key = {} ".format(closeKey))

text = 'World was on fire and no one can save me but you'

print(text)

encodedText = encode(text, closeKey, N)

print("Encoded text: %s" % encodedText)

decodedText = decode(encodedText, openKey, N)

print("Decoded text: %s" % decodedText)


