"""
给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。
https://leetcode-cn.com/problems/count-primes/
"""


class Solution:
    @staticmethod
    def countPrimes(n: int) -> int:
        if n < 3:
            return 0

        prime_cnt = 0
        prime_table = [True] * n

        for outer in range(2, n):
            prime_flag = True
            if not prime_table[outer]:
                continue

            # Prime number check
            inner = 2
            while inner * inner <= outer:
                if not prime_table[inner]:
                    inner += 1
                    continue
                if not outer % inner:
                    prime_flag = False
                    prime_table[outer] = False
                    break
                inner += 1

            #  Sieve of Eratosthenes
            if prime_flag:
                prime_cnt += 1
                num = n // outer
                for index in range(min(n, outer), num + 1):
                    non_prime = index * outer
                    if non_prime >= n:
                        break
                    prime_table[non_prime] = False

        return prime_cnt

# 500w超时，看来只能用线性筛了
