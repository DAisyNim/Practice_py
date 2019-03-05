def re_sequence(seq):
	"""(str)->str
	replace T to A, A to T, G to C and C to G"""
	seq = seq.lower()
	seq = seq.replace('a','T')
	seq = seq.replace('t','A')
	seq = seq.replace('g','C')
	seq = seq.replace('c','G')
	return seq

print(re_sequence('AATTGCCGT'))
