import re
# Create a class named SeqRead
class SeqRead:
    # Initiate object in this class with its attributes
    def __init__(self, read_id, seq, plus, qualit):
        self.id = read_id
        self.seq = seq
        self.plus = plus
        self.quality = qualit

# specify the path of your file
file_path = r'E:\Bioinformatics_diploma\missing_plus_single.fq'

# open &read compressed file
def read_gz(self):  
    filepath = ""

    if filepath.endswith('.gz'):
        self._file = gzip.open(filepath)
    else:
        self._file = open(filepath, 'r')

# counter to terminate reading from the file
counter = 1
# create a list to put reads from the file (i.e.list of SeqRead objects)
reads = []
# Open the file with keyword 'with', with open let file to be closed after iteration
with open(file_path)as f, open("report.txt", 'w') as report::
    # A loop that reads each 4 lines in the file as read object and puts them in a list of read objects
    while True:
        lines = []
        for i in range(4):
            lines.append(next(f))   # next brings the upcoming line
            counter += 1
        # Create a read object named SeqRead
        reads.append(SeqRead(read_id=lines[0], seq=lines[1], plus=lines[2], qualit=lines[3]))
        if counter >= 30:
            break

#start analysis with checking header line starts with "@"
        def header_control(self):
            if self.seqheader.startswith('@'):
                report.write('valid read'.format(self.seqheader))
            else:
                report.write('invalid read'.format(self.seqheader))
                
#checking sequence line if it contains any other character other than  "ATCGNatcgn"
         def seq_errors(self):
            if re.match(r'[ATCGNatcgn]+$', self.seq) and len(self.seq) >= 36:
                report.write('valid read'.format(self.seq))
            else:
                report.write('Invalid read'.format(self.seq))
                
#checking plus line if it contains + or not
        def no_plus(self):
            if self.plus == '+':
                report.write('valid read'.format(self.plus))
            else:
               report.write("Invalid read".format(self.plus))
#checking quality line if its length of characters  = length of seuence line 
         def qualine_errors(self):
            if len(self.quality) == len(self.seq):
                report.write('valid read'.format(self.quality))
            else:
                report.write("Invalid read".format(self.quality))
print(reads)
SeqRead.header_control()
SeqRead.seq_errors()
SeqRead.no_plus()
SeqRead.qualine_errors()
