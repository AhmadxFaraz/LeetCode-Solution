class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1 = list(s)
        l2 = list(t)
        if len(l1)!=len(l2):
            return False
        for char in l1:
            if char in l2:
                l2.remove(char)
            else:
                return False
        return True

# better solution
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

# even better solution
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
        return True