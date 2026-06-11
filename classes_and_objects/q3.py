## 3. Counter Class with Class vs Instance Attributes
class Counter:
    total = 0

    def __init__(self, name):
        self.name = name
        self.count = 0 

    def increment(self, step=1):
        self.count += step
        Counter.total += step

    def reset(self):
        self.count = 0

    @staticmethod
    def show_total():
        return Counter.total

    def __str__(self):
        return f"{self.name}: count={self.count}"

c1 = Counter("clicks")
c2 = Counter("views")
c3 = Counter("downloads")

for _ in range(3):
    c1.increment()

for _ in range(5):
    c2.increment()

c3.increment(10)
c1.reset()
print(c1)
print(c2)
print(c3)
print(f"Total across all counters: {Counter.show_total()}")