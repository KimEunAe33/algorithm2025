# Notice!
After completing the code initially and recording the execution time, 
I realized that I also needed to check memory usage and stability for the report. 
Additionally, I had only tested with data ranges of 1k, 10k, and 100k. 
After I found it, I changed the data ranges to 1k, 10k, 100k, and 1M, 
but I noticed that it would be impossible to run the tests before the assignment submission. 
Some of algorithms took over 18~93 expectation hours to execute once for 1M, so I couldn't execute datasets of 1M.
I'm so sorry about that.
And 1M dataset files were so big to upload so i zipped them in dataset folder seperately.

# Usage of analysis.py
By using analysis.py, you can see execution time of each algorithm.
If you execute 
"python analysis.py [algorithm_name]"
like
"python analysis.py bubble_sort"
then, it will execute that algorithm with all files in datasets. 
Before, using it, be sure to contain only json files in datasets folders. 
After all execution, the mean results of execution will be saved as csv file.
