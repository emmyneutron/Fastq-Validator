
#1- Create a class named SeqRead
class SeqRead:
    def __init__(self, seqheader, seq, plusline, qual):
        self.id = seqheader
        self.seq = seq
        self.plus = plus
        self.qual = qual
        
     def qualine_errors(self):
         if len(self.qual) == len(self.seq):
            print('valid read'.format(self.qual))
        else:
            print("Invalid read".format(self.qual))
    
 

#2- open compressed files
filepath= ""
 if filePath.endswith('.gz'):
            self._file = gzip.open(filePath)
        else:
            self._file = open(filePath, 'rU')
