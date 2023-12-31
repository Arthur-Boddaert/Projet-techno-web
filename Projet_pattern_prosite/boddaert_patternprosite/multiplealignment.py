from .multifasta import Multifasta

class MultipleAlignment :
    def __init__(self, multi_fasta):
        string = ""
        for i in multi_fasta.sequences ():
            string += f"{i}\n"
        self.__align = string.rstrip()
        self.__dictionary = multi_fasta.sequences()

    def __str__(self):
        """
        Returns all sequences

        Returns
        -------
        str :
             All sequences
        """
        return (self.__align)

    def __len__(self):
        """
        Return the length of the sequences

        Returns
        -------
        int :
            Length of the sequences
        """
        return len(self.__dictionary[0])

    def size (self) :
        """
        Returns the number of sequences

        Returns
        -------
        int :
            Number of sequences
        """
        return len(self.__dictionary)

    def is_conserved (self, column) :
        """
        Checks if the amino acids of all sequences at one position are identical.

        Parameters
        ----------
        column : int
            Position in the sequences, start at 1.

        Returns
        -------
        bool :
            True if the amino acids are the same if not return False
        """
        comp = self.__dictionary[0][column-1]
        for i in self.__dictionary : # Compares the position of the sequence with the position of the previous sequence
            if i[column-1] != comp :
                return False
            else :
                comp = i[column-1]
        return True

    def contains_indel (self, row):
        """
        Checks if a sequence contains indels

        Parameters
        ----------
        row : int
            The number of the corresponding sequence in the multifasta file, start at 1.

        Returns
        -------
        bool :
            True if the sequence contain an indel or more if not return False
        """
        for i in self.__dictionary[row-1] : # Compare all positions to check if it is an indel
            if i == '-' :
                return True
        return False

    def letters (self,column):
        """
        Gives all possible amino acids to a position, including indel

        Parameters
        ----------
        column : int
            Position in the sequences, start at 1.

        Returns
        -------
        dict :
            The dictionary contains all possible amino acids at one position
        """
        letters = []
        for i in self.__dictionary: # Browse all positions
            caps = i.upper() #
            if caps[column-1] not in letters : # Add the new letters
                letters.append(caps[column-1])
        return (letters)

    def indel_min(self, column_start):
        """
        Gives the minimum number of amino acids in a part of a sequence containing indels

        Parameters
        ----------
        column_start : int
            Position from which the successive indels are counted

        Returns
        -------
        int :
            Minimum number of amino acids in a part of a sequence containing indels
        """
        indel_min = self.__len__()
        for i_row in range(self.size()):  # check sequence by sequence
            if self.contains_indel(i_row + 1):
                comp = self.__dictionary[i_row][column_start - 1: column_start + self.indel_max(column_start)]
                # defined the reading frame
                nb_letters = len(comp) - comp.count('-')
                if indel_min > (nb_letters):
                    indel_min = nb_letters - 1
                else:
                    pass
            else:
                pass
        return indel_min

    def indel_max(self, column_start):
        """
        Give the maximum number of consecutive indels

        Parameters
        ----------
        column_start : int
            Position from which the successive indels are counted

        Returns
        -------
        int :
            Maximum number of consecutive indels
        """
        indel_max = 0
        for i in range(column_start - 1, self.__len__()):  # Check the sequence from the given position
            if '-' in self.letters(i + 1):  # checks for the presence of indel
                indel_max += 1
            elif '-' not in self.letters(i + 1) and indel_max > 0:
                return indel_max
        return indel_max