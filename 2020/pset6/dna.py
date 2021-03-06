import sys
import pandas as pd

# check for the correct number CL arguments
if len(sys.argv) != 3:
	print("Usage: python dna.py data.csv sequence.txt")
	exit()

# fetching the csv and txt filepaths
[csvpath, seqpath] = sys.argv[1:]

# reading from the csv and txt and storing them in variables
df = pd.read_csv(csvpath)
seq = ""
with open(seqpath, "r") as f:
	for line in f:
		seq += line

# getting each of the csv headers (the STRs) except the 0th one (the name of person)	
strs = [st for st in df][1:]

# initializing output to a "No match"
name = "No match"

# iterating through each csvrow
for index, row in df.iterrows():
	
	# checking if each STR appears in txt at minimum
	if False not in [st * int(row[[st]]) in seq for st in strs]:

		# checking for presence of any extra repetitions
		truth = []
		for st in strs:
			truth.append(seq[seq.find(st * int(row[st])) + len(st * (int(row[st]))):][:len(st)] == st)

		if True not in truth:
			name = row["name"]

print(name)
