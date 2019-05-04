#1- Create a class named SeqRead
class SeqRead:
    def __init__(self, seqheader, seq, plusline, qual):
        self.id = seqheader
        self.seq = seq
        self.plus = plus
        self.qual = qual
        
    def read_gz(self): #open &read compressed file
        filepath= ""

        if filepath.endswith('.gz'):
            self._file = gzip.open(filepath)
        else:
            self._file = open(filepath, 'rU')

        self._currentLineNumber = 0

    def next(self):
        # Get Next Four Lines 
        elemList = []
        for i in range(4):
            line = self._file.readline()
            self._currentLineNumber += 1 ## increment file position
            if line:
                elemList.append(line.strip('\n'))
            else: 
                elemList.append(None)

    def qualine_errors(self):            
         if len(self.qual) == len(self.seq):
            print('valid read'.format(self.qual))
         else:
            print("Invalid read".format(self.qual))        
   
