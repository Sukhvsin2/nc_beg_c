class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        i = 0
        counter = 0
        while counter < len(students) and len(students) > 0 and len(sandwiches) > 0:
            print(counter)
            if students[i//len(students)] == sandwiches[i//len(sandwiches)]:
                students.pop(0)
                sandwiches.pop(0)
                counter = 0
            else:
                students.append(students.pop(0))
                counter += 1
        print(students)
        return len(students)
        
