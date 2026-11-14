class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        wtf = sorted(zip(position, speed), key=lambda x: -x[0])
        stack = []
        for i, element in enumerate(wtf):
            p, s = element
            time = (target - p) / s
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)
            else:
                stack[-1] = max(stack[-1], time)
        return len(stack)