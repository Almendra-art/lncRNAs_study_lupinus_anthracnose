#Script to generate tables.csv with pairs connections previous filtered by a quantil, to and relate with a treatment
#In this step you will have files with significant gene connections related to each treatment 
#This information could be useful as an atribute of edges in the final network

import pandas as pd

# Load the BIG_QUANTIL network file
big_network_file = "your_path/big_net_099.txt"
big_network_df = pd.read_csv(big_network_file, sep="\t")

# Load the putative gene connections file
putative_connections_file = "your_path/r_gene_pairs.txt" #replace with your gene pairs file
putative_df = pd.read_csv(putative_connections_file, sep="\t", header=None, names=["fromNode", "toNode"])

# Merge the BIG network with the putative connections to filter the network
merge_df = big_network_df.merge(putative_df, on=["fromNode", "toNode"])

# Save the merge network to a new file
merge_df.to_csv("your_path/bignet_r_099.txt", sep="\t", index=False)

# Load the putative gene connections file
putative_connections_file = "your_path/r24hpi_gene_pairs.txt"
putative_df = pd.read_csv(putative_connections_file, sep="\t", header=None, names=["fromNode", "toNode"])

# Merge the BIG network with the putative connections to filter the network
merge_df = big_network_df.merge(putative_df, on=["fromNode", "toNode"])

# Save the merge network to a new file
merge_df.to_csv("your_path/bignet_r24hpi_099.txt", sep="\t", index=False)

# Load the putative gene connections file
putative_connections_file = "your_path/r60hpi_gene_pairs.txt"
putative_df = pd.read_csv(putative_connections_file, sep="\t", header=None, names=["fromNode", "toNode"])

# Merge the BIG network with the putative connections to filter the network
merge_df = big_network_df.merge(putative_df, on=["fromNode", "toNode"])

# Save the merge network to a new file
merge_df.to_csv("your_path/bignet_r60hpi_099.txt", sep="\t", index=False)

# Load the putative gene connections file
putative_connections_file = "your_path/r84hpi_gene_pairs.txt"
putative_df = pd.read_csv(putative_connections_file, sep="\t", header=None, names=["fromNode", "toNode"])

# Merge the BIG network with the putative connections to filter the network
merge_df = big_network_df.merge(putative_df, on=["fromNode", "toNode"])

# Save the merge network to a new file
merge_df.to_csv("your_path/bignet_r84hpi_099.txt", sep="\t", index=False)

print("Done")
