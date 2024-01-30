class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_int(num):
            if num and num.lstrip('-').isdigit():
                return True
            return False
        stack = []
        for num in tokens:
            if is_int(num):
                stack.append(num)
            else:
                b = stack.pop()
                a = stack.pop()
                res = eval(a + num + b)
                stack.append(str(int(res)))
        return int(stack[-1])
