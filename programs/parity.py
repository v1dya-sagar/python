def main():
    parityOf(int(input("Enter Number : ")))

def parityOf(x):
    if x % 2 == 0:
        print("It's even")
    else:
        print("It's odd")
main()