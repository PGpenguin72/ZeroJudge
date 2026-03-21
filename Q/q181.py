red_Light, green_Light = map(int, input().split())
total_Second = 0
child_Number = int(input())
children_Time_data = list(map(int, input().split()))

for child_Time in children_Time_data:
    wait_Time = child_Time % (red_Light+green_Light)
    total_Second += ((green_Light+red_Light)-wait_Time if wait_Time >= red_Light else 0)

print(total_Second)