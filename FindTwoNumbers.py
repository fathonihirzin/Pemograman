def twoSums(nums, target):
    for i in range(len(nums)):
        if nums[i] < target:
            potNumb1 = nums[i]
            for j in range(len(nums)):

                #case 1: to get straight pattern only
                if nums[i] < nums[j] and nums[i] + nums[j] == target:
                    potNumb2 = nums[j]
                    if i < j and nums[j] != nums[i]:
                        x = (i, j)
                    else:
                        x = (j, i)
                    print(list(x))

                #case 2: to get all the patterns, including back and forth pattern    
                # if nums[i] != nums[j] and nums[i] + nums[j] == target:
                #     potNumb2 = nums[j]
                #     x = (i, j)
                #     print(list(x))

listNumber = []
listNumber = [int(float(number)) for number in input("Enter the list numbers (Example: 2 7 11 15): ").split()]
print("List Number: ", listNumber)
target = int(input("Target : "))
print("Output : ")
twoSums(listNumber, target)