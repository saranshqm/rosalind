# Frequent Words with Mismatches and Reverse Complements Problem
#
# Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.
#
# Given: A DNA string Text as well as integers k and d.
#
# Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern) over all possible k-mers.

# Sample Dataset
#
# ACGTTGCATGTCGCATGATGCATGAGAGCT
# 4 1

# Sample Output
#
# ATGT ACAT


import inout 	# my module for handling Rosalind's file I/O
sequence = inout.infilelines[0].strip()
k, d = map(int, inout.infilelines[1].strip().split())

complement = { 'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
def reverse_complement(kmer):
	r = ''
	for base in kmer:
		r = complement[base] + r
	return r

def enumerate_mismatches (kmer, maxdist):
	if maxdist == 0:
		return [kmer]
	else:
		r = []
		for m_kmer in enumerate_mismatches(kmer, maxdist - 1):
			for loc in range(k):
				for base in ['A', 'C', 'G', 'T']:
					new_kmer = m_kmer[:loc] + base + m_kmer[loc + 1:]
					r.append(new_kmer)
		return set(r)

kmer_counts = {}
max_kmers = []
max_kmer_count = 0
for idx in range(len(sequence) - k + 1):
	kmer = sequence[idx:idx+k]
	m_kmers = list(enumerate_mismatches(kmer, d))
	m_kmers.extend(list(enumerate_mismatches(reverse_complement(kmer), d)))
	for m_kmer in m_kmers:
		if m_kmer in kmer_counts:
			count = kmer_counts[m_kmer] + 1
		else:
			count = 1
		kmer_counts[m_kmer] = count

		if count > max_kmer_count:
			max_kmer_count = count
			max_kmers = [m_kmer]
		elif count == max_kmer_count:
			max_kmers.append(m_kmer)

inout.output(' '.join(max_kmers))
