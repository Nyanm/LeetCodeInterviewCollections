"""
887. 鸡蛋掉落
给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。
已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。
每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。
如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。
请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
https:╱╱leetcode-cn.com╱problems╱super-egg-drop
"""
from collections import defaultdict
from math import inf


class Solution:
    @staticmethod
    def superEggDropBisectDP(k: int, n: int) -> int:
        memo = defaultdict(int)

        def egg_test(left: int, x: int) -> int:

            if left == 1 or x <= 1:  # if there is only one egg left, we have no choice but test all floors from 1 to x
                return x
            if memo[(left, x)]:  # look up in memo
                return memo[(left, x)]

            low, high, res = 1, x, inf
            while high >= low:
                mid = (low + high) // 2  # bisection point

                # the egg crashed in this test, so we lost an egg and continue the test in lower floors (1, mid - 1)
                # [↑] the value of broken is a monotone non-decreasing function through x
                broken = egg_test(left - 1, mid - 1)
                # the egg survived, so we keep this egg and continue the test in higher floors (mid + 1, n)
                # those higher floors will be abstracted as an individual building (1, n - mid)
                # [↓] the value of not_broken is a monotone non-increasing function through x
                non_broken = egg_test(left, x - mid)

                # number of necessary tests
                # ↑    not-broken             broken
                # |  test(left, n-x)     test(left-1, x-1)
                # |                 ╲ ┆ ╱
                # |                  ╲┆╱  worse condition
                # | ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╳╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
                # |                  ╱┆╲
                # |                 ╱ ╎ ╲
                # └───────────────────↓──────────────────> x
                #        the minima we are looking for

                # the x goes to the right side of the intersection point of broken(x) and non-broken(x)
                # thus the higher border should be deflated
                if broken > non_broken:
                    high = mid - 1
                    res = min(res, broken + 1)
                # similarly, the lower border should be inflated
                else:
                    low = mid + 1
                    res = min(res, non_broken + 1)

            memo[(left, x)] = res
            return res

        return egg_test(k, n)

    @staticmethod
    def superEggDropAccumulativeDP(k: int, n: int) -> int:
        memo = defaultdict(int)
        cnt = 0
        # defining cnt as the maximum chances we can try, memo[(k, cnt)] as the highest floor we can achieve
        while memo[(k, cnt)] < n:
            cnt += 1
            for left in range(1, k + 1):
                # the highest floor we can achieve on the condition that
                # we have "left" eggs to lose and "cnt" times to try is :
                #  the last egg survived  →  memo[(left, cnt - 1)]
                #            +
                #    the last egg died    →  memo[(left - 1, cnt - 1)]
                #            +
                #            1            →  the current floor
                # it looks like a reverse solution of the former one, which separate the floors into two parts
                # and this solution trace back to the last condition and add them up to reconstruct a new condition
                memo[(left, cnt)] = memo[(left, cnt - 1)] + memo[(left - 1, cnt - 1)] + 1
        return cnt


"""
仔细看完了题解，深刻感受到自己抽象问题与建模能力差出太多来
非常漂亮的题目，非常漂亮的解法，二分的应用格外令人惊讶，而逆向解更令人称奇

二分法+动规尝试自己写了一下题解，思路就清晰多了，但是二分的边界条件就，就先抄着吧

逆向解乍一看更加抽象，但是理解后这种解法更显得简洁有力

好难啊啊啊啊啊！！！！！
"""
