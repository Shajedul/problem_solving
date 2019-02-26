def main():
    i, j = input().split()
    i = int(i)
    j = int(j)
    if i==0 or j==0:
        return 0
    maxCycleLength = 0
    if i > j:
        temp = i
        i = j
        j = temp

    temp = i
    while i < j:
        cycleLength = 1
        n = i

        while n != 1:

            if n % 2 == 1:
                n = 3 * n + 1

            else:
                n = n / 2

            cycleLength += 1

        if cycleLength > maxCycleLength:
            maxCycleLength = cycleLength
        i += 1

    print(str(temp) + ' ' + str(j) + ' ' + str(maxCycleLength))


if __name__ == '__main__':
    print('Enter 2 Numbers')
    main()
