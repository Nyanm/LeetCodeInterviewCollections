"""
1344. 时钟指针的夹角
给你两个数 hour 和 minutes 。请你返回在时钟上，由给定时间的时针和分针组成的较小角的角度（60 单位制）。
https://leetcode-cn.com/problems/angle-between-hands-of-a-clock/
"""


class Solution:
    @staticmethod
    def angleClock(hour: int, minutes: int) -> float:
        h_angle = (((hour + (minutes / 60)) % 12) / 12)
        m_angle = (minutes / 60)
        return min(abs(h_angle - m_angle), abs((1 - m_angle) + h_angle), abs((1 - h_angle) + m_angle)) * 360


"""
简单题，但还有个绊子
狡猾！狡猾！
"""
