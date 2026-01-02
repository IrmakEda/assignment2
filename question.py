## Irmak Eda Aykan
###foxp2
import Bio
from Bio import SeqIO

#for printing the sequence identifiers
seq_file_path_foxp2 = "protein_seq_folder/foxp2.fasta"
seq_handle_foxp2 = SeqIO.parse(seq_file_path_foxp2, "fasta")

for seq_record in seq_handle_foxp2:
    print (seq_record.id)
    print (repr(seq_record.seq))
    print (len(seq_record))

#for converting the files to the genbank format
count = SeqIO.convert(seq_file_path_foxp2, "fasta", "foxp2.genbank", "genbank")
print ("Converted %i records" % count)

## Alperen Şen
###prion
import Bio
from Bio import SeqIO

#for printing the sequence identifiers
seq_file_path_prion = "protein_seq_folder/prion.fasta"
seq_handle_prion = SeqIO.parse(seq_file_path_prion, "fasta")

for seq_record in seq_handle_prion:
    print (seq_record.id)
    print (repr(seq_record.seq))
    print (len(seq_record))

#for converting the files to the genbank format
count = SeqIO.convert(seq_file_path_prion, "fasta", "prion.genbank", "genbank")
print ("Converted %i records" % count)



