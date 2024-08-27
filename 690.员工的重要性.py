"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
class Solution:
    def getImportance(self, employees: list['Employee'], id: int) -> int:
        val = 0
        val_dict = dict()
        sub_dict = dict()
        sub = []
        for employee in employees:
            val_dict[employee.id]=employee.importance
            sub_dict[employee.id]=employee.subordinates
            if employee.id==id:
                val=employee.importance
                sub=employee.subordinates[:]
        while len(sub)>0:
            cur_id = sub.pop(0)
            cur_val = val_dict[cur_id]
            cur_sub = sub_dict[cur_id]
            val+=cur_val
            sub+=cur_sub
        return val
    
def employeeGenerator(employees) -> Employee:
    new_employees = []
    for employee in employees:
        new_employees.append(Employee(employee[0],employee[1],employee[2]))
    return new_employees
    
if __name__ == '__main__':
    sol = Solution()
    employees = employeeGenerator([[1,5,[2,3]],[2,3,[]],[3,3,[]]])
    print(sol.getImportance(employees,1))
        