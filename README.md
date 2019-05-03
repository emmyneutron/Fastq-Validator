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
INPUTS
``` java
1. Path containing fastq file(s) to be validated.
2. Minimum length accepted for sequences - default 36.
```
OUTPUTS
``` java
Generate a text file report for each fastq file to be validated. The name of the file
should be the same as fastq file + .report
• In the report the following information should be presented:
a. Total number of reads in the file.
b. Min, max, and average read length.
c. List of errors including the read_id (if exists) and the line number
of the error.
```
SUBTASKS
``` java
1-Download fastq dataset from SRA or Array Express databases to use our input
data
2-Since fastq files are large in size we will use the keyword “with” to open the
file
3- Our aim is to take each four lines of the fastq file as one read object and put
them in a list of read objects (a dictionary, a list, or an array (NumPy)
might be used to achieve this purpose)
4- Create a class named “sequence read” and in it initiate an object with the
attributes ‘read id’, ‘sequence (to be identified as a string of no less than
36 characters containing the letters ACGTN/acgtn), “+” sign and ‘quality
score’.
5- Then a for loop containing an if condition to be created in order to go through
each line to perform the following:
- Check lines for the expected form i.e. if the four lines of a read match the
objects in our class.
- Check Sequence Identifier line starts with an '@' followed by a
sequence identifier
- Check third line has ‘+’ sign
- Check for the quality score line characters
6- Make sure the quality score line length exceeds minimum accepted sequence
length (36) characters.
7- Make sure the sequence and quality score lines have equal lengths.
8- Use Scipy package in order to calculate the minimum, maximum, and average
read length.
9- Create an empty list that contains all the outputs to be put into a file (report)
10- Program validation through comparing it with the already established tool,
e.g. FASTQValidator https://genome.sph.umich.edu/wiki/FastQValidator.
```
EXPECTED DIFFICULTIES
``` java
- Fastq file large size and PCs’ limited computational powers
- Reading each four lines as one read
- For Loops
- Dictionaries
- Detecting the errors in each line of the reads.
```
