from .multiplealignment import MultipleAlignment
import re

class PrositePattern :

    __TRANSLATE = {'-': '', 'x': '.', '(': '{', ')': '}'}

    def __init__(self, multiple_alignment, val) :
        self.__word = self.__template_pattern(multiple_alignment, val)
        self.__pattern = self.__pattern(self.__word)

    def __template_pattern (self, multiple_alignment, val) :
        """
        Gives a dictionary summarising the prosite pattern for each position

        Parameters
        ----------
        multiple_alignment :
            An object of type MultipleAlignment

        val : int
            maximum value of the number of amino acids per position

        Returns
        -------
        dict :
            A dictionary summarising the prosite pattern
        """
        word = []
        i = 0
        while i < multiple_alignment.__len__(): # for each position
            letters = multiple_alignment.letters(i + 1)
            if '-' not in letters: # if no indel
                if len(letters) == 1: # if one amino acid add it
                    word.append(letters[0])
                elif len(letters) <= val: # if several amino acids but less than val will add them
                    word.append(self.__write_frame(letters))
                elif len(letters) > val: # if several amino acids but more than val will add x
                    word.append('x')
                i += 1
            else:  # '-' in letters : = inel
                min = multiple_alignment.indel_min(i)
                max = multiple_alignment.indel_max(i)
                word.append(f'{min},{max}') # add the indel with min and max values
                i += max
        return word

    def __write_frame (self, letters) :
        """
        Prepare strings when there are multiple amino acids

        Parameters
        ----------
        letters : dict
            The letters corresponding to the amino acids for a position

        Returns
        -------
        str :
            The string containing the amino acid letters formatted for output

        """
        out = '['+''.join(letters)+']'
        return out

    def __pattern(self, pattern_dictio):
        """
        Prepare the prosite pattern

        Parameters
        ----------
        pattern_dictio : dict
            Dictionary summarising the prosite pattern for each position

        Returns
        -------
        str :
            The pattern in prosite format
        """
        pattern = ''
        min = 0
        max = 0
        nb_x = 0
        for i in pattern_dictio: # compare each position
            if ',' in i:  # an indel
                number = i.split(',')
                min += int(number[0])
                max += int(number[1])
            else:  # not an indel
                if i == 'x':
                    nb_x += 1
                elif i != 'x' :
                    if nb_x > 1: # add the current i to the pattern with the previous x or indel
                        if self.__min_or_max_not_null(min, max): # if min != 0 or max != 0 :
                            pattern += self.__write_indel(min, max, nb_x, i)
                        else: # if min == 0 or max == 0 :
                            pattern += f'-x({nb_x})-{i}'
                    elif nb_x > 0:
                        if self.__min_or_max_not_null(min, max):
                            pattern += self.__write_indel(min, max, nb_x, i)
                        else:
                            pattern += f'-x-{i}'
                    elif nb_x == 0:
                        if self.__min_or_max_not_null(min, max):
                            pattern += self.__write_indel(min, max, nb_x, i)
                        else:
                            pattern += f'-{i}'
                    min = 0 # reset min, max, nb_x
                    max = 0
                    nb_x = 0
        if max != 0: # add the last part of the pattern
            pattern += f'-x({min + nb_x},{max + nb_x})'
        elif nb_x != 0:
            pattern += '-x'
        return pattern[1:len(pattern)]

    def __min_or_max_not_null (self, min, max) :
        """
        Check if there are any indel

        Parameters
        ----------
        min : int
            Minimum number of amino acids in a part of a sequence containing indels
        max : int
            Maximum number of consecutive indels

        Returns
        -------
        bool :

        """
        return (min != 0 or max != 0)

    def __write_indel (self, min, max, nb_x, str_to_add) :
        """
        Prepare the pattern string for the indel

        Parameters
        ----------
        min : int
        Minimum number of amino acids in a part of a sequence containing indels
        max : int
            Maximum number of consecutive indels
        nb_x : int
            The count of x
        str_to_add : str
            Part of the pattern to be added

        Returns
        -------
        str :
            The character string for indel
        """
        min = min + nb_x
        max = max + nb_x
        return ( f'-x({min},{max})-{str_to_add}')

    def __str__(self):
        """
        Return the prosite pattern

        Returns
        -------
        str :
            The pattern in prosite format
        """
        return self.__pattern

    def __re (self, pattern, target) :
        """
        Use re to search for a pattern in a sequence

        Parameters
        ----------
        pattern : str
            The pattern to find
        target : str
            The sequence in which the research will take place

        Returns
        -------
        re.Match :
            The span and the match in the sequence
        """
        return re.search(pattern, target)

    def __prosite_to_re (self, pattern_prosite) :
        """
        Change the prosite pattern into a pattern accepted by re

        Parameters
        ----------
        pattern_prosite : str
            A pattern in prosite format

        Returns
        -------
        str :
            The pattern adapted to re
        """
        pattern_prosite_str = str(pattern_prosite)
        pattern_re = ''
        for i in pattern_prosite_str : # Change the character if necessary and add in the string
            if i in self.__TRANSLATE :
                pattern_re += self.__TRANSLATE[i]
            else :
                pattern_re += i

        return pattern_re

    def search (self, target) :
        """
        Search for the pattern in a sequence

        Parameters
        ----------
        target : str
            The sequence in which the research will take place

        Returns
        -------
        tuple :
            The tuple with the match position and the sequence corresponding to the match
        """
        seq = self.__read_fasta(target)
        pattern = self.__prosite_to_re(self.__pattern)
        find = self.__re(pattern, seq)
        if find != None : # compares the result of re
            string_to_cut = str(find) # take the necessary element for the tuple
            posi_and_match = string_to_cut.split('=')
            posi = str(posi_and_match[1]).split(',')[0]
            posi = posi.split('(')[1]
            start = int(posi)
            match = posi_and_match[2][1:-2]
            return (start, match)
        else :
            return None

    def __read_fasta (self, file) :
        """
        Extract a sequence in FASTA file.

        Parameters
        ----------
        file : string
            name of the file with .fasta

        Returns
        -------
        string
            the sequence contain in the file
        """
        seq = ''
        # We need to pass the line who start by > and put the rest in 'seq'.
        with open(file) as fileIn:
            fileIn.readline()
            for ligne_lue in fileIn:
                seq += ligne_lue.rstrip()
        return seq