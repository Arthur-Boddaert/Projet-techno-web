class Multifasta :
    def __init__(self,file):
        """
        Extract in a dictionary the sequences in a multifasta file.

        Returns
        -------
        dict :
            dictionary of all sequences in the multifasta file in parameters
        """
        liste_seq = []
        seq = ''
        # read a multifasta file and extract the sequences in a list.
        with open(file) as fileIn:
            for lignelue in fileIn:
                if lignelue[0] != ">":
                    seq += lignelue
                else: # if lignelue[0] == ">":
                    if seq != '':
                        liste_seq.append(seq.strip())
                        seq = ''
                    else:
                        pass
            liste_seq.append(seq.strip())
        self.__seqs = liste_seq

    def sequences (self) :
        """
        Display dictionary with all the sequences in a multifasta file.

        Returns
        -------
        dict :
            dictionary of all sequences in the multifasta file in parameters
        """
        return (self.__seqs)