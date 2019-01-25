import extractor
import pytest


REFERENCE = 'ACGTCGATTCGCTAGCTTCGGGGGATAGATAGAGATATAGAGAT'


TESTS = [
    # No variants
    (REFERENCE,
     REFERENCE,
     [{'location': {'start': {'position':  0, 'type': 'point'},
                    'end':   {'position': 44, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    # Single variants

    ## Substitution: 7A>G
    (REFERENCE,
     'ACGTCGGTTCGCTAGCTTCGGGGGATAGATAGAGATATAGAGAT',
     [{'location': {'start': {'position': 0, 'type': 'point'},
                    'end':   {'position': 6, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 6, 'type': 'point'},
                    'end':   {'position': 7, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 6, 'type': 'point'},
                                    'end'  : {'position': 7, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position':  7, 'type': 'point'},
                    'end':   {'position': 44, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## Single nucleotide deletion: 7del
    (REFERENCE,
     'ACGTCGTTCGCTAGCTTCGGGGGATAGATAGAGATATAGAGAT',
     [{'location': {'start': {'position': 0, 'type': 'point'},
                    'end':   {'position': 6, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 6, 'type': 'point'},
                    'end':   {'position': 7, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 6, 'type': 'point'},
                                    'end'  : {'position': 6, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position':  7, 'type': 'point'},
                    'end':   {'position': 44, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## Multi nucleotide deletion: 7_8del
    (REFERENCE,
     'ACGTCGTCGCTAGCTTCGGGGGATAGATAGAGATATAGAGAT',
     [{'location': {'start': {'position': 0, 'type': 'point'},
                    'end':   {'position': 6, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 6, 'type': 'point'},
                    'end':   {'position': 8, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 6, 'type': 'point'},
                                    'end'  : {'position': 6, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position':  8, 'type': 'point'},
                    'end':   {'position': 44, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## Single nucleotide insertion: 6_7insC
    (REFERENCE,
     'ACGTCGCATTCGCTAGCTTCGGGGGATAGATAGAGATATAGAGAT',
     [{'location': {'start': {'position': 0, 'type': 'point'},
                    'end':   {'position': 6, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 6, 'type': 'point'},
                    'end':   {'position': 6, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 6, 'type': 'point'},
                                    'end'  : {'position': 7, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position':  6, 'type': 'point'},
                    'end':   {'position': 44, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## Multi nucleotide insertion: 6_7insCC
    (REFERENCE,
     'ACGTCGCCATTCGCTAGCTTCGGGGGATAGATAGAGATATAGAGAT',
     [{'location': {'start': {'position': 0, 'type': 'point'},
                    'end':   {'position': 6, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 6, 'type': 'point'},
                    'end':   {'position': 6, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 6, 'type': 'point'},
                                    'end'  : {'position': 8, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position':  6, 'type': 'point'},
                    'end':   {'position': 44, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## Inversion: 7_11inv
    (REFERENCE,
     'ACGTCGCGAATCTAGCTTCGGGGGATAGATAGAGATATAGAGAT',
     [{'location': {'start': {'position': 0, 'type': 'point'},
                    'end':   {'position': 6, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 6, 'type': 'point'},
                    'end':   {'position': 11, 'type': 'point'},
                    'type': 'range'},
       'type': 'inv'},
      {'location': {'start': {'position': 11, 'type': 'point'},
                    'end':   {'position': 44, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## Inversion: 6_7inv
    (REFERENCE,
     'ACGTCTCTTCGCTAGCTTCGGGGGATAGATAGAGATATAGAGAT',
     [{'location': {'start': {'position': 0, 'type': 'point'},
                    'end':   {'position': 5, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 5, 'type': 'point'},
                    'end':   {'position': 7, 'type': 'point'},
                    'type': 'range'},
       'type': 'inv'},
      {'location': {'start': {'position': 7, 'type': 'point'},
                    'end':   {'position': 44, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## Deletion/insertion 7delinsCC
    (REFERENCE,
     'ACGTCGCCTTCGCTAGCTTCGGGGGATAGATAGAGATATAGAGAT',
     [{'location': {'start': {'position': 0, 'type': 'point'},
                    'end':   {'position': 6, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 6, 'type': 'point'},
                    'end':   {'position': 7, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 6, 'type': 'point'},
                                    'end'  : {'position': 8, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position':  7, 'type': 'point'},
                    'end':   {'position': 44, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## Deletion/insertion 21_23delinsTTTT
    (REFERENCE,
     'ACGTCGATTCGCTAGCTTCGTTTTGATAGATAGAGATATAGAGAT',
     [{'location': {'start': {'position':  0, 'type': 'point'},
                    'end':   {'position': 20, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 20, 'type': 'point'},
                    'end':   {'position': 23, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                        'location': {'start': {'position': 20, 'type': 'point'},
                                     'end'  : {'position': 24, 'type': 'point'},
                        'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position': 23, 'type': 'point'},
                    'end':   {'position': 44, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## Deletion/insertion 7_8delinsTC
    (REFERENCE,
     'ACGTCGTCTCGCTAGCTTCGGGGGATAGATAGAGATATAGAGAT',
     [{'location': {'start': {'position': 0, 'type': 'point'},
                    'end':   {'position': 6, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 6, 'type': 'point'},
                    'end':   {'position': 8, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 6, 'type': 'point'},
                                    'end'  : {'position': 8, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position': 8, 'type': 'point'},
                    'end':   {'position': 44, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## Duplication (insertion) 7dup
    (REFERENCE,
     'ACGTCGAATTCGCTAGCTTCGGGGGATAGATAGAGATATAGAGAT',
     [{'location': {'start': {'position': 0, 'type': 'point'},
                    'end':   {'position': 7, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 7, 'type': 'point'},
                    'end':   {'position': 7, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 7, 'type': 'point'},
                                    'end'  : {'position': 8, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position':  7, 'type': 'point'},
                    'end':   {'position': 44, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## Duplication (insertion) 6_7dup
    (REFERENCE,
     'ACGTCGAGATTCGCTAGCTTCGGGGGATAGATAGAGATATAGAGAT',
     [{'location': {'start': {'position': 0, 'type': 'point'},
                    'end':   {'position': 7, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 7, 'type': 'point'},
                    'end':   {'position': 7, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 7, 'type': 'point'},
                                    'end'  : {'position': 9, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position':  7, 'type': 'point'},
                    'end':   {'position': 44, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## Duplication (insertion) 5_7dup
    (REFERENCE,
     'ACGTCGACGATTCGCTAGCTTCGGGGGATAGATAGAGATATAGAGAT',
     [{'location': {'start': {'position': 0, 'type': 'point'},
                    'end':   {'position': 7, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 7, 'type': 'point'},
                    'end':   {'position': 7, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position':  7, 'type': 'point'},
                                    'end'  : {'position': 10, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position':  7, 'type': 'point'},
                    'end':   {'position': 44, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),


    # Multiple variants

    ## [5_6insTT;17del;26A>C;35dup]
    ('ATGATGATCAGATACAGTGTGATACAGGTAGTTAGACAA',
     'ATGATTTGATCAGATACATGTGATACCGGTAGTTAGGACAA',
     [{'location': {'start': {'position': 0, 'type': 'point'},
                    'end':   {'position': 5, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 5, 'type': 'point'},
                    'end':   {'position': 5, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 5, 'type': 'point'},
                                    'end'  : {'position': 7, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position':  5, 'type': 'point'},
                    'end':   {'position': 16, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 16, 'type': 'point'},
                    'end':   {'position': 17, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 18, 'type': 'point'},
                                    'end'  : {'position': 18, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position': 17, 'type': 'point'},
                    'end':   {'position': 25, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 25, 'type': 'point'},
                    'end':   {'position': 26, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 26, 'type': 'point'},
                                    'end'  : {'position': 27, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position': 26, 'type': 'point'},
                    'end':   {'position': 34, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 34, 'type': 'point'},
                    'end':   {'position': 34, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 35, 'type': 'point'},
                                    'end'  : {'position': 36, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position': 34, 'type': 'point'},
                    'end':   {'position': 39, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## [26A>C;30C>A;35G>C]
    ('TAAGCACCAGGAGTCCATGAAGAAGATGGCTCCTGCCATGGAATCCCCTACTCTACTGTG',
     'TAAGCACCAGGAGTCCATGAAGAAGCTGGATCCTCCCATGGAATCCCCTACTCTACTGTG',
     [{'location': {'start': {'position':  0, 'type': 'point'},
                    'end':   {'position': 25, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 25, 'type': 'point'},
                    'end':   {'position': 26, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 25, 'type': 'point'},
                                    'end'  : {'position': 26, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position': 26, 'type': 'point'},
                    'end':   {'position': 29, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 29, 'type': 'point'},
                    'end':   {'position': 30, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 29, 'type': 'point'},
                                    'end'  : {'position': 30, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position': 30, 'type': 'point'},
                    'end':   {'position': 34, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 34, 'type': 'point'},
                    'end':   {'position': 35, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 34, 'type': 'point'},
                                    'end'  : {'position': 35, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position': 35, 'type': 'point'},
                    'end':   {'position': 60, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## [26_29inv;30C>G]
    ('TAAGCACCAGGAGTCCATGAAGAAGATGGCTCCTGCCATGGAATCCCCTACTCTA',
     'TAAGCACCAGGAGTCCATGAAGAAGCCATGTCCTGCCATGGAATCCCCTACTCTA',
     [{'location': {'start': {'position':  0, 'type': 'point'},
                    'end':   {'position': 25, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 25, 'type': 'point'},
                    'end':   {'position': 29, 'type': 'point'},
                    'type': 'range'},
       'type': 'inv'},
      {'location': {'start': {'position': 29, 'type': 'point'},
                    'end':   {'position': 30, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 29, 'type': 'point'},
                                    'end'  : {'position': 30, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position': 30, 'type': 'point'},
                    'end':   {'position': 55, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## [26_29inv;30C>G;41del]
    ('TAAGCACCAGGAGTCCATGAAGAAGATGGCTCCTGCCATGGAATCCCCTACTCTA',
     'TAAGCACCAGGAGTCCATGAAGAAGCCATGTCCTGCCATGAATCCCCTACTCTA',
     [{'location': {'start': {'position':  0, 'type': 'point'},
                    'end':   {'position': 25, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 25, 'type': 'point'},
                    'end':   {'position': 29, 'type': 'point'},
                    'type': 'range'},
       'type': 'inv'},
      {'location': {'start': {'position': 29, 'type': 'point'},
                    'end':   {'position': 30, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 29, 'type': 'point'},
                                    'end'  : {'position': 30, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position': 30, 'type': 'point'},
                    'end':   {'position': 39, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 39, 'type': 'point'},
                    'end':   {'position': 40, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 39, 'type': 'point'},
                                    'end'  : {'position': 39, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position': 40, 'type': 'point'},
                    'end':   {'position': 55, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    # Transpositions

    ## Transpostion 37_38ins15_24
    ('ATGGCGGCGGTGGTCGCCCTCTCCTTGAGGCGCCGGTTGCCGGCCACAACCCTTGGCGGA',
     'ATGGCGGCGGTGGTCGCCCTCTCCTTGAGGCGCCGGTCGCCCTCTCCTGCCGGCCACAACCCTTGGCGGA',
     [{'location': {'start': {'position':  0, 'type': 'point'},
                    'end':   {'position': 37, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 37, 'type': 'point'},
                    'end':   {'position': 37, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'reference',
                       'location': {'start': {'position': 14, 'type': 'point'},
                                    'end'  : {'position': 24, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position': 37, 'type': 'point'},
                    'end':   {'position': 60, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## Transposition of reverse complement 37_38ins3_26inv
    ('ATGGCGGCGGTGGTCGCCCTCTCCTTGAGGCGCCGGTTGCCGGCCACAACCCTTGGCGGA',
     'ATGGCGGCGGTGGTCGCCCTCTCCTTGAGGCGCCGGTAAGGAGAGGGCGACCACCGCCGCCTGCCGGCCACAACCCTTGGCGGA',
     [{'location': {'start': {'position':  0, 'type': 'point'},
                    'end':   {'position': 37, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 37, 'type': 'point'},
                    'end':   {'position': 37, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'reference',
                       'inverted': 'true',
                       'location': {'start': {'position':  2, 'type': 'point'},
                                    'end'  : {'position': 26, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position': 37, 'type': 'point'},
                    'end':   {'position': 60, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    ## Duplication 18_42dup
    ('ATGGCGGCGGTGGTCGCCCTCTCCTTGAGGCGCCGGTTGCCGGCCACAACCCTTGGCGGA',
     'ATGGCGGCGGTGGTCGCCCTCTCCTTGAGGCGCCGGTTGCCGCCTCTCCTTGAGGCGCCGGTTGCCGGCCACAACCCTTGGCGGA',
     [{'location': {'start': {'position':  0, 'type': 'point'},
                    'end':   {'position': 42, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 42, 'type': 'point'},
                    'end':   {'position': 42, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'reference',
                       'location': {'start': {'position': 17, 'type': 'point'},
                                    'end'  : {'position': 42, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position': 42, 'type': 'point'},
                    'end':   {'position': 60, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

    # Compound transpositions

    # 42_43ins[CA;19_42]
    ('ATGGCGGCGGTGGTCGCCCTCTCCTTGAGGCGCCGGTTGCCGGCCACAACCCTTGGCGGA',
     'ATGGCGGCGGTGGTCGCCCTCTCCTTGAGGCGCCGGTTGCCGCACTCTCCTTGAGGCGCCGGTTGCCGGCCACAACCCTTGGCGGA',
     [{'location': {'start': {'position':  0, 'type': 'point'},
                    'end':   {'position': 42, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'},
      {'location': {'start': {'position': 42, 'type': 'point'},
                    'end':   {'position': 42, 'type': 'point'},
                    'type': 'range'},
       'insertions': [{'source': 'observed',
                       'location': {'start': {'position': 42, 'type': 'point'},
                                    'end'  : {'position': 44, 'type': 'point'},
                       'type': 'range'}},
                      {'source': 'reference',
                       'location': {'start': {'position': 18, 'type': 'point'},
                                    'end'  : {'position': 42, 'type': 'point'},
                       'type': 'range'}}],
       'type': 'delins'},
      {'location': {'start': {'position': 42, 'type': 'point'},
                    'end':   {'position': 60, 'type': 'point'},
                    'type': 'range'},
       'type': 'equal'}]),

]


@pytest.mark.parametrize('reference, observed, variants', TESTS)
def test_variants(reference, observed, variants):
    assert variants == extractor.describe_dna(reference, observed)
