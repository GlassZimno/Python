#Glass Zimny
#29/12/2019
def afind(values, count, taken):
        if count != 0:
            instance = values.index(searchVal)
            instances.append(instance + taken)
            values = values[instance + 1:]
            count -= 1
            taken += instance + 1
            afind(values, count, taken)

def mode(nums, limit):
    count = []
    count2 = []

    nums.sort()

    length = len(nums)
    for i in range(length):
        count.append(nums.count(nums[i]))


    nums2 = list(set(nums))
    nums2.sort()

    length2 = len(nums2)
    for i in range(length2):
                   count2.append(0)

                   
    for i in range(length):
                   location = nums2.index(nums[i])
                   count2[location] = count[i]

    modeCount = [0,0,0]
    instances = []
    searchVal = max(count2)

    count = count2.count(searchVal)

    

    afind(count2, count, 0)
    modes = []

    for i in range(len(instances)):
        modes.append(str(nums2[instances[i]]))

    length = len(modes)
    if length <= limit:
        output = ", ".join(modes)
        if length == 1: 
            output = "mode is " + output
        else:
            output = "modes are " + output
        
        output = "Your " + output + "."

    else:
        output = "There are no modes"
        
    print(output)

mode([1,2,2,3],3)
