# Brute Force Approach
### Description
This a straight forward problem in which we can use a hashmap to store to frequency of integers that we visit in the array. Once all of these values have been loaded into our hashmap, we can then compare each of their frequencies to get the most used integer in the list and return its key which will denote the most frequent integer given in the list.


#### Algorithm
1. Create hasmap to store integer frequencies
2. Iterate through hashmap and check for largest frequency of integer
3. Return the key of largest integer

#### Time Complexity
Our time complexity is **O(n)** since we have n number of integers in the given list.

#### Space Complexity
Our space complexity is **O(n)** since we storing n number of integers in a hashmap.

#### Code
```python
 def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        highestFrequency = 0
        result = 0
        #load character counts into dictionary
        for letter in nums:
            if letter not in counter:
                counter[letter] = 0
            counter[letter] += 1
        #check for highest character counter
        for key, value in counter.items():
            if counter[key] >= highestFrequency:
                highestFrequency = value
                result = key
        return result
        
```
# Optimal Approach
### Description
Use Boyer Moore Algorithm