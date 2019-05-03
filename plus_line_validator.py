
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


        def test_no_plus_char_on_third_line(self):
            if self.plus == '+':
                print('valid read'.format(self.plus))
            else:
                print("Invalid read".format(self.plus))






