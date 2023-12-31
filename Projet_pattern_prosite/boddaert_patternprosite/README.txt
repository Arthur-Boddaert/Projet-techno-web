The script pratt.py allows to check if a part of a sequence in a fasta file follows a prosite pattern determined from the sequences in a multifasta file.
For this purpose 3 class are used :
- Multifasta in multifasta.py
- MultipleAlignment in multiplealignment.py
- PrositePattern in prositepattern.py

The class Multifasta is used to extract sequences from a multifasta file into a dictionary.
The method sequences() displays the sequence dictionary.
The sequences in the file are aligned.

The class MultipleAlignment allows to read the sequences in a dictionary to display it in a string.
The method size() gives the number of sequences in the dictionary.
The method is_conserved() take in parameter the number of one position of the sequences and check if all the amino acids at this position are the same.
The method contains_indel() take in parameter the number of one sequence and check if this sequence contains indels.
The method letters() take in parameter the number of one position of the sequences and gives the one-letter code of the amino acids at that position 
(an indel counts as one letter).
It is possible to print the object MultipleAlignment and given the length of the sequences.

The class PrositePattern take an object MultipleAlignment and create the prosite pattern corresponding to the sequences of the multifasta file.
The method search() take in parameter the name of a file containing a sequence and check if the pattern can be find in the sequence. The an occurrence is find 
give the position and the match.

Parameters :
Mandatory and in this order :
1) Name of the multifasta file.
2) Name of the file containing the sequence to be compared with the pattern.

optionnal :
-t or --threshold_value ; int ; Changes the number of different amino acids accepted at a position before putting an 'x'.
			   	Default 4

How the program works :
The program pratt start by extract the sequences in a dictionary with Multifasta.sequences() then the program use MultipleAlignment to create an 
object MultipleAlignment from the dictionary. Finally create an object with the class PrositePattern and use the method search() to get the tuple.
The program use the tuple and the prosite pattern obtain with the class PrositePattern to return the string :
'Pattern {prosite_pattern} found at position {position} : {match}' if an occurrences is find else return 'Pattern {prositepattern} not found'.

Program launching :
Linux :
$ python3 pratt.py exemple2.fasta seq2.fasta -t 2
$ python3 pratt.py exemple2.fasta seq2.fasta
$ python3 pratt.py exemple2.fasta seq1.fasta -t 2
$ python3 pratt.py exemple1.fasta seq2.fasta
$ python3 pratt.py exemple1.fasta seq1.fasta -t 5

Windows :
> python.exe pratt.py exemple2.fasta seq2.fasta -t 2
> python.exe pratt.py exemple2.fasta seq2.fasta
> python.exe pratt.py exemple2.fasta seq1.fasta -t 5
> python.exe pratt.py exemple1.fasta seq2.fasta
> python.exe pratt.py exemple1.fasta seq1.fasta -t 2

seq files :
For these examples the seq.fasta files contain :
seq1.fasta
> seq1
CGGSKSAYPNGNLACATGSKCVKQNEYYSQCV

seq2.fasta
> seq2
YVCPFDGCNKKFAQSTNLKSHILT--HGYSG

Example :
$ python3 pratt.py exemple2.fasta seq2.fasta -t 2
Pattern C-x(2,4)-C-x-K-x(7)-[LV]-x(2)-H-x(3,5)-H found at position 2 : CPFDGCNKKFAQSTNLKSHILT--H

The pattern is obtained from the 4 sequences in the file exemple2.fasta
Then we can see an occurrence of the pattern at the second position of the sequence.
The position is given with the python count, here the two corresponds to the third position