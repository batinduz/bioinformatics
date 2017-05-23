class RNA:
    complementLetters = {'A': 'U', 'G': 'C'}

    def __init__(self, seq):
        self.__seq = seq

    def reverse_transcription(self):
        return self.__seq.replace('U', 'T')

    def reverse(self):
        letters = list(self.__seq)
        letters.reverse()
        return ''.join(letters)

    def complement(self):
        letters = list(self.__seq)
        letters = [self.complementLetters[base] for base in letters]
        return ''.join(letters)
