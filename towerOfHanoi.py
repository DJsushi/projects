def hanoi(n, source, helper, target):
    if n > 0:
        hanoi(n - 1, source, target, helper)
        if source:
            target.append(source.pop())
        hanoi(n - 1, helper, source, target)
        
source = [4,3,2,1]
target = []
helper = []

#zavolame funkciu
hanoi(len(source),source,helper,target)

print("{}, {}, {}".format(source, helper, target))
