#Dominik Zimny
#20/12/2019
nums = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4: "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten"
}
s = input()
for i in range(11):
    s = s.replace(str(i), nums[i])
print(s.lower())
