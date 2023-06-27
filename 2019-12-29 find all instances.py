#Dominik Zimny
#29/12/2019
values = [1,2,3,1,2,4,5,6,3,2,1,3]
instances = []
searchVal = 3

count = values.count(searchVal)

def afind(values, count, taken):
    if count != 0:
        instance = values.index(searchVal)
        instances.append(instance + taken)
        values = values[instance + 1:]
        count -= 1
        taken += instance + 1
        afind(values, count, taken)

afind(values, count, 0)
print(instances)
