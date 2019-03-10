import unittest
from city_functions import guo_jia_m
class NameTestCase(unittest.TestCase):
    def test_country_city(self):
        new_country = guo_jia_m('china','beijing','123456789')
        self.assertEqual(new_country,'Chinabeijing123456789')

    def test_city_country(self):
        new_city = guo_jia_m('usa', 'chijiago','98765')
        self.assertEqual(new_city, 'Usachijiago98765')

if __name__=="__main()__":
    unittest.main()