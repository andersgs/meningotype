import unittest
from pkg_resources import resource_filename
import os
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import meningotype

from meningotype import meningotype

DBpath = resource_filename('meningotype', 'db')
porA1DB = os.path.join( DBpath, 'blast', 'porA1' )
porA2DB = os.path.join( DBpath, 'blast', 'porA2' )

porA_string = '''
ACCGCCCTCGTATTGTCCGCACTGCCGCTTGCGGCCGTTGCCGATGTCAGCCTGTACGGC
GAAATCAAAGCCGGCGTGGAAGGCAGGAACTACCAGCTGCAATTGACTGAAGCACAAGCC
GCTAACGGTGGAGCGAGCGGTCAGGTAAAAGTTACTAAAGTTACTAAGGCCAAAAGCCGC
ATCAGGACGAAAATCAGTGATTTCGGCTCGTTTATCGGCTTTAAGGGGAGTGAGGATTTG
GGCGAAGGGCTGAAGGCTGTTTGGCAGCTTGAGCAAGACGTATCCGTTGCCGGCGGCGGC
GCGACCCAGTGGGGCAACAGGGAATCCTTTATCGGCTTGGCAGGCGAATTCGGTACGCTG
CGCGCCGGTCGCGTTGCGAATCAGTTTGACGATGCCAGCCAAGCCATTGATCCTTGGGAC
AGCAACAATGATGTGGCTTCGCAATTGGGTATTTTCAAACGCCACGACGATATGCCGGTT
TCCGTACGCTACGACTCTCCGGAATTTTCCGGTTTTAGCGGCAGCGTCCAATTCGTTCCG
GCTCAAAACAGCAAGTCCGCCTATACGCCGGCTCATTATACTACTGTGTATAATGCTACT
ACTACTACTACTACTTTCGTTCCGGCTGTTGTCGGCAAGCCCGGATCGGATGTGTATTAT
GCCGGTCTGAATTAC
'''

porA_string = porA_string.replace('\n', '')
sid = 'porA'
seq = Seq(porA_string)
seq = SeqRecord(seq)
seq.id = sid

class TestFetABLASTX(unittest.TestCase):

    res_A1 = meningotype.finetypeBLAST(seq, porA1DB)
    res_A2 = meningotype.finetypeBLAST(seq, porA2DB)

    def test_porA1(self):
        self.assertEqual(self.res_A1, "7")

    def test_porA2(self):
        self.assertEqual(self.res_A2, "30")

if __name__ == '__main__':
    unittest.main()
