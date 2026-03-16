### NOTE1: before running, the sequencing data must be downloaded
### NOTE2: input files and their paths needs previously listed in two columns separate by a tab \t, similar to list_file.txt: your_path/{filename}sample1_1.fastq.gz	    your_path/sample1_2.fastq.gz
### then run this script in ubuntu terminal as: python3 run01_fastp_trimming.py list_file.tsv
### NOTE4: our dataset was sequenced with umis, subsequently, umis were removed in this step

#!/usr/bin/env python
# coding: utf-8
import sys
import os
from pathlib import Path

list_of_data = sys.argv[1]
adapters="your_path/adapters.fasta"

out=".../01_trimming"
paired=out+"/paired"
unpaired=out+"/unpaired"
json=out+"/reports/json"
html=out+"/reports/html"

Path(out).mkdir(parents=True, exist_ok=True)
Path(paired).mkdir(parents=True, exist_ok=True)
Path(unpaired).mkdir(parents=True, exist_ok=True)
Path(json).mkdir(parents=True, exist_ok=True)
Path(html).mkdir(parents=True, exist_ok=True)

with open(list_of_data, "r") as fp: 
    for line in fp:
        line=line.rstrip()
        aux=line.split("\t")
        #print(aux[0])
        fn=aux[0].split("/")
        fn=fn[-1].split("_")
        p1=paired+"/"+fn[0]+"_paired1.fq.gz"
        p2=paired+"/"+fn[0]+"_paired2.fq.gz"
        up1=unpaired+"/"+fn[0]+"_unpaired1.fq.gz"
        up2=unpaired+"/"+fn[0]+"_unpaired2.fq.gz"
        jsonr=json+"/"+fn[0]+"_report.json"
        htmlr=html+"/"+fn[0]+"_report.html"
        print ("Running trimming step")
        fastp="fastp -i "+ aux[0] + " -I "+ aux[1]+ " -o "+ p1+ " -O "+p2+" -q 30 -r -w 16 -l 50 -g --dedup --dup_calc_accuracy 6 -U --umi_loc per_read --umi_len 3 -p --unpaired1 "+up1+ " --unpaired2 "+up2+" -f 10 -t 10 --detect_adapter_for_pe --adapter_fasta " +adapters+ " -j "+ jsonr+ " -h "+ htmlr
        os.system(fastp)
        print ("End of trimming step")
        
