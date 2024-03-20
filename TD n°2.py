#Exercice 1

#Fonctions auxiliaires

def PGCD(a,b) :
    r = a
    while r!=0:
        r = a%b
        a = b
        b = r
    return a

print('Le PGCD de 24 et 32 est ' +  str(PGCD(24,32)))

# === Class

class Fraction :
    def __init__(self,num,denum):
        """ This function creates two objects : numerator and denominator """
        if denum == 0:
            print(" Error : denum equals zero")
            exit(1)
        self.num = num
        self.denum = denum


# === Méthodes

    def __str__(self):
        """ This function returns the fraction"""
        return f"({self.num}/{self.denum})"

    def add(self,other):
        """This function adds two different fractions and returns a new fraction object"""
        return Fraction(self.num*other.denum + self.denum*other.num,self.denum*other.denum)

    def mult(self,other):
        """This function multiplies two different fractions and returns a new fraction object"""
        return Fraction(self.num*other.num,self.denum*other.denum)


    def simplify(self):
        """This function reduces the fraction"""
        if PGCD(self.num,self.denum) == 1:
            return self
        else :
            a = PGCD(self.num,self.denum)
            return Fraction(self.num//a,self.denum//a)

    def flottant(self):
        """Converts to float in order to see all the digits"""
        return (self.num/self.denum)


def Harmonique(n):
    H = Fraction(0,1)
    for i in range(n+1):
        H = H.add(Fraction(1,i+1))
    return H


def Leibnitz(n):
    L = Fraction(1,1)
    for i in range(1,n+1):
        L = L.add(Fraction((-1)**i,2*i + 1))
    return L




class Polynomial:
    def __init__(self,Liste_coeff):
        self.coeffs = Liste_coeff


    def __str__()





# ===Test

if __name__ == "__main__" :

    my_fraction_1 = Fraction(3,4)
    my_fraction_2 = Fraction(5,6)
    my_fraction_3 = Fraction(24,32)

    print('my_fraction_1 : ' + str(my_fraction_1))                # Test de la classe Fraction
    print('my_fraction_2 : ' + str(my_fraction_2))

    print('La somme de my_fraction_1 et de my_fraction_2 est : ' +str(my_fraction_1.add(my_fraction_2)))
    print('Le produit de my_fraction_1 et de my_fraction_2 est : ' +str(my_fraction_1.mult(my_fraction_2)))
    print('La fraction simplifiée est : ' + str(my_fraction_3.simplify()))

    n =10000
    print('H(10000) vaut ' + str(Harmonique(n).flottant()))
    print('L(10000) vaut ' + str(Leibnitz(n).flottant()))









