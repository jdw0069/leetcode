# Iterative Approach
### Description
We start by creating variables that will hold our starting and ending points (high and low). Next, we will loop through the array as long as these two variables/pointers to do equal each other. First, we calculate the middle and check to see if that is our target. We then start to cut the array in half each time depending our calculations until we finally reach the desired target.

#### Algorithm
1. Begin with the mid element of the whole array as search key.
2. If the value of the search key is equal to the item then return index of the search key.
3. Or if the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
4. Otherwise, narrow it to the upper half.
5. Repeatedly check from the second point until the value is found or the interval is empty

#### Time Complexity
Our time complexity is **O(logn)** as we are reducing the problem set by half on each iteration. Put another way, every time you double the number of elements in the list, you only increase the number of steps to solution by one. O(log N) basically means time goes up linearly while the n goes up exponentially. So if it takes 1 second to compute 10 elements, it will take 2 seconds to compute 100 elements, 3 seconds to compute 1000 elements, and so on.

#### Space Complexity
Our space complexity is **O(1)** since we are only storing a constant space for the variables.

#### Code
```python
def search(self, nums: List[int], target: int) -> int:
        #set low and high of list
        low = 0
        high = len(nums) - 1
        #low looping through list
        while (low <= high):
            #calculate middle
            middle = (low + high) / 2
            #check to see if we hit the target:
            if (nums[middle] == target):
                return middle
            #if number lower than target, search right subarray
            elif (nums[middle] < target):
                low = middle + 1
            #if number higher than target, search left subarray
            elif (nums[middle] > target):
                high = middle - 1
        #didn't find target
        return -1 
```

---

# Recursive Approach
### Description
 



#### Time Complexity


#### Space Complexity


#### Code
```python

```