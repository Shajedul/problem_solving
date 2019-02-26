import math


def main():
    a, b, c = input().split()
    a = float(a)
    b = float(b)
    c = float(c)
    mod_one = module_one(a, b, c)

    if a!=0:
        if mod_one < 0:
            print('Impossivel calcular')
        else:
            r1 = (-b + math.sqrt(mod_one)) / (2 * a)
            r2 = (-b - math.sqrt(mod_one)) / (2 * a)
            print("R1 = %.5f" % r1)
            print("R2 = %.5f" % r2)
    else:
        print('Impossivel calcular')


def module_one(a, b, c):
    module_one_result = b*b - 4*a*c
    return module_one_result


if __name__ == '__main__':
    main()
