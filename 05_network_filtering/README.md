
### Step 05 - Network Filtering

##### These steps were performed to select genes significantly associated with a treatment, and the strongest co-expressions/connections (by quantils) between genes for data visualization.


#### `run09_coexp_data_filter.ipynb`

##### To select the module more significantly associated with every gene. 

**Input:** - `geneModuleMembership.csv` - `PvalueModuleMembership.csv` 

#### To select genes more associated with every trait.

**Input:** - `geneTraitSignificance_resistant.csv` - `GeneSignificancePvalue_resistant.csv ` 


**Output:** - `filtered_mm.tsv`

#### You obtain tables or lists of genes, with genes and their respective related modules (filtered_mm.tsv), and their treatment significantly associated. 
------------------------------------------------------------------------

#### `run10_genepairs_net_construction.py`

##### This step is to generate gene pairs from a list of genes, to then extract co-expression weights information.

**Input:** - `list_genes_of_interest.txt` 


**Output:** - `gene_list_pairs.txt`

------------------------------------------------------------------------

#### `run11_quantilnetwork_to_cytoscape.py`

##### Here we select the strongest connections among genes. 
**Input:** - `bigNet_edges.txt`

##### We filtered connections by quantils.

**Output:** - Filtered networks

------------------------------------------------------------------------

#### `run12_edges_attributes1_pairsxtrait.py`

##### Here we obtain the connection weights of our gene-pairs generated in Run10.

**Input:** - `filtered_network.txt` - `gene_list_pairs.txt`


**Output:** - Weighted gene pairs: bignet_075_resistant.txt

------------------------------------------------------------------------

#### `run13_edges_attributes2_to_cytoscape.ipynb`

##### Step to save one table of edges-attributes to cytoscape. 

**Input:** - `bignet_075_resistant.txt` - `bignet_075_resistant24hpi.txt` - `bignet_075_resistant60hpi.txt` - `bignet_075_resistant84hpi.txt` - pairs genes with weight info. 

**Output:** - `edges_attributes.tsv`

------------------------------------------------------------------------

#### `run14_nodes_attributes_to_cytoscape.ipynb`

##### Step to save one table of nodes-attributes to cytoscape. 

**Input:** - `filtered_mm.tsv ` - `genes_DE_run07.txt` - any list of genes attributes 

**Output:** - `node_attributes.tsv`

------------------------------------------------------------------------

#### `run15_annotation_nodes_of_interest.ipynb`

##### Step to add annotation information if you have.

**Input:** - `annotation_file.tsv ` - `list_nodes.txt` - `list_edges.txt`

**Output:** - `annotated_genes.tsv`'`annotated_genes.tsv`

