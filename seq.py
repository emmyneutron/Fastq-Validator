import re
def seq_errors(self):
    if re.match(r'[ATCGNatcgn]+$', self.seq) and len(self.seq) >= 36:
        print('valid read'.format(self.seq))
    else:
        print('Invalid read'.format(self.seq))