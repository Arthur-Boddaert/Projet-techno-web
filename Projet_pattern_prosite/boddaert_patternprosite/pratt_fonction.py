from .multifasta import Multifasta
from .multiplealignment import MultipleAlignment
from .prositepattern import PrositePattern

def patternprosite(multifasta_file, sequence, seuil):
        multifasta = Multifasta(multifasta_file)
        multialignment = MultipleAlignment(multifasta)
        prositepattern = PrositePattern(multialignment, seuil)
        search_result = prositepattern.search(sequence)

        if search_result != None:
            pattern, occurence = prositepattern, f'Le pattern à été retrouvé à la position {search_result[0]} : {search_result[1]}'
        else:
            pattern, occurence = prositepattern, 'Le pattern n\'a pas été trouvé dans la sequence.'

        return pattern, occurence

def verif_conserv(multifasta_file):
    multifasta = Multifasta(multifasta_file)
    multialignment = MultipleAlignment(multifasta)
    not_conserved = []
    for i in range(len(multialignment)):
        if not multialignment.is_conserved(i):
            not_conserved.append(i)
    return not_conserved

def verif_indel(multifasta_file):
    multifasta = Multifasta(multifasta_file)
    multialignment = MultipleAlignment(multifasta)
    with_indel = []
    for i in range(multialignment.size()):
        if multialignment.contains_indel(i+1):
            with_indel.append(i)
    if len(with_indel) == 0:
        return None
    return with_indel

def info_rapide(multifasta_file):
    multifasta = Multifasta(multifasta_file)
    multialignment = MultipleAlignment(multifasta)
    nb_seq = multialignment.size()
    taille = len(multialignment)
    return nb_seq, taille