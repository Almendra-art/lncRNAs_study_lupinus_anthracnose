###Choose your desire quantil

import pandas as pd

# Load the edges BIG network file generated in WGCNA analysis
big_network_file = "your_path/bigNet_edges.txt"
big_network_df = pd.read_csv(big_network_file, sep="\t")

# filter by quantil 

quant = big_network_df['weight'].quantile([0.75]).tolist()
big_quantil_filtered75 = big_network_df[big_network_df['weight'] >= quant[0]]

# Save the filtered network to a new file
big_quantil_filtered75.to_csv("your_path/big_net_075.txt", sep="\t", index=False)

# filter by quantil 

quant = big_network_df['weight'].quantile([0.80]).tolist()
big_quantil_filtered80 = big_network_df[big_network_df['weight'] >= quant[0]]

# Save the filtered network to a new file
big_quantil_filtered80.to_csv("your_path/big_net_080.txt", sep="\t", index=False)

# filter by quantil 

quant = big_network_df['weight'].quantile([0.90]).tolist()
big_quantil_filtered = big_network_df[big_network_df['weight'] >= quant[0]]

# Save the filtered network to a new file
big_quantil_filtered.to_csv("your_path/big_net_090.txt", sep="\t", index=False)

# filter by quantil 

quant = big_network_df['weight'].quantile([0.95]).tolist()
big_quantil_filtered = big_network_df[big_network_df['weight'] >= quant[0]]

# Save the filtered network to a new file
big_quantil_filtered.to_csv("your_path/big_net_095.txt", sep="\t", index=False)

# filter by quantil 

quant = big_network_df['weight'].quantile([0.99]).tolist()
big_quantil_filtered = big_network_df[big_network_df['weight'] >= quant[0]]

# Save the filtered network to a new file
big_quantil_filtered.to_csv("your_path/big_net_099.txt", sep="\t", index=False)

print("Done :D")
