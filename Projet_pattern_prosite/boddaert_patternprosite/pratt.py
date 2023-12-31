from multifasta import Multifasta
from multiplealignment import MultipleAlignment
from prositepattern import PrositePattern
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("multifasta_file", type=str, help="Your file with the sequences")
    parser.add_argument("sequence", type=str, help="Sequence in which we look for the pattern")
    parser.add_argument("-t", "--threshold_value", type=int, default= 4,
                        help="The threshold value for the number of different amino acids accepted for a position")
    args = parser.parse_args()

    multifasta = Multifasta(args.multifasta_file)
    multialignment = MultipleAlignment(multifasta)
    prositepattern = PrositePattern(multialignment,args.threshold_value)
    search_result = prositepattern.search(args.sequence)

    if search_result != None :
        out = f'Pattern {prositepattern} found at position {search_result[0]} : {search_result[1]}'
    else :
        out = f'Pattern {prositepattern} not found'

    print(out)