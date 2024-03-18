class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        s = s; g = g
        while s and g:
            if(min(g)<=min(s)):
                g.remove(min(g))
                count += 1
            s.remove(min(s))

        return count