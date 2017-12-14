#!/usr/bin/env python2

from Bio import SeqIO
from Bio.Seq import Seq
import sys


seq=[]
tabs=[]
new=''
with open(sys.argv[1], 'rU') as phile:
	for record in list(SeqIO.parse(phile, "fasta")):
		seq.append(record.seq)
		print(record.seq)
		print('test')
#	for i in range(len(seq)):
#		for m in range(len(record.seq)):
#			new+= seq[i][m]
#			print(new)
#		print('asdasaadadsd')
#		tabs.append(new)
#		new=''
#	print(tabs)

