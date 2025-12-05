### Mapping  
### Input files (previously trimmed by run01_fastp_trimming.py) must be listed in two columns separate by a tab \t, similar to list_of_data.txt: ../{filename}sample1_paired1.fq.gz   ../{filename}sample1_paired2.fq.gz
### An index was previously constructed in ubuntu terminal running: hisat2-build ../{filename_reference_genome.fasta} index_output
### CReate a directory mkdir 02_mapping, and then run inside this script in the ubuntu terminal as: python3 run02_hisat_mapping.py list_trimmed_file.txt 

#!/usr/bin/env python
# coding: utf-8

import sys
import os
from pathlib import Path


list_of_data = sys.argv[1]

#NOTE: indicate the path to your index directory, not to the files. 
index = "your_path/index"  

out_directory = "./02_mapping"
summary_dir = os.path.join(out_directory, "summary")

Path(out_directory).mkdir(parents=True, exist_ok=True)
Path(summary_dir).mkdir(parents=True, exist_ok=True)


with open(list_of_data, "r") as fp:
    for line in fp:
        line = line.rstrip()
        aux = line.split("\t")

        r1 = aux[0]
        r2 = aux[1]

        # Nombre base
        base = Path(r1).name.split("_")[0]

        # Output names
        sam_out = os.path.join(out_directory, f"{base}.sam")
        summary_out = os.path.join(summary_dir, f"{base}.txt")
        sorted_sam = os.path.join(out_directory, f"{base}_sorted.sam")
        bam_out = os.path.join(out_directory, f"{base}.bam")

        print(f"\n=== Running HISAT2 mapping for {base} ===")

        # ===========================
        # HISAT2
        # ===========================
        hisat2_cmd = (
            f"hisat2 -p 64 --dta -x {index} "
            f"-1 {r1} -2 {r2} "
            f"-S {sam_out} --summary-file {summary_out}"
        )
        os.system(hisat2_cmd)

        # ===========================
        # SAMTOOLS sort
        # ===========================
        sort_cmd = f"samtools sort --threads 64 {sam_out} -o {sorted_sam}"
        os.system(sort_cmd)

        # ===========================
        # SAMTOOLS view → BAM
        # ===========================
        bam_cmd = f"samtools view -bS -@ 64 -o {bam_out} {sorted_sam}"
        os.system(bam_cmd)

        # ===========================
        # clean SAM
        # ===========================
        rm_cmd = f"rm {sam_out} {sorted_sam}"
        os.system(rm_cmd)

        print(f"=== FINISHED {base} ===\n")
