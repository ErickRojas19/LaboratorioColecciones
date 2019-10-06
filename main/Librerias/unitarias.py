from custom_functions import temperature_methods
import unittest


class TestStringMethods(unittest.TestCase):
    def test_promedio(self):
        lista = [1,2,3,4,5,6,7,8,9,10,11,12]
        print(temperature_methods.promedio(lista))
        self.assertEqual(temperature_methods.promedio(lista), 6.5)
    def test_tem_mayor(self):
        lista = [30,32,33,32,35,36,37,35,36,32,40,30]
        self.assertEqual(temperature_methods.tem_mayor(lista),40)
    def test_tem_menor(self):
        lista = [30,32,33,32,35,36,37,35,36,32,40,29]
        self.assertEqual(temperature_methods.tem_menor(lista),29)
    def test_desvio(self):
        lsita = [30,32,33,32,35,36,37,35,36,32,40,30]
        self.assertEquals(temperature_methods.desviacion(lsita),3.0151134457776365)

    
unittest.main()