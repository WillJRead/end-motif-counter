# Counting End-Motifs

This is a personal project where I explored DNA sequence data in FASTQ files to extract and count end-motifs of user-defined lengths. The goal was to practice Python programming, file parsing, and data summarization while working with real sequencing data before I started a much larger project where I would be underatking similiar tasks. The example data in this project is publicly avaibale however I cannot state exactly where it was downloaded from as the URL has been lost.

---

## **Project Structure** 

The project provides two modular scripts:

Count motifs from a single FASTQ file.

Count motifs from all FASTQ files in a folder, combining results into a single summary .csv.

Results are saved in a results/ folder, making it easy to reuse the scripts on new datasets.

```
Counting_End_Motifs/
│
├── data/                    # Place your FASTQ files here
│   ├── example_single_file.fastq
│   └── example_folder/      # Example folder with multiple FASTQ files
│       ├── sample1.fastq
│       ├── sample2.fastq
│       └── .gitkeep
│
├── results/                 # Output CSV files are saved here
│   └── .gitkeep
│
├── scripts/                 # Python scripts
│   ├── count_fastq_file.py  # Count end-motifs in a single FASTQ file
│   └── count_fastq_folder.py# Count end-motifs from all FASTQ files in a folder
│
└── README.md
```

# Usage

Before starting, make sure you have:
- Downloaded the project (ZIP or Git clone)
- Decompressed it 
- Placed your FASTQ files into the data/ folder

1. Count Motifs from a Single FASTQ File

```
from scripts.count_fastq_file import count_fastq_file

# Count 2-mer motifs from a single FASTQ file
df = count_fastq_file("example_single_file.fastq", motif_lengths=[2])
```

Can change the length to any number you want. You can specify multiple motif lengths:

```
df = count_fastq_file("example_single_file.fastq", motif_lengths=[2, 4])
```

2. Count Motifs from All FASTQ Files in a Folder

```
from scripts.count_fastq_folder import count_fastq_folder

# Count 2-mer motifs from all FASTQ files in a folder and combine results
df = count_fastq_folder("example_folder", motif_lengths=[2])
```

Generates combined_motif_counts.csv in the results/ folder. Each motif count includes information about which file it came from. Again multiple motif lengths are supported:

```
df = count_fastq_folder("example_folder", motif_lengths=[2, 4])
```

Aimed as a personal project to practice genomic data analysis. Make sure the data/ folder contains the files before running scripts. Results will always be saved in results/ for easy access. The scripts are modular, so you can reuse them with other datasets. Any suggestions for improvements or collaboration ideas are welcome!