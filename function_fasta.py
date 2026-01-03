#Assignment2.2, write a function to parse a fasta document
def read_fasta_file(file_name):
    fileObj = open(file_name, "rU")
    sequences = []
    seq = ""
    for line in fileObj:
        if line.startswith(">"):
            if seq:
                sequences.append(seq)
        else:
            seq += line.rstrip()
    if seq:
        sequences.append(seq)
    fileObj.close()
    return sequences
