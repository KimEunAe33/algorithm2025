import os
import json
import time
import sys
import csv
import tracemalloc  

from merge_sort import merge_sort
from heap_sort import heap_sort
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from quick_sort import quick_sort
from library_sort import library_sort
from tim_sort import tim_sort
from cocktail_shaker_sort import cocktail_shaker_sort
from comb_sort import comb_sort
from tournament_sort import tournament_sort
from introsort import introsort

algorithms = {
    "merge_sort": merge_sort,
    "heap_sort": heap_sort,
    "bubble_sort": bubble_sort,
    "insertion_sort": insertion_sort,
    "selection_sort": selection_sort,
    "quick_sort": quick_sort,
    "library_sort": library_sort,
    "tim_sort": tim_sort,
    "cocktail_shaker_sort": cocktail_shaker_sort,
    "comb_sort": comb_sort,
    "tournament_sort": tournament_sort,
    "introsort": introsort
}

def is_sorted_correctly(arr, origin):
    return arr == sorted(origin, key=lambda x:x[0])

def run_analysis(algorithm_name):
    algo_func = algorithms[algorithm_name]
    dataset_dir = "datasets"
    result_rows = []
    result_dir = "results"
    os.makedirs(result_dir, exist_ok=True)

    print(f"Running analysis for: {algorithm_name}\n")

    for file in sorted(os.listdir(dataset_dir)):
        file_path = os.path.join(dataset_dir, file)
        with open(file_path, "r") as f:
            data = json.load(f)

        size = int(file.split('_')[-1].replace(".json", ""))
        repeat_count = 10 
        total_time = 0.0
        total_memory = 0.0  
        correct = True
        for _ in range(repeat_count):
            copied = data.copy()

            tracemalloc.start() 
            start = time.perf_counter()

            algo_func(copied)

            end = time.perf_counter()
            current, peak = tracemalloc.get_traced_memory() 
            tracemalloc.stop() 

            total_time += end - start
            total_memory += peak / (1024 ** 2)  

            if not is_sorted_correctly(copied, data):
                print(f"Not Sorted! input: {data[:20]}, output: {copied[:20]}") 
                correct = False
            else:
                print(f"V {file} | Time: {round(total_time, 6)}s | Memory: {round(total_memory, 6)}MB | Correct: {correct}")

        mean_time = total_time / repeat_count 
        mean_memory = total_memory / repeat_count 

        dtype = file.replace(".json", "").rsplit("_", 1)[0]  
        result_rows.append([file, len(data), dtype, round(mean_time, 6), round(mean_memory, 6), "Yes" if correct else "No"])

        print(f"V {file} | Mean_Time: {round(mean_time, 6)}s | Mean_Memory: {round(mean_memory, 6)}MB | Correct: {correct}")

    csv_path = os.path.join(result_dir, f"{algorithm_name}_results.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["File", "Size", "Type", "Mean Time (s)", "Mean Memory (MB)", "Correct"])
        writer.writerows(result_rows)

    print(f"\nResults saved to: {csv_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analysis.py [algorithm_name]")
    else:
        run_analysis(sys.argv[1])
