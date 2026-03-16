#Create the count matrix to downstream analysis such as differential expression and co-expression, from .bam files created in run02_hisat_mapping.py 
#Previously, a new_annotation.gtf file was constructed including annotated genes in the reference genome with "Llu" prefix, and the identifier of unannotated genes predicted as lncRNAs were change with the "Llu_lncRNA" prefix. The genes not identified in the genome and not predicted as lncRNAs, were identified with prefix "MSTRG".

#Run featurecounts in your ubuntu terminal and in the directory of .bam files : bash run06_featurecounts.sh

featureCounts -T 8 -a your_path/new_annotation.gtf -o count_matrix.tsv *.bam
