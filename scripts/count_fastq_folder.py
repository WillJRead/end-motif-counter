from pathlib import Path
import pandas as pd
import glob

def count_fastq_folder(folder_name, motif_lengths=[2]):
    
    #set up paths
    script_dir = Path(__file__).resolve().parent
    data_dir = script_dir.parent / "data" / folder_name
    results_dir = script_dir.parent / "results"
    results_dir.mkdir(exist_ok=True)

    files = glob.glob(f"{data_dir}/*.fastq")
    all_results = {}
    combined_df = pd.DataFrame()

    for file_path in files:
        file_name = Path(file_path).name
        print(f"Processing {file_name}...")

        #initialize motif counts
        motif_counts = {l: {} for l in motif_lengths}
        total_reads = 0

        #read FASTQ folder
        with open(file_path, "rt") as f:
            while True:
                header = f.readline().strip()
                if not header:
                    break
                seq = f.readline().strip()
                f.readline()  # skip + sign
                f.readline()  # skip quality line
                total_reads += 1

                for l in motif_lengths:
                    if len(seq) >= l:
                        motif = seq[:l]
                        motif_counts[l][motif] = motif_counts[l].get(motif, 0) + 1

        print(f"Processed {total_reads} reads from {file_name}")

        #convert to DataFrame
        results_df = pd.DataFrame(motif_counts).fillna(0).astype(int)
        results_df.columns = ["end_motif_count"]
        results_df = results_df.sort_values(by="end_motif_count", ascending=False)
        results_df["file"] = file_name  # add file column for combined DF

        #save per-file CSV
        output_file = results_dir / f"{file_name.replace('.fastq','')}_motif_counts.csv"
        results_df.to_csv(output_file)

        #store in dictionary and append to combined DF
        all_results[file_name] = results_df
        combined_df = pd.concat([combined_df, results_df])

    #save combined CSV
    combined_output_file = results_dir / "combined_motif_counts.csv"
    combined_df.to_csv(combined_output_file)

    return all_results, combined_df

# Example usage:
results = count_fastq_folder("folder of files", motif_lengths=[2])
print(results)