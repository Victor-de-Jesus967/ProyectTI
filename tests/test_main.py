import pytest
from src.Main import *  # Ajusta según las importaciones reales en Main.py

def test_inicializacion():
    # Prueba básica de inicialización: verifica que no lance excepciones y que imprima el mensaje esperado
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        inicializar_base_datos()  # Llama sin esperar retorno
        output = captured_output.getvalue()
        assert "Base de datos y tablas creadas correctamente." in output
    finally:
        sys.stdout = sys.__stdout__

def test_ejecucion_principal():
    # Prueba de ejecución principal (ejemplo; adapta)
    resultado = iniciar_interfaz_principal()  # Asume una función principal
<<<<<<< HEAD
    assert resultado == "éxito"  # Cambia según el comportamiento esperado
=======
    assert resultado == "éxito"  # Cambia según el comportamiento esperado
>>>>>>> ee8135f36b84a92fbc46dc8cdcf4ff299be21ee3
