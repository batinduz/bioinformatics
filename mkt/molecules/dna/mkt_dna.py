class DNA:
    complementLetters = {'A': 'T', 'G': 'C'}

    def __init__(self, seq):
        self.__seq = seq

    def seq(self):
        return self.__seq

    def transcription(self):
        return self.__seq.replace('T', 'U')

    def replication(self):
        return self

    def complement(self):
        letters = list(self.__seq)
        letters = [self.complementLetters[base] for base in letters]
        return ''.join(letters)
