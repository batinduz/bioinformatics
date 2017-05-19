class Alphabet:
    def __init__(self, seq):
        self.__seq = seq

    def kmer(self, value):
        seq = self.__seq
        end = len(seq) - (len(seq) % value) - 1
        kmers = [seq[i:i + value] for i in range(0, end, value)]
        return kmers
