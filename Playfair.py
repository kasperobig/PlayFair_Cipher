class Playfair:

    def __init__(self, plaintext, key):
        self.plaintext = plaintext
        self.key = key
        codeText = ''
        condingAlphabet = ''
        self.globall = ''

     def textformation(self):
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