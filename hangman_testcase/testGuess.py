import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

        self.g1.guess('q') # false
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

        self.g1.guess('a') # Duplicate letters
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

        self.g1.guess('1') # int
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

        self.g1.guess('D') # upper
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')

        self.g1.guess('@') # Special Characters
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')

        self.g1.guess('ㄴ') #hangle
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')

        self.g1.guess('as') # len > 1
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('c')
        self.assertEqual(self.g1.displayGuessed(), ' a c e n t u ')
        # Duplicate letters
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a c e n t u ')
        # Special Characters
        self.g1.guess('@')
        self.assertEqual(self.g1.displayGuessed(), ' a c e n t u ')
        # int
        self.g1.guess('1')
        self.assertEqual(self.g1.displayGuessed(), ' a c e n t u ')

        # hangle
        self.g1.guess('ㄴ')
        self.assertEqual(self.g1.displayGuessed(), ' a c e n t u ')


    def testGuess(self):
        # secretword in  character
        self.assertFalse(self.g1.guess('c'))
        self.assertTrue(self.g1.guess('a'))

        # currentStatus
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        self.g1.guess('t')
        self.assertEqual(self.g1.currentStatus, '_e_a__t')
        self.g1.guess('u')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.g1.guess('as')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.g1.guess('a')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.g1.guess('1')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.g1.guess('@')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.g1.guess('ㄴ')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')



    def testFinished(self):
        # return

        self.assertFalse(self.g1.finished())
        self.g1.guess('a')
        self.assertFalse(self.g1.finished())
        self.g1.guess('d')
        self.assertFalse(self.g1.finished())
        self.g1.guess('f')
        self.assertFalse(self.g1.finished())
        self.g1.guess('u')
        self.assertFalse(self.g1.finished())
        self.g1.guess('l')
        self.assertFalse(self.g1.finished())
        self.g1.guess('t')
     # True
        self.assertTrue(self.g1.finished())

if __name__ == '__main__':
    unittest.main()
