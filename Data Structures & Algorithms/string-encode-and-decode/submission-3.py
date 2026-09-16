class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        length = len(strs)
        if length > 99:
            s = s + "t" + str(length)
        elif length > 9:
            s = s + "o" + str(length)
        else:
            s = s + str(length)
        for i in strs:
            n = len(i)
            if n > 99:
                s = s + "t" + str(n) + i
            elif n > 9:
                s = s + "o" + str(n) + i
            else:
                s = s + str(n) + i
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        idx = s[0]
        if (idx == "o"):
            idx = int(s[1 : 3])
            i = 3
        elif (idx == "t"):
            idx = int(s[1 : 4])
            i = 4
        else:
            idx = int(s[0])
            i = 1
        lst = []
        for j in range(idx):
            n = s[i]
            if (n == "o"):
                n = s[i + 1 : i + 3]
                i += 2
            elif (n == "t"):
                n = s[i + 1 : i + 4]
                i += 3
            start = i + 1
            end = start + int(n) - 1
            lst.append(s[start: end + 1])
            i = end + 1
        return lst