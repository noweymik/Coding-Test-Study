prices = list(map(int, input().split()))

time1 = list(map(int, input().split()))
time2 = list(map(int, input().split()))
time3 = list(map(int, input().split()))

min_time = min(time1[0], time2[0], time3[0])
max_time = max(time1[1], time2[1], time3[1])

payment = 0
for t in range(min_time+1, max_time+1):
    count = 0
    if time1[0] < t <= time1[1]:
        count += 1
    if time2[0] < t <= time2[1]:
        count += 1
    if time3[0] < t <= time3[1]:
        count += 1
    payment += count * prices[count-1]

print(payment)