#new  approch , use notes first before python.org
from fractions import Fraction

def main():
    x = Fraction(get_int("Fraction: "))
    #print logic
    percent = (x)*100
    if percent > 100:
        x = Fraction(get_int("Fraction: ")) #that's dumbass thing a have ever done
    elif percent <= 1:
        print('E')
    elif percent >= 99:
        print('F')
    else:
        print(f'{percent:.0f}%')


def get_int(prompt):
    while True:
        try:
            return Fraction(input(prompt))
        except (ValueError, ZeroDivisionError): #from hint
            pass



main()
