class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len (t):
            return False
        for i in s:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        for i in t:
            if i not in d.keys():
                return False
            else:
                d[i] -= 1
                if d[i] == 0:
                    d.pop(i)
        return True if len(d) == 0 else False