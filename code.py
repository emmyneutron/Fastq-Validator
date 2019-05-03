
#1- Create a class named fastq
class SeqRead:
    def __init__(self, seqheader, seq, plusline, qual):
        self.id = seqheader
        self.seq = seq
        self.plus = plus
        self.qual = qual
        
    #len(seq)=len(qual)
    
 

#2- open compressed files
filepath= ""
 if filePath.endswith('.gz'):
            self._file = gzip.open(filePath)
        else:
            self._file = open(filePath, 'rU')
