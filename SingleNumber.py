def singleNumber(nums):
    for i in range(len(nums)):
        exist_count = nums.count(nums[i])
        if exist_count == 1:
            print("Single Number =",nums[i])

listNumber = []
listNumber = [int(float(number)) for number in input("Enter the list numbers (Example: 4 1 2 2 1): ").split()]
print("List Number: ", listNumber)
singleNumber(listNumber)