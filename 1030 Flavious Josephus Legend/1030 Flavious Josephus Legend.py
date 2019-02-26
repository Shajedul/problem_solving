def main():
    n, k = input().split()
    n = int(n)
    k = int(k)
    ans = lastmanstanding(n, k)
    print(ans)



def lastmanstanding(n, k):
    if n == 1:
        return 1
    else:
        return (lastmanstanding(n-1, k)+k-1) % n+1


if __name__ == '__main__':
    main()
