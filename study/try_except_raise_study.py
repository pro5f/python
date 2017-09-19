import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except IOError:
    print("File doesn't existed!!")
except:
    print("Unexpected error:", sys.exc_info()[0])
else:
    i = i + 10
    print("Open file successs.")

#try:
#    raise NameError('HiThere')
#except NameError:
#    print('An exception flew by!')
#    raise

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)
