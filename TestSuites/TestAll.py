import unittest
from Package1.Test1 import *
from Package1.Test2 import *

t1 = unittest.TestLoader().loadTestsFromTestCase(Test1)
t2 = unittest.TestLoader().loadTestsFromTestCase(Test2)

ts = unittest.TestSuite([t1, t2])
unittest.TextTestRunner().run(ts)
