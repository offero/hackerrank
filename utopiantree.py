def ut(n, x):
    return (2**(((n-1)//2)+1))*x + 2**(((n-1)//2)+1) - 1 - n%2

def main():
    x = 1
    T = int(raw_input().strip())
    for i in xrange(T):
        n = int(raw_input().strip())
        print(ut(n, x))

if __name__ == "__main__":
    main()
