class Solution:
    def reverse(self, x: int) -> int:
        num = list(str(x))
        if num[0] == '-':
            mid = len(num[1:]) // 2
            for i in range(mid):
                num[i + 1], num[-i - 1] = num[-i - 1], num[i + 1]

            re = num[1]
            while re == 0:
                del re
                re = num[1]

        else:
            mid1 = len(num) // 2
            for j in range(mid1):
                num[j], num[-j - 1] = num[-j - 1], num[j]

            re = num[0]
            while re == 0:
                del re
                re = num[0]

        st = ''
        for ch in num:
            st += ch

        if int(st) < -2 ** 31 or int(st) > ((2 ** 31) - 1):
            return 0
        return int(st)