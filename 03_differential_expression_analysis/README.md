
### Step 03 - Differential Expression Analysis

#### `run06_featurecounts.sh`
##### Create the count matrix to downstream analysis.

**Input:** - `.bam`

**Output:** - `count_matrix.tsv`

------------------------------------------------------------------------

#### `run07_EdgeR_DESEQ2_DEanalysis.ipynb`
##### This notebook includes the instructions to run both tools. Genes reported as differential expressed for both were selected for further investigation. 

**Input:** - `count_matrix.tsv` - `metadata.txt`

Example metadata.txt:

sample  hpi genotype    biosample   response    tissue  treatment 
C195_60H_1  060HPI  C195    R1  Susceptible hypocotyl   C195_060HPI

**Output:** - normalized count_matrix.tsv, DE genes: contrast 1 infection-associated and contrast 2 genotype-associated, PCA, heatmaps

------------------------------------------------------------------------
