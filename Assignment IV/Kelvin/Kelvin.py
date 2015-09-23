while True:
    f = input("How many degrees celsius? ")

    k = f + 273.15
    if k == 0:
        print "Absolute zero"
    elif k < 0:
        print "Value can not be below absolute zero"
    else:
        print k



