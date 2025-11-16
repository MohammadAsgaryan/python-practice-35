class StudentClass:
    def __init__(self, count, ages, heights, weights):
        self.count = count
        self.ages = ages
        self.heights = heights
        self.weights = weights
        
        
        def avg_age(self):
            return sum(self.ages) / self.count
        
        def avg_height(self):
            return sum(self.heights) / self.count
        
        def avg_weight(self):
             return sum(self.weights) / self.count
         
         
# ---- دریافت ورودی‌های کلاس A ----
countA = int(input())
agesA = list(map(int, input().split()))
heightsA = list(map(int, input().split()))
weightsA = list(map(int, input().split()))

A = StudentClass(countA, agesA, heightsA, weightsA)

# ---- دریافت ورودی‌های کلاس B ----
countB = int(input())
agesB = list(map(int, input().split()))
heightsB = list(map(int, input().split()))
weightsB = list(map(int, input().split()))

B = StudentClass(countB, agesB, heightsB, weightsB)


print(float(A.avg_age()))
print(float(A.avg_height()))
print(float(A.avg_weight()))

print(float(B.avg_age()))
print(float(B.avg_height()))
print(float(B.avg_weight()))

avg_hA = A.avg_height()
avg_hB = B.avg_height()

avg_wA = A.avg_weight()
avg_wB = B.avg_weight()

if avg_hA > avg_hB:
    print("A")
elif avg_hB > avg_hA:
    print("B")
else:
    # قد برابر
    if avg_wA < avg_wB:
        print("A")
    elif avg_wB < avg_wA:
        print("B")
    else:
        print("Same")


