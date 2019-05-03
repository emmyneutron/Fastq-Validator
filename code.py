
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
    
 

#2- open and reading compressed files 
filepath= ""
 if filePath.endswith('.gz'):
            self._file = gzip.open(filePath)
        else:
            self._file = open(filePath, 'rU')
# counter to terminate reading from the file
counter = 1
# create a list to put reads from the file (i.e.list of SeqRead objects)
reads = []
# Open the file with keyword 'with'
with open(filepath)as f:
    # A loop that reads each 4 lines in the file as read object and puts them in a list of read objects
    while True:
        lines = []
        for i in range(4):
            lines.append(next(f))   # next brings the upcoming line
counter += 1
