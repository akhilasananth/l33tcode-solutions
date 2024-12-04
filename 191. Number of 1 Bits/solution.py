class Solution:
    def hammingWeight(self, n: int) -> int:
        n_binary = bin(n)[2:]
        digits = list(n_binary)
        count = 0

        for t in range(len(n_binary)):
            d = digits.pop()

            if d == '1':
                count += 1

        return count