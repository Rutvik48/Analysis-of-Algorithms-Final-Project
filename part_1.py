import random, sys, math, timeit, decimal
from random import randint

#----------------------------------------------------------------------
#Craete a list
def createList(a, raNge, lengthl):
  # for loop 0 to n, which is the number of elements
  for index in range(0, lengthl):
      # picks a number from 1 to N(n)
      a.append(random.randint(1, raNge))
#---------------------------------------------------------------------
#
#
#
#
#---------------------------------------------------------------------
#Median Order Statistic
def selectionBased(arr, leftindex, rightindex):
  n = rightindex - leftindex + 1
  k = math.ceil(n / 2)
  l = leftindex
  for i in range(k):
      min_idx = l
      for j in range(l + 1, rightindex + 1):
          if arr[min_idx] > arr[j]:
              min_idx = j
      arr[l], arr[min_idx] = arr[min_idx], arr[l]
      l += 1
  return arr[(rightindex + leftindex) // 2]

#-----------------------------------------------------------------------
def pick_pivot(arr, leftindex, rightindex):
  median = []
  n = math.ceil((rightindex - leftindex + 1) / 5)
  for i in range(0, n - 1):
      median.append(selectionBased(arr, leftindex+5*i, leftindex + 5 * (i + 1) - 1))
  median.append(selectionBased(arr, leftindex + (n - 1) * 5, rightindex))
  # now find median of medians
  # if number of element inside median list < 100 use selection based algorithm
  # else use findKth using k = ceil of len(median)//2
  if(len(median)<=500):
      value = selectionBased(median, 0, len(median) - 1)
  else:
     value = (findTheMEdianAlg(median, 0, len(median)-1, math.ceil(len(median)/2)))
  median.clear()
  return value

def partition(arr, leftindex, rightindex):
  k = pick_pivot(arr, leftindex, rightindex)
  tmp = arr.index(k)
  arr[rightindex], arr[tmp] = arr[tmp], arr[rightindex]  # swapping new_pivot with the last element
  pivot = arr[rightindex]
  i = leftindex
  j = leftindex
  while j < rightindex:
      if arr[j] <= pivot:
          arr[i], arr[j] = arr[j], arr[i]
          i += 1  # and increment i
      j += 1
  arr[i], arr[rightindex] = arr[rightindex], arr[i]
  return i

def findTheMEdianAlg(arr, leftindex, rightindex, k):
  if (rightindex - leftindex + 1 >= k and k > 0):

      pivotindex = partition(arr, leftindex, rightindex)
      if (pivotindex - leftindex == k - 1):
          return arr[pivotindex]
      elif (pivotindex - leftindex >= k):  # k is in first subarray
          return findTheMEdianAlg(arr, leftindex, pivotindex - 1, k)
      else:  # k is in first subarray
          return findTheMEdianAlg(arr, pivotindex + 1, rightindex, k - pivotindex+leftindex - 1)
  else:
      return sys.maxsize
#----------------------------------------------------------------------------------------------------------
#
#
#
#
#
#
#
#
#Quick Sort---------------------------------------------------------------------------------------------
def quicksort(alist, start, end):
    if start < end:
        pIndex = partition_quickSort(alist, start, end)
        quicksort(alist, start, pIndex - 1)
        quicksort(alist, pIndex + 1, end)

    return alist

def partition_quickSort(alist, start, end):
    pivot = randint(start, end)
    temp = alist[end]
    alist[end] = alist[pivot]
    alist[pivot] = temp
    pIndex = start

    for i in range(start, end):
        if alist[i] <= alist[end]:
            temp = alist[i]
            alist[i] = alist[pIndex]
            alist[pIndex] = temp
            pIndex += 1
    temp1 = alist[end]
    alist[end] = alist[pIndex]
    alist[pIndex] = temp1
    return pIndex

#--------------------------------------------------------------------------------------------------------
#
#
#
#
#
#
#
#Quick-Select-------------------------------------------------------------------------------------

def partition_quick_Select(alist, start, end):
    pivot = randint(start, end)
    temp = alist[end]
    alist[end] = alist[pivot]
    alist[pivot] = temp
    pIndex = start

    for i in range(start, end):
        if alist[i] <= alist[end]:
            temp = alist[i]
            alist[i] = alist[pIndex]
            alist[pIndex] = temp
            pIndex += 1
    temp1 = alist[end]
    alist[end] = alist[pIndex]
    alist[pIndex] = temp1
    return pIndex


def findTheKth_QuickSelect(arr, leftindex, rightindex, k):
  if (rightindex - leftindex + 1 >= k and k > 0):

      pivotindex = partition_quick_Select(arr, leftindex, rightindex)
      if (pivotindex - leftindex == k - 1):
          return arr[pivotindex]
      elif (pivotindex - leftindex >= k):  # k is in first subarray
          return findTheKth_QuickSelect(arr, leftindex, pivotindex - 1, k)
      else:  # k is in first subarray
          return findTheKth_QuickSelect(arr, pivotindex + 1, rightindex, k - pivotindex+leftindex - 1)
  else:
      return sys.maxsize



#-----------------------------------------------------------------------------------
#
#
#
#
#
#
#
#
#
#
#MAIN
if __name__ == '__main__':
  # rangeList is N
  rangeL = [5000, 8000, 10000]
  # lengthList is n
  lengthL = [100, 300, 500, 1000, 2000, 4000]
  aList = []
  aList.clear()
  for lenIndex in range(0, len(lengthL)):
      for rangeIndex in range(0, len(rangeL)):
          createList(aList, rangeL[rangeIndex], lengthL[lenIndex])
          ith = random.randint(1, lengthL[lenIndex] - 1)
          # this loop will pick 5 "i" randomly from  1 to n
          #for i in range():
          print("Using Median Order Statistic-----------------------------------------------------------")
          print("Looking for ith = ", ith, "\nRange is 0 to N = ", rangeL[rangeIndex],
                "\nList length is 1 to n = ", lengthL[lenIndex])
          start = timeit.default_timer() * 1e+6
          print("ith Smallest(return from findKthSmallest) = ", findTheMEdianAlg(aList, 0, len(aList) - 1, ith))
          end = timeit.default_timer() * 1e+6
          print("After sorting we get ith index = ", aList[ith - 1])
          print("It took approximately ", round(end - start, 2), " Microseconds to find the ", ith,
                "th element of array.\n")

          # ----------------------------------------------------------------------------------------------
          print("Using Quick Select-----------------------------------------------------------")
          print("Looking for ith = ", ith, "\nRange is 0 to N = ", rangeL[rangeIndex],
                "\nList length is 1 to n = ", lengthL[lenIndex])
          start = timeit.default_timer() * 1e+6
          print("ith Smallest(return from findKthSmallest) = ", findTheKth_QuickSelect(aList, 0, len(aList) - 1, ith))
          end = timeit.default_timer() * 1e+6
          print("After sorting we get ith index = ", aList[ith - 1])
          print("It took approximately ", round(end - start, 2), " Microseconds to find the ", ith,
                "th element of array.\n")
          # -------------------------------------------------------------------------------------------------
          print("Using Quick Sort-----------------------------------------------------------")
          print("Looking for ith = ", ith, "\nRange is 0 to N = ", rangeL[rangeIndex],
                "\nList length is 1 to n = ", lengthL[lenIndex])
          start = timeit.default_timer() * 1e+6
          quicksort(aList, 0, len(aList) - 1)
          print("ith Smallest(return from findKthSmallest) = ",
                aList[ith - 1])
          end = timeit.default_timer() * 1e+6
          print("After sorting we get ith index = ", aList[ith - 1])
          print("It took approximately ", round(end - start, 2), " Microseconds to find the ", ith,
                "th element of array.\n")
          ith = random.randint(1, lengthL[lenIndex] - 1)

      print("\n\n\n")
      aList.clear()
