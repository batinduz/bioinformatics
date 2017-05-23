from mkt_dna import DNA


seq = 'ATGTTCCCCAGTTGCAAAATTTCG'
dna = DNA(seq)
print ("Seq: ")
print (seq)
replica = dna.replication()

print ("Replication: ")
print (replica.seq())
print ("Transcription: ")

print (dna.transcription())