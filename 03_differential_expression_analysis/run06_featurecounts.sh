#Create the count matrix to downstream analysis such as differential expression and co-expression analysis from .bam files created in run02_hisat_mapping.py 
#Run featurecounts in your ubuntu terminal and in the directory of .bam files : bash run06_featurecounts.sh
#!/bin/bash
featureCounts -T 8 -a your_path/new_annotation.gtf -o count_matrix.tsv *.bam
