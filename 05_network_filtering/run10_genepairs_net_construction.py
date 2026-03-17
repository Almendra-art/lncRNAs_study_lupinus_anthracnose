#Note1: Before run, DELETE HEADERS of your gene list file generated in run09_coexp_data_filter.ipynb, to avoid generate gene pairs with headers


def generate_gene_pairs(input_file, output_file):
    with open(input_file, 'r') as file:
        genes = [line.strip() for line in file.readlines()]

    pairs = []
    for gene1 in genes:
        for gene2 in genes:
            if gene1 != gene2:
                pairs.append(f"{gene1}\t{gene2}")

    with open(output_file, 'w') as file:
        for pair in pairs:
            file.write(pair + '\n')

# Specify the input and output files
input_file = 'your_path/your_gene_list.txt'  # Replace with your input file name
output_file = 'your_path/your_gene_pairs_output.txt'  # Replace with your desired output file name

# Generate the pairs
generate_gene_pairs(input_file, output_file)

print(f"Pairs generated and saved to {output_file}")


