# Fastq-Validator
OVERVIEW
``` java
The purpose of the program is to validate the format of fastq files.
A fastq file normally uses four lines per sequence.
● Line 1 begins with a '@' character and is followed by a sequence identifier
and an optional description .
● Line 2 is the raw sequence letters.
● Line 3 begins with a '+' character and is optionally followed by the same
sequence identifier (and any description) again.
● Line 4 encodes the quality values for the sequence in Line 2, and must
contain the same number of symbols as letters in the sequence.
Example:
@SEQ_ID
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT
+
!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65
```
