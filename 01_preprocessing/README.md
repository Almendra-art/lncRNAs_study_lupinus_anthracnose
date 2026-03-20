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
