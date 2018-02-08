def coinToss():
    newArr = []
    tossCount = 0
    headCount = 0
    tailCount = 0
    print "Starting the program..."
    import random
    for num in range(5000):
        newArr.append(random.randint(1,2))
    print newArr
    for val in newArr:
        if val == 1:
            headCount += 1
            tossCount += 1
            print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(tossCount, headCount, tailCount)
        elif val == 2:
            tailCount += 1
            tossCount += 1
            print "Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format(tossCount, headCount, tailCount)
    print "Ending the program, thank you!"
coinToss()