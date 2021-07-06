class Fractie:

    def __init__(self,numarator,numitor):
        self.numarator=numarator
        self.numitor=numitor

    def __str__(self):
        print('Fractia este: ',self.numarator,'/',self.numitor)

    def __add__(self, first_numarator, first_numitor, second_numarator, second_numitor):
        final_fraction=Fractie(1,1)
        if first_numitor==second_numitor:
            print('sdsad')
            final_fraction.numarator=first_numarator+second_numarator
            final_fraction.numitor=first_numitor
        else:
            final_fraction.numarator=(first_numarator*second_numitor)+(second_numarator*first_numitor)
            final_fraction.numitor=first_numitor*second_numitor
        if final_fraction.numarator%2==0 and final_fraction.numitor%2==0:
            final_fraction.numarator=final_fraction.numarator/2
            final_fraction.numitor=final_fraction.numitor/2
        if final_fraction.numarator % 3 == 0 and final_fraction.numitor % 3 == 0:
            final_fraction.numarator = final_fraction.numarator / 3
            final_fraction.numitor = final_fraction.numitor / 3
        if final_fraction.numarator%5==0 and final_fraction.numitor%5==0:
            final_fraction.numarator=final_fraction.numarator/5
            final_fraction.numitor=final_fraction.numitor/5
        return final_fraction

    def __sub__(self, first_numarator, first_numitor, second_numarator, second_numitor):
        final_fraction = Fractie(1,1)
        if first_numitor == second_numitor:
            final_fraction.numarator = first_numarator - second_numarator
            final_fraction.numitor = first_numitor
        else:
            final_fraction.numarator = (first_numarator * second_numitor) - (second_numarator * first_numitor)
            final_fraction.numitor = first_numitor * second_numitor
        if final_fraction.numarator % 2 == 0 and final_fraction.numitor % 2 == 0:
            final_fraction.numarator = final_fraction.numarator / 2
            final_fraction.numitor = final_fraction.numitor / 2
        if final_fraction.numarator % 3 == 0 and final_fraction.numitor % 3 == 0:
            final_fraction.numarator = final_fraction.numarator / 3
            final_fraction.numitor = final_fraction.numitor / 3
        if final_fraction.numarator % 5 == 0 and final_fraction.numitor % 5 == 0:
            final_fraction.numarator = final_fraction.numarator / 5
            final_fraction.numitor = final_fraction.numitor / 5
        return final_fraction

    def __inverse__(self):
        aux=self.numarator
        self.numarator=self.numitor
        self.numitor=aux
        return self

first_fraction=Fractie(1,2)
second_fraction=Fractie(3,4)
sum=Fractie(1,1)
dif=Fractie(1,1)
inverse=Fractie(1,1)
first_fraction.__str__()
second_fraction.__str__()
sum=Fractie.__add__(sum,first_fraction.numarator,first_fraction.numitor,second_fraction.numarator,second_fraction.numitor)
dif=Fractie.__sub__(dif,first_fraction.numarator,first_fraction.numitor,second_fraction.numarator,second_fraction.numitor)
inverse=Fractie.__inverse__(first_fraction)
print('Sum:')
sum.__str__()
print('Dif:')
dif.__str__()
print('Inverse:')
inverse.__str__()