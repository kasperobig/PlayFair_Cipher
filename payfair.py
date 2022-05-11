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

    def alphabet(self):
        b = str(self.key)
        b = self.key.upper()
        text = ''
        keyalphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        # erweitert mit der Begruendung s.u.
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

    def code(self):
        #codingtext = self.textformation.text2
        outputText = ''
        final = ''
        while len(self.codeText) != 0:
            erstebeide = self.codeText[0:2]
            pos1 = self.condingAlphabet.find(erstebeide[0])
            pos2 = self.condingAlphabet.find(erstebeide[1])
            self.codeText = self.codeText[2:]
            y1 = pos1 / 5
            x1 = pos1 % 5
            y2 = pos2 / 5
            x2 = pos2 % 5
            if y1 == y2:
                if x1 == 4:
                    x1 = 0
                else:
                    x1 += 1
                if x2 == 4:
                    x2 = 0
                else:
                    x2 += 1
                z1 = y1 * 5 + x1
                z2 = y2 * 5 + x2
            else:
                if x1 == x2:
                    if y1 == 4:
                        y1 = 0
                    else:
                        y1 += 1
                    if y2 == 4:
                        y2 = 0
                    else:
                        y2 += 1
                    z1 = y1 * 5 + x1
                    z2 = y2 * 5 + x2
                else:
                    z1 = 5 * y1 + x2
                    z2 = 5 * y2 + x1
            outputText = outputText + \
                self.condingAlphabet[z1]+self.condingAlphabet[z2]
            self.globall = outputText
        return "global:" + self.globall
