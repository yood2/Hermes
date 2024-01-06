from interest_module import *

def main():
    a = 100
    b = 0.05
    c = 10

    # Test
    d = compound(a,b,c)
    print(d)
    print(discount(d,b,c))
    print(calculate_effective_annual_rate(0.05,12,12))

if __name__ == '__main__':
    main()