import unittest


def sum(a, b):
    return a + b


class SumTest(unittest.TestCase):
    def test_sum(self):            #5 
        self.assertEqual(sum(1, 2), 3) # el test falla porque indirectamente, la suma entre (1,2) se iguala a 5
                                    # si hacemos el cambio para el 3, el test pasa sin problema


if __name__ == '__main__':
    unittest.main()
