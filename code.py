
#1- Create a class named fastq
class fastq(object):
    seqHeader= "@" 
    seq= ["A", "T", "C", "G", "N"]
    plusline= "+"
    qual= "c"
    len(seq)=len(qual)
    
    def _init_(self, seqHeader, seq, plusline, qual):
        print(seqHeader, seq, plusline, qual)

#print(fastq.seqHeader)

#2- open compressed files
filepath= ""
 if filePath.endswith('.gz'):
            self._file = gzip.open(filePath)
        else:
            self._file = open(filePath, 'rU')
