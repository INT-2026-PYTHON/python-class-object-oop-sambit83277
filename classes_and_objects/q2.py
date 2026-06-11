## 2. Student Class with Marks List
class Student:
    def __init__(self, name, roll, marks=None):
        self.name = name
        self.roll = roll

        if marks is None:
            self.marks = []
        else:
            self.marks = list(marks) 

    def add_mark(self, mark):
        if mark < 0 or mark > 100:
            print(f"Invalid mark {mark}. Marks must be between 0 and 100.")
            return

        self.marks.append(mark)

    def total(self):
        return sum(self.marks)

    def average(self):
        if len(self.marks) == 0:
            return 0
        return self.total() / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"

    def report(self):
        return (
            self.name,
            self.roll,
            self.total(),
            self.average(),
            self.grade()
        )
s1 = Student("Alice", 101)
for m in [90, 85, 95]:
    s1.add_mark(m)
s2 = Student("Bob", 102)
for m in [40, 55, 60]:
    s2.add_mark(m)
s1.add_mark(110)
s2.add_mark(-10)
print(s1.report())
print(s2.report())