# CSC-382-Final-Project
Group project CSC382
Group members: Asliddin Asliev, Rajan Patell, Junde Jiang

Finding the kth smallest element using Order Statistic
&
Median Filtering

Part 1
In part one we had to implement Order Statistic algorithm and run various array to calculate CPU time. 
1.	What is Order Statistic?
2.	Pseudo code
3.	Implemented code
4.	Results
5.	Comparison with Quick sort and 
6.	Summary
	Suppose we have an array and we want to find how does elements of the array behave. For instance, we want to find if the kth (k in range of number of elements) element is smaller than P(any number). There are multiples ways to find out.
a.	Sort up to kth element using bubble or selection sort.
b.	Sort array completely using quick, heap or merge sort.
c.	Order statistic algorithm
Part a. 
	First option is good when you have small number of elements. However, this algorithm become slower when array is big and k is closer to n/2 (n is number of elements). We will have O(n^2).
Part b.
	Using quick, heap or merge sort the best time we can get is O(nlogn). Just sort the array and return (k-1)th element.
Part c.
	Using Order Statistic we can find the kth element in O(n ) time . We know that partition function in QuickSort divides array into two sub-arrays, left side will be less than or equal to pivot, and the right side is always greater than pivot. Using this concept we can drop half of the array and save the time. You can write this algorithm in to ways, randomized pivot or you choose a pivot(deterministic solution).

	We use deterministic solution to find the medians of array, because after each iteration you will have at least n/4 elements less than the pivot and at most 3n/4 elements greater than pivot. Moreover, for the random kth element randomised pivot would be better choice.



	Pseudo Code (Order Statistic)
	
	findKthElement(arr, left, right,k)
		if(right-left+1>=k){ 
			indexPivot = partition(arr, left, right)
			if(indexPivot+1==k)
				return arr[indexPivot]
			if(indexPivot+1 > k) // k is inside the left subarray
				return findKthElement(arr,left,indexPivot-1,k)
			if (indexPivot+1<k) //k is inside the right sub-array
				return findKthElement(arr, indexPivot+1, right, k-indexPivot-1)
1.	For the Quick_Select we just pick a pivot randomly(inside the partition function we call random function).
2.	For the Deterministic Solution  divide the original array of size n into n/5 sub-arrays. Then, we have to find the median of each sub-array and finally we will choose our pivot as a median of all these meadians.
