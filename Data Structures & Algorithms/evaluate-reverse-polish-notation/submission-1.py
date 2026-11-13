import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '/': operator.floordiv,
            '*': operator.mul
        }
        current = []
        for _, item in enumerate(tokens):
            if item not in ops.keys():
                current.append(item)
            else:
                a, b = current.pop(), current.pop()
                res = ops[item](int(b), int(a))
                current.append(str(res))
        
        return int(current[0])