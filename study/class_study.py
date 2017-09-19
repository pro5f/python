
'''
This is the study example to understand class.attribute and instance. attribute
'''

class Body(object):
    _weight = 171

    def __init__(self):
        self.age = 39
        self.bday = 1227
    def get_age(self):
        return self.age
    def get_bday(self):
        return self.bday

c = Body()

print "This is my body weight %d \n" % c._weight
print "This is my age %d \n" %c.age
print "This is my birthday %d \n" %c.bday

print "Print the __dict__ : %s \n" %c.__dict__


print "Run get_age %d \n" % c.get_age()
print "Run get_bday %d \n" %c.get_bday()
