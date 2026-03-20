### Step 04 - Co-expression Analysis

#### `run08_WGCNA_coexpanalysis.ipynb`

**Input:** - `count_matrix_TMM.tsv` - `metadata.txt` - `binary_traits.tsv`

Example binary_traits.tsv:

| Sample  | Resistant | Susceptible | S_000hpi | S_024hpi | R_084hpi |
|---------|----------|-------------|----------|----------|----------|
| R_84hpi | 1        | 0           | 0        | 0        | 1        |

Where:
- 1 = sample belongs to the condition
- 0 = sample does not belong to the condition

**Output:** 
- Network files and plots
- Tables with relationships between modules and traits: ModuleTraitCorrelation.tsv, genes and modules: geneModuleMembership.csv, PvalueModuleMembership.csv
- Tables with relationships between genes and traits: geneTraitSignificance_resistant.csv and GeneSignificancePvalue_resistant.csv
- BigNet output: bigNet_edges.txt and bigNet_nodes.txt files, is the necessary information of relationships between all genes.  


