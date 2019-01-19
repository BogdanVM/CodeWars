def DNA_strand(dna):
    genes = {"A": "T", "T": "A", "C": "G", "G": "C"}
    listDna = list(dna)
    for i in range(0, len(listDna)):
        listDna[i] = genes[dna[i]]
      
    return "".join(listDna)