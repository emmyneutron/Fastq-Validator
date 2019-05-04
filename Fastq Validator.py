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


def read_gz(self):  # open &read compressed file
    filepath = ""

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
        self._currentLineNumber += 1  ## increment file position
        if line:
            elemList.append(line.strip('\n'))
        else:
            elemList.append(None)

# counter to terminate reading from the file
counter = 1
# create a list to put reads from the file (i.e.list of SeqRead objects)
reads = []
# Open the file with keyword 'with'
with open(file_path)as f:
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


        def header_control(self):
            if self.seqheader.startswith('@')
                print('valid read'.format(self.seqheader))
            else:
                print('invalid read'.format(self.seqheader))


        def test_no_plus_char_on_third_line(self):
            if self.plus == '+':
                print('valid read'.format(self.plus))
            else:
                print("Invalid read".format(self.plus))


    def qualine_errors(self):
        if len(self.qual) == len(self.seq):
            print('valid read'.format(self.qual))
        else:
            print("Invalid read".format(self.qual))
