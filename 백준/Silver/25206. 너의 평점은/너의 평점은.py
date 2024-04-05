examination = {"A+": 4.5, "A0": 4.0,
               "B+": 3.5, "B0": 3.0,
               "C+": 2.5, "C0": 2.0,
               "D+": 1.5, "D0": 1.0,
               "F": 0.0}

cnt = 0
avg_sum = 0

for i in range(20):
  subject, grade, rating = input().split()
  grade = float(grade)
  if rating == 'P':
    continue
  avg_sum += grade * examination[rating]
  cnt += grade

print(avg_sum / cnt)