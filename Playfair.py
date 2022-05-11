class Playfair:

    def __init__(self, plaintext, key):
        self.plaintext = plaintext
        self.key = key
        codeText = ''
        condingAlphabet = ''
        self.globall = ''

    def textFormation(self):
        a = str(self.plaintext)
        a = self.plaintext.upper()
        text = ''
        for i in range(len(a)):
            if a[i] == 'Ä':
                text = text + 'AE'
            elif a[i] == 'Ö':
                text = text + 'OE'
            elif a[i] == 'Ü':
                text = text + 'UE'
            elif a[i] == 'ß':
                text = text + 'SZ'
            elif a[i] == '"':
                text = text + ''
            elif a[i] == "'":
                text = text + ''
            elif a[i] == ".":
                text = text + ''
            elif a[i] == " ":
                text = text + ''
            elif a[i] == "J":
                text = text + 'I'
            else:
                text = text + a[i]
        text2 = ''
        for e in range(len(text)-1):
            if text[e] == text[e+1]:
                # in case of double characters, note only the first one
                text2 = text2 + text[e] + "X"
            else:
                text2 = text2 + text[e]
        text2 = text2 + text[len(text)-1]
        if len(text2) % 2 == 1:
            text2 = text2 + "X"
        self.codeText = text2
        print(text2)

    def Alphabet(self):
        b = str(self.key)
        b = self.key.upper()
        text = ''
        keyalphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        # extended with the reason see below
        b += keyalphabet
        for i in range(len(b)):
            if b[i] == 'Ä':
                text = text + 'AE'
            elif b[i] == 'Ö':
                text = text + 'OE'
            elif b[i] == 'Ü':
                text = text + 'UE'
            elif b[i] == 'ß':
                text = text + 'SZ'
            elif b[i] == '"':
                text = text + ''
            elif b[i] == "'":
                text = text + ''
            elif b[i] == ".":
                text = text + ''
            elif b[i] == " ":
                text = text + ''
            elif b[i] == "J":
                text = text + 'I'
            else:
                text = text + b[i]
        text3 = ''
        keytextneu = ''
        for e in range(len(text)):
            if text3.find(text[e]) == -1:
                text3 = text3 + text[e]
        self.condingAlphabet = text3
        print(text3)
