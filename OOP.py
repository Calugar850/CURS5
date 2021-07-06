class Animal:
    legs_no = 4

    def __init__(self, name, breed=None):
        self._name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    @classmethod
    def create_instance(cls):
        return cls('Ben')

    def __str__(self):
        return '<%s - Name = %s>' % (type(self), self._name)

    def __repr__(self):
        return '%s(name="%s, breed=%s)' % (type(self).__name__, self._name, self.breed)

    def __len__(self):
        return len(self._name)

    @staticmethod
    def speak():
        pass


class Dog(Animal):

    @staticmethod
    def speak():
        print("Ham Ham")

class CustomClass:
    legs_no=2

class Cat(Animal):

    @staticmethod
    def speak():
        print("Miua Miua")

    def __len__(self):
        return 20


#print(Dog.legs_no)
#Dog.legs_no=20

#print(type(Dog))
rex=Dog('Rex','Bulldog')
#print('Dog naem:',rex.name,'rasa',rex.breed,'nr legs',rex.legs_no)
ben=Dog('Ben')
#print('Dog naem:',ben.name,'rasa',ben.breed,'nr legs',rex.legs_no)
#print(Dog.legs_no)
#print(rex.name)
#rex.name='New Name'
#print(rex.name)
#rex.speak()
#Dog.speak()
#Dog.create_instance()
#new_dog=Dog.create_instance()
#print(new_dog)
#x=new_dog.__str__()
#print(x)
#print(len(new_dog))
#l=[new_dog]
#print(l)
julie=Cat('Julie')
#print(julie.name)
#print(julie.legs_no)
#julie.speak()

data1=[1,2,3,4,5]
data2='abcdefg'
data3=julie
l=[data1,data2,data3]
for i in l:
    print(len(i))

l=[rex,ben]
for animal in l:
    print(len(animal))

class FibonnaciIterator:
    def __init__(self,n):
        self._n=n

    def __iter__(self):
        self.value=1
        self.next_value=1
        return self

    def __next__(self):
        aux_value=self.value
        if self.next_value==1:
            self.next_value+=1
        else:
            self.value=self.next_value
            self.next_value=aux_value+self.next_value
        return aux_value

x=iter(FibonnaciIterator(10))
j=0
for i in x:
    print(i)
    j+=1
    if j==10:
        break
