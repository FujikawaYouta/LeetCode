class Solution:
    def calPoints(self, operations: list[str]) -> int:
        records = []
        for op in operations:
            if op == '+':
                records.append(records[-1]+records[-2])
            elif op == 'C':
                records.pop()
            elif op == 'D':
                records.append(records[-1]*2)
            else:
                records.append(int(op))
        return sum(records)

if __name__ == '__main__':
    sol = Solution()
    print(sol.calPoints(operations = ["5","2","C","D","+"]))
    print(sol.calPoints(operations = ["5","-2","4","C","D","9","+","+"]))