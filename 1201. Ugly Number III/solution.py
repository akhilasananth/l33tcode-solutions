class Solution:
    def nthUglyNumber(self, k: int, a: int, b: int, c: int) -> int:
        min_abc = min(a, b, c)

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return abs(x)

        ab = (a * b) / gcd(a, b)
        bc = (b * c) / gcd(b, c)
        ac = (a * c) / gcd(a, c)
        abc = (a * bc) / gcd(a, bc)

        def is_kth_ugly_num(num: int) -> bool:
            count = (num // a + num // b + num // c
                     - num // ab
                     - num // bc
                     - num // ac
                     + num // abc)
            return count >= k

        left, right = 1, min_abc * k

        while left < right:
            mid = left + (right - left) // 2

            if is_kth_ugly_num(mid):
                right = mid
            else:
                left = mid + 1

        return left
