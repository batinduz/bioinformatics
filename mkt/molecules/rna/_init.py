from mkt_rna import RNA


seq = 'AUGGUCAGCUCAAGGCCGGAACCUU'
rna = RNA(seq)
print "Seq: "+ seq


print "Reverse Transcription: "+rna.reverse_transcription()