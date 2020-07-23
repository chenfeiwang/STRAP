# -*- coding: utf-8 -*-
# @Author: Dongqing Sun
# @E-mail: Dongqingsun96@gmail.com
# @Date:   2020-07-17 07:37:07
# @Last Modified by:   Dongqing Sun
# @Last Modified time: 2020-07-17 20:32:22


import argparse
import pysam
import time, os
from collections import defaultdict

chr_list = ['chr'+str(i) for i in list(range(1,23))] 
chr_list = chr_list + ['chrX', 'chrY']

def CommandLineParser():
    parser=argparse.ArgumentParser(description = "Reshape the 10X fragment file to long fragment bed file.")
    parser.add_argument("-F","--frag", dest = "fragfile", default = "",help = "The fragment file generated by 10X CellRanger ATAC, "
        "with barcodes and counts.")
    parser.add_argument("-O", "--outdir", dest = "outdir", default = "", help = "The output directory.")

    return parser.parse_args()


parser = CommandLineParser()
fragfile = parser.fragfile
outdir = parser.outdir
outfile = os.path.join(outdir, "fragments_BEDPE.bed")

try:
    os.makedirs(outdir)
except OSError:
    pass

start_time = time.time()
print("Start to reshape 10X fragment file.",time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
with open(fragfile, "r") as frag_in, open(outfile, "w") as frag_out:
    for line in frag_in.readlines():
        items = line.strip().split("\t")
        if int(items[4]) == 1:
            frag_out.write("\t".join(items[0:3]) + "\n")
        else:
            for i in range(int(items[4])):
                frag_out.write("\t".join(items[0:3]) + "\n")
end_time = time.time()
print("End:", end_time-start_time)

