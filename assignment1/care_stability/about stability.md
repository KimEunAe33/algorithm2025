# About difference with no_care_stability
In analysis.py, 
sorted(origin, key=lambda x:x[0]) executed correctly.
If input is [[3,1],[1,5],[1,2],[2,3],...], 
It will only compare each elements from the first element of each element of input. -> 3,1,1,2,...
sorted() function is based on tim sort, which is stable,
so the results of sorting will be like [[1,5],[1,2],[2,3],[3,1],...]
This folder's datasets are [[1,2], [1,4],[2,3],...] 
