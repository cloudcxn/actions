"""test_funcion_nombre.py para realizar pruebas."""

import unittest
from funcion_nombre import get_nombre_formateado


class NombresCasoPrueba(unittest.TestCase):
    """Pruebas para funcion_nombre.py ."""

    def test_nombre_apellido(self):
        """Probar si nombres como 'Enrique Bunbury' funcionan."""
        nombre_formateado = get_nombre_formateado('enrique', 'bunbury')
        self.assertEqual(nombre_formateado, 'Enrique Bunbury')
