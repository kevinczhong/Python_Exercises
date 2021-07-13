class Solution:
    def find_factor(self, n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors

    def isPrime(self, n):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    return False
            else:
                return True

    def primeFactors(self, n):
        pre_factors = self.find_factor(n)
        results = []
        start, end = 0, len(pre_factors) - 1
        while start + 1 < end:
            if self.isPrime(pre_factors[start]) is True:
                results.append(pre_factors[start])
                start += 1
            else:
                start += 1
        return results

s = Solution()
print(s.primeFactors(900))

