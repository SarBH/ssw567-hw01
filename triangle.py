import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
    """
    # Note: This code is completely bogus but demonstrates a few features of python
    if (a + b <= c or a + c <= b or b + c <= a) or (a or b or c)<0:
        return 'NotATriangle'
    elif (round(a**2 + b**2  - c**2, 1) == 0 or round(a**2 + c**2 - b**2, 1) == 0 or round(c**2 + b**2 - a**2, 1) == 0):
        return 'Right'
    elif a == b == c:
        return 'Equilateral'
    elif (a == b or b == c or a == c):
        return 'Isoceles'
    else:
        return 'Scalene'
    
        


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet_Right(self):
        """This function tests for right triangle classification"""
        self.assertEqual(classifyTriangle(3,4,5),'Right')
        self.assertEqual(classifyTriangle(6.5,10.70,8.5), 'Right')
        self.assertNotEqual(classifyTriangle(3,3,3), 'Right')
        self.assertNotEqual(classifyTriangle(0,0,0), 'Right', 'should be NotATriangle')

    def testSet_Equilateral(self): 
        """This function tests for equilateral triangle classification"""
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral')
        self.assertNotEqual(classifyTriangle(10,10,11),'Equilateral')
        self.assertEqual(classifyTriangle(34.5, 34.5, 34.5), 'Equilateral')

    def testSet_Isoceles(self): 
        """This function tests for Isoceles triangle classification"""
        self.assertNotEqual(classifyTriangle(1,1,1),'Isoceles')
        self.assertEqual(classifyTriangle(10,10,11),'Isoceles')
        self.assertEqual(classifyTriangle(34.5, 34.5, 35), 'Isoceles')
        
    def testSet_Scalene(self): 
        """This function tests for Scalene triangle classification"""
        self.assertNotEqual(classifyTriangle(1,1,1),'Scalene')
        self.assertEqual(classifyTriangle(10,20,11),'Scalene')
        self.assertEqual(classifyTriangle(34, 34.5, 35), 'Scalene')

    def testSet_NotATriangle(self): 
        """This function tests for NotATriangle triangle classification"""
        self.assertNotEqual(classifyTriangle(1,1,1),'NotATriangle')
        self.assertEqual(classifyTriangle(25,10,11),'NotATriangle')
        self.assertEqual(classifyTriangle(34.5, 34.5, 135), 'NotATriangle')
        self.assertEqual(classifyTriangle(34.5, 34.5, -35), 'NotATriangle')

if __name__ == '__main__':
   unittest.main(verbosity=2)