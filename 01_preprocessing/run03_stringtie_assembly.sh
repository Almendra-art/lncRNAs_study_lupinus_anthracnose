###Assembly 
###NOTE1: run this script in your ubuntu terminal as: bash run03_stringtie_assembly.sh

#!/bin/bash
mkdir -p 03_stringtie


mergelist="03_stringtie/mergelist.txt"
> "$mergelist"   

# ===============================
# 1) StringTie x BAM
# ===============================

for bam in ../your_path/*.bam; do
    base=$(basename "$bam" .bam)

    echo "Processing $bam ..."

    stringtie "$bam" \
        -l "$base" \
        -p 64 \
        -G your_path/ref_genome.gtf \
        -o 03_stringtie/"${base}.gtf"
 
    echo "03_stringtie/${base}.gtf" >> "$mergelist"
done

# ===============================
# 2) Merge 
# ===============================

echo "Running StringTie --merge ..."

stringtie --merge \
    -p 64 \
    -G your_path/ref_genome.gtf \
    -o 03_stringtie/stringtie_merged.gtf \
    "$mergelist"

echo "Done."
