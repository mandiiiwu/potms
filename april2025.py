n = int(input())
nums = sorted(list(map(int, input().split())))
print(nums)

newlist = []

if n % 2 == 1:
    n += 1

for _ in range(int(n/2)):
    newlist.append(max(nums) - min(nums))
    nums.remove(min(nums))
    try:
        nums.remove(max(nums))
    except: pass
    print(newlist)

print(sum(newlist))
