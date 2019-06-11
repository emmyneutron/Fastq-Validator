import re
import sys

# Create a class named SeqRead
class SeqRead:
    # Initiate object in this class with its attributes
    def __init__(self, read_id, seq, plus, qualit):
        self.id = read_id
        self.seq = seq
        self.plus = plus
        self.quality = qualit
        
#start analysis with checking header line starts with "@"
    def header_control(self, report, line_no):
        if not self.id.startswith('@'):
            report.write('invalid header.{}\n'.format(line_no-3))
                
#checking sequence line if it contains any other character other than  "ATCGNatcgn"
    def seq_errors(self,report, line_no,min_len):
        if not re.match('[ATCGNatcgn]+$', self.seq) or len(self.seq) < min_len:
            report.write('Invalid seq.{}\n'.format(line_no-2))
                
#checking plus line if it contains + or not
    def no_plus(self,report, line_no):
        if self.plus != '+\n':
            report.write('Invalid plus_line.{}\n'.format(line_no-1))
            
#checking quality line if its length of characters  = length of sequence line 
    def qualine_errors(self,report, line_no):
        if len(self.quality) != len(self.seq):
            report.write('Invalid quality.{}\n'.format(line_no))
            
            
# open &read compressed file
def read_gz(file_path):  
    if file_path.endswith('.gz'):
        file = gzip.open(file_path)
    else:
        file = open(file_path, 'r')
    return file
        
# specify the path of your file

#input file 'fastq'
file_path = sys.argv[1]
min_len= int(sys.argv[2])

# Open the file with keyword 'with', with open let file to be closed after iteration
f= read_gz(file_path)
#report_file= sys.argv[2]
r_name = file_path + "report"

counter=0
with open(r_name, 'w') as report:
    # A loop that reads each 4 lines in the file as read object and puts them in a list of read objects
    while True:
        lines = []
        for i in range(4):
            line= f.readline()
            lines.append(line)  
            counter +=1 
        if not line:
            break
        # Create a read object named SeqRead
        read= SeqRead(read_id=lines[0], seq=lines[1], plus=lines[2], qualit=lines[3])
        read.header_control(report,counter)
        read.seq_errors(report,counter,min_len)
        read.no_plus(report,counter)
        read.qualine_errors(report,counter)
f.close()
