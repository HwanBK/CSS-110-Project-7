# CSC 110
# Project 7 - Test File
# Hwansu Kim (Billy)
# PyUnit Test for project 7

import unittest
import project7hwansu


class FunctionTest(unittest.TestCase):

    def test_fixCustNum(self):
        self.assertEqual(1234567890, project7hwansu.fixCustNum("1234567890"))
        self.assertEqual(1234567890, project7hwansu.fixCustNum("l234567890"))
        self.assertEqual(1234567890, project7hwansu.fixCustNum("123456789O"))
        self.assertEqual(101010101,  project7hwansu.fixCustNum("lOlOlOlOl"))

    def test_fixCustName(self):
        self.assertEqual(("Chulainn", "Cu"),         project7hwansu.fixCustName("Chulainn, Cu"))
        self.assertEqual(("mac Roich", "Fergus"),    project7hwansu.fixCustName("mac  Roich, Fergus"))
        self.assertEqual(("mac Cumhail", "Fionn"),   project7hwansu.fixCustName("  mac Cumhail  ,  Fionn  "))
        self.assertEqual(("Ua Duibhne", "Diarmuid"), project7hwansu.fixCustName(" Ua  Duibhne , Diarmuid  "))

    def test_fixCustPhone(self):
        self.assertEqual(("206", "1234567"), project7hwansu.fixCustPhone("2061234567"))
        self.assertEqual(("206", "1234567"), project7hwansu.fixCustPhone("(206)1234567"))
        self.assertEqual(("206", "1234567"), project7hwansu.fixCustPhone("206-123-4567"))
        self.assertEqual(("206", "1234567"), project7hwansu.fixCustPhone("(206)123-4567"))

    def test_fixCustBalance(self):
        self.assertEqual(1000.00, project7hwansu.fixCustBalance("$1000.00"))
        self.assertEqual(1000.00, project7hwansu.fixCustBalance("1000.00"))
        self.assertEqual(1000.00, project7hwansu.fixCustBalance("1,000.00"))
        self.assertEqual(1000.00, project7hwansu.fixCustBalance("$1,000.00"))
        self.assertEqual(0.00,    project7hwansu.fixCustBalance(""))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(FunctionTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


main()