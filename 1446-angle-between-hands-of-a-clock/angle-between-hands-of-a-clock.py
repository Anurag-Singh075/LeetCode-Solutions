class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        H=hour
        M=minutes
        H=H%12
        outer_angle = abs((30*H)-((11*M)/2))
        return min(outer_angle, 360-(outer_angle))
