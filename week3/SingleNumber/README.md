# Non-Optimal Approach
### Description
We can create a hashmap that will store all occurences of each number in the list. Return the key that only has an occurence of 1.

#### Algorithm
1. Create hashmap to hold occurence of integers
2. Add integers and number of occurences to hashmap
3. Search for key that only has a value of one
4. Return that key 

#### Time Complexity
Our time complexity is **O(n)** since we might search through each integers in the list.
#### Space Complexity
Our space complexity is **O(n)** since we are using a hashmap of size n number of integers.
#### Code
```python
def singleNumber(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    matchingDict = {}
    for i in range(len(nums)):
        if nums[i] not in matchingDict:
            matchingDict[nums[i]] = 1
        else:
            matchingDict[nums[i]] = matchingDict.get(nums[i]) + 1
    for key,value in matchingDict.items():
        if value == 1:
            return key
```
# Optimal Approach
### Description
This approach uses bit manipulation. https://www.youtube.com/watch?v=qMPX1AOa83k

#### Algorithm
1. Use bit manupilation to XOR each integer in the list.

#### Time Complexity
Our time complexity is **O(n)** since we might search through each integers in the list.
#### Space Complexity
Our space complexity is **O(1)** since we aren't using any auxialry data strucutres.
#### Code
```python
def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
           result = n ^ result
        return result
```