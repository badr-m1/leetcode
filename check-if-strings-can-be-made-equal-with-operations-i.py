import pytest

class Solution(object):
    def canBeEqual(self, s1, s2):
        s1 = list(s1)
        s2 = list(s2)
        n = len(s1)

        for i in range(n):
            if s1[i] == s2[i]:
                continue

            if i + 2 >= n:
                return False

            if s1[i] == s2[i + 2] and s2[i] == s1[i + 2]:
                ns1 = s1[:]
                ns2 = s2[:]

                ns1[i], ns1[i + 2] = ns1[i + 2], ns1[i]
                ns2[i], ns2[i + 2] = ns2[i + 2], ns2[i]

                return (
                    self.canBeEqual(ns1[i:], s2[i:]) or
                    self.canBeEqual(s1, ns2[i:])
                )

            elif s1[i] == s2[i + 2]:
                s2[i], s2[i + 2] = s2[i + 2], s2[i]

            elif s2[i] == s1[i + 2]:
                s1[i], s1[i + 2] = s1[i + 2], s1[i]

            else:
                return False

        return True

        

def test():
    s = Solution()

    assert s.canBeEqual("abcd", "cdab") == True
    assert s.canBeEqual("abcd", "dacb") == False
