#dict for fasta
def parse_fasta_dict(sequence_file):
    fasta_dict = {}
    current_header = ""
    current_sequence = []

    with open(sequence_file) as file_handle:
        for line in file_handle:
            line = line.strip()

            if line.startswith(">"):
                if current_header:
                    fasta_dict[current_header] = "".join(current_sequence)

                current_header = line[1:]
                current_sequence = []
            else:
                current_sequence.append(line)

    if current_header:
        fasta_dict[current_header] = "".join(current_sequence)

    return fasta_dict
