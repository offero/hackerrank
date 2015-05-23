#!python3
def main():
    n = int(input().strip())
    for i in range(n):
        m = int(input().strip())
        print(((2**m)-1) % 10**5)

if __name__ == "__main__":
    main()
