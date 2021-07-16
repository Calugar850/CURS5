class Fractie:

    def __init__(self,numarator,numitor):
        self.numarator=numarator
        self.numitor=numitor

    def __str__(self):
        value=str(self.numarator)
        value+='/'
        value+=str(self.numitor)
        return value

    def __add__(self, other):
        if self.numitor == other.numitor:
            new_fr = Fractie(self.numarator + other.numarator, self.numitor)
            return new_fr
        new_num = (other.numitor * self.numarator) + (other.numarator * self.numitor)
        new_den = self.numitor * other.numitor
        new_fr = Fractie(new_num, new_den)
        if new_fr.numarator%2==0 and new_fr.numitor%2==0:
            new_fr.numarator=new_fr.numarator/2
            new_fr.numitor=new_fr.numitor/2
        if new_fr.numarator%3==0 and new_fr.numitor%3==0:
            new_fr.numarator=new_fr.numarator/3
            new_fr.numitor=new_fr.numitor/3
        if new_fr.numarator%5==0 and new_fr.numitor%5==0:
            new_fr.numarator=new_fr.numarator/5
            new_fr.numitor=new_fr.numitor/5
        return new_fr

    def __sub__(self, other):
        if self.numitor == other.numitor:
            new_fr = Fractie(self.numarator - other.numarator, self.numitor)
            return new_fr
        new_num = (other.numitor * self.numarator) - (other.numarator * self.numitor)
        new_den = self.numitor * other.numitor
        new_fr = Fractie(new_num, new_den)
        if new_fr.numarator%2==0 and new_fr.numitor%2==0:
            new_fr.numarator=new_fr.numarator/2
            new_fr.numitor=new_fr.numitor/2
        if new_fr.numarator%3==0 and new_fr.numitor%3==0:
            new_fr.numarator=new_fr.numarator/3
            new_fr.numitor=new_fr.numitor/3
        if new_fr.numarator%5==0 and new_fr.numitor%5==0:
            new_fr.numarator=new_fr.numarator/5
            new_fr.numitor=new_fr.numitor/5
        return new_fr

    def __inverse__(self):
        aux=self.numarator
        self.numarator=self.numitor
        self.numitor=aux
        return self

first_fraction=Fractie(1, 2)
second_fraction=Fractie(3, 4)
sum_fraction=first_fraction + second_fraction
dif_fraction=first_fraction - second_fraction
inverse_fraction=first_fraction.__inverse__()
print('First fraction',first_fraction.__str__())
print('Second fraction',second_fraction.__str__())
print('Sum fraction',sum_fraction.__str__())
print('Dif fraction',dif_fraction.__str__())
print('Inverse fraction',inverse_fraction.__str__())
