"""
Program Description: This program takes a given DNA sequence translates it to a protein sequence.

Author: [Andrew Dana]
"""

import helper 


# dna_sequence = input('Please enter the DNA sequence: ')
def transcription(dna_sequence):
    dna =  dna_sequence.replace('T', 'U')
    complement = ''

    for i in dna:
        if i == 'U':
            complement += 'A'
        elif i == 'A':
            complement += 'U'
        elif i == 'C':
            complement += 'G'
        elif i == 'G':
            complement += 'C'

    return complement

def translate(mrna):
    protein = ''

    triplet_list = helper.chunk(mrna, 3)
    for triplet in triplet_list:
        protein += helper.amino_acids[triplet] + ' '
    return protein


dna = 'TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT'

mrna = transcription(dna)

print(f'DNA sequence:\n{dna}')
print(f'RNA sequence:\n{mrna}')
print(f'Protein sequence:\n{translate(mrna)}')