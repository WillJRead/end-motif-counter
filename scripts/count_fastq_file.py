from pathlib import Path
import pandas as pd

def count_fastq_file(file_name, motif_lengths=[]):
    #ensure correct pathing
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir.parent / "data" / file_name
    results_dir = script_dir.parent / "results"
    results_dir.mkdir(exist_ok=True)

    #intialise library 
    motif_counts = {l: {} for l in motif_lengths}
    total_reads = 0
    headers = []
    seq_len = []

    #start loop that will open file and read line by line
    with open(file_path, "rt") as f:
        while True:
            header = f.readline().strip()
            if not header:
                break
            seq = f.readline().strip()
            f.readline() #skips + sign
            f.readline() #skips quality line

            headers.append(header)
            seq_len.append(len(seq))
            total_reads += 1

            for l in motif_lengths:
                if len(seq) >= l:
                    motif = seq[:l]  # start-motifs
                    motif_counts[l][motif] = motif_counts[l].get(motif, 0) + 1

    print(f"Processed {total_reads} reads from {file_name}")
    
    #convert motifs to a dataframe
    results_df = pd.DataFrame(motif_counts).fillna(0).astype(int)
    results_df.columns = ["end_motif_count"]
    results_df = results_df.sort_values(by="end_motif_count", ascending=False)
    
    #saving file
    output_file = results_dir / f"{file_name.replace('.fastq', '')}_motif_counts.csv"
    results_df.to_csv(output_file)

    return results_df
    
    

# Example usage:
#df = count_fastq_file("your.file.name.fastq"), motif_lengths=[desired integer value of end-motif])
#print(df)
