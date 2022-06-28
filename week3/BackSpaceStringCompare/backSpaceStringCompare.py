class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []
        
        for i in s:
            if i == "#" and len(stackS) > 0:
                stackS.pop()
            if i != "#":
                stackS.append(i)
        for i in t:
            if i == "#" and len(stackT) > 0:
                stackT.pop()
            if i != "#":
                stackT.append(i)
        
        if stackS == stackT:
            return True
        return False