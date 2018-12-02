# Day 1
def day1part1():
    print reduce((lambda x, y: int(x)+int(y)), open("input.txt").readlines())

def day1part2():
    frequencies = dict()
    frequency = 0
    frequencies[frequency] = ""
    nums = open("input.txt").readlines()
    while (True):
        for num in nums:
            frequency = frequency + int(num)
            if frequencies.get(frequency) != None:
                return frequency
            frequencies[frequency] = ""
        print "reached end of file"
    return "hi"
print day1part2()
