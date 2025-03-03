class Bird:
    wings = True
    beak = True
    plumage = True

    def fly(self):
        print('Машу крыльями и лечу')

    def walk(self):
        pass


class Sparrow(Bird):
    size = 'small'
    color = 'brown'

    def walk(self):
        print('прыг - прыг')

class Duck(Bird):
    def walk(self):
        print('шагает')


chizhik = Sparrow()
pyzhik = Sparrow()
utka = Duck()
pyzhik.size = 'medium'

print(chizhik.size)
print(pyzhik.size)
print(chizhik.color)
print(pyzhik.color)
chizhik.fly()
utka.fly()
pyzhik.walk()
chizhik.walk()
utka.walk()

