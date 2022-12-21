def print_formatted(number):
    x=len(str(bin(number)[2:]))
    for i in range(number):
        print(f"{i+1 : >{x}}{oct(i+1)[2:] : >{x+1}}{hex(i+1)[2:].upper() : >{x+1}}{bin(i+1)[2:] : >{x+1}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)