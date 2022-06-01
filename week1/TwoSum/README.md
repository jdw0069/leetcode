# Brute Force Approach
### Description
We check every possible pair in the array by using two pointers. One pointer that starts at the beginning of the list (index 0), and another that starts at the second index in the list (index i + 1). We use two for loops, add the two values, and compare this result to the target values. If these two numbers sum to the target, then we return the indices of pairs of integers.

#### Algorithm
1. Run the first loop to point to the first index of the nums array
2. Run another loops to poin to the second index of the nums array
3. Check if both elements sumed equal the target
4. Return the indicies of elements that sum to the target

#### Time Complexity
Our time complexity is **O(n^2)**. We use two for loops in which the first visits N number of elements and the second visits n-1 elements. Since we have to chech all possible pairs this comes out to be O(N*N) = O(n^2)

#### Space Complexity
Our space complexity is **O(1)** since we are only storing a constant space for the variable i.

#### Code
```python
 def twoSum(self, nums: List[int], target: int) -> List[int]:
        #start a beginning of list
        for i in range(0, len(nums)):
            #start at second index of list
            for j in range(i + 1, len(nums)):
                #sum both values and if equal to target, return index pair
                if nums[i] + nums[j] == target:
                    return [i, j]
```

---

# Optimized Approach
### Description
In order to optimize our solution, we have to move away from using nested for loops that check every element until an integer pair is found that sums up to our target as this time complexity is very slow. Here, we declare a dictionary to keep track of all the values we have seen so far and use one for loop to go through the entire array. We then subtract the target value from the current value to search for the complement. If the pair is found in the dictionary, return the index of both numbers. Otherwise, add it to our dictionary for a future visit. 

#### Algorithm
1. Create dictionary to keep track of all values seen so far
2. Run loop to iterate over the entire array
3. Check if the pair is found by subtracting the target value from the current value (the complement).
4. If the correct pair is found, return the indicies of elements that sum to the target
5. Otherwise, add the current value to the dictionary for future lookup

#### Time Complexity
Our time complexity is **O(N)** since we still have to check each N elements in the array, but here we are using only one for loop to iterate through the array and using the search property of a dictionary which guarantees us O(1) search times. 

#### Space Complexity
Our space complexity is **O(N)** since we are using a dictionary to store N number of elements.

#### Code
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create dictionary to store values we have already seen
        myDict = {}
        #loop through list starting at index 0
        for i in range(len(nums)):
            #if compelement in dictionary, return indexed pair
            if target - nums[i] in myDict:
                return [myDict[target - nums[i]], i]
            #add current index and value to dictionary
            else:
                myDict[nums[i]] = i
```