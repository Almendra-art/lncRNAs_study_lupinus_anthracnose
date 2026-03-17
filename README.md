# lncRNA identification and Co-expression analyses

## Overview

This repository provides a complete computational framework to identify
lncRNAs and putative regulatory interactions between lncRNAs and
protein-coding genes by integrating:

-   Two lncRNA prediction tools (FEELnc and CPC2) to increase confidence
    in results
-   Two differential expression analysis tools (DESeq2 and edgeR)
-   Co-expression network analysis (WGCNA)
  

![Pipeline diagram](docs/esquema_solo.png)
------------------------------------------------------------------------

## Repository Structure

    ├── 01_preprocessing/
    │   ├── run01_fastp_trimming.py
    │   ├── run02_hisat_mapping.py
    │   ├── run03_stringtie_assembly.sh
    │   └── run04_gffcompare.sh
    ├── 02_lncRNA_identification/
    │   └── run05_FEELnc_CPC2_lncRNAprediction.txt
    ├── 03_differential_expression_analysis/
    │   ├── run06_featurecounts.sh
    │   └── run07_EdgeR_DESEQ2_DEanalysis.ipynb
    ├── 04_coexpression_WGCNA_analysis/
    │   └── run08_WGCNA_coexpanalysis.ipynb
    ├── 05_network_filtering/
    │   ├── run09_coexp_data_filter.ipynb
    │   ├── run10_genepairs_net_construction.py
    │   ├── run11_quantilnetwork_to_cytoscape.py
    │   ├── run12_edges_attributes1_pairsxtrait.py
    │   ├── run13_edges_attributes2_to_cytoscape.ipynb
    │   ├── run14_nodes_attributes_to_cytoscape.ipynb
    │   └── run15_annotation_nodes_of_interest.ipynb
    └── README.md

**Note:** The modules must be executed in order.

------------------------------------------------------------------------

## Pipeline Overview

### Step 01 - Preprocessing

#### `run01_fastp_trimming.py`

**Input:** - Raw paired-end reads (forward and reverse)

Example:

    your_path/sample1_1.fastq.gz    your_path/sample1_2.fastq.gz

**Output:** - Trimmed reads

------------------------------------------------------------------------

#### `run02_hisat_mapping.py`

**Input:** - Trimmed reads - Reference genome index

Example:

    ../sample1_paired1.fq.gz    ../sample1_paired2.fq.gz

Build index:

    hisat2-build reference_genome.fasta index_output

**Output:** - `.bam` files

------------------------------------------------------------------------

#### `run03_stringtie_assembly.sh`

**Input:** - `.bam` - `ref_genome.gtf`

**Output:** - `stringtie_merged.gtf`

------------------------------------------------------------------------

#### `run04_gffcompare.sh`

**Input:** - `ref_genome.gtf` - `stringtie_merged.gtf`

**Output:** - Comparison data

------------------------------------------------------------------------

### Step 02 - lncRNA Identification

#### `run05_FEELnc_CPC2_lncRNAprediction.txt`

**Input:** - `ref_genome.gtf` - `stringtie_merged.gtf`

**Output:** - Common lncRNAs

------------------------------------------------------------------------

### Step 03 - Differential Expression Analysis

#### `run06_featurecounts.sh`

**Input:** - `.bam`

**Output:** - `count_matrix.tsv`

------------------------------------------------------------------------

#### `run07_EdgeR_DESEQ2_DEanalysis.ipynb`

**Input:** - `count_matrix.tsv` - `metadata.txt`

**Output:** - DE genes, PCA, heatmaps

------------------------------------------------------------------------

### Step 04 - Co-expression Analysis

#### `run08_WGCNA_coexpanalysis.ipynb`

**Input:** - `TMM.tsv` - `metadata.txt` - `binary_traits.tsv`

**Output:** - Network files and plots

------------------------------------------------------------------------

### Step 05 - Network Filtering

#### `run09_coexp_data_filter.ipynb`

**Output:** - `filtered_mm.tsv`

------------------------------------------------------------------------

#### `run10_genepairs_net_construction.py`

**Output:** - `gene_list_pairs.txt`

------------------------------------------------------------------------

#### `run11_quantilnetwork_to_cytoscape.py`

**Output:** - Filtered networks

------------------------------------------------------------------------

#### `run12_edges_attributes1_pairsxtrait.py`

**Output:** - Weighted gene pairs

------------------------------------------------------------------------

#### `run13_edges_attributes2_to_cytoscape.ipynb`

**Output:** - `net075_pairsxtrait.tsv`

------------------------------------------------------------------------

#### `run14_nodes_attributes_to_cytoscape.ipynb`

**Output:** - `node_attributes.tsv`

------------------------------------------------------------------------

#### `run15_annotation_nodes_of_interest.ipynb`

**Output:** - `annotated_genes.tsv`
