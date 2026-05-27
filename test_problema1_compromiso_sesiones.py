"""Pruebas basicas para problema1_compromiso_sesiones.py."""

from problema1_compromiso_sesiones import clasificar_compromiso, procesar_sesiones


def ejecutar_pruebas() -> None:
    assert clasificar_compromiso(181, 9) == "Alto"
    assert clasificar_compromiso(180, 9) == "Medio"
    assert clasificar_compromiso(181, 8) == "Medio"
    assert clasificar_compromiso(59, 8) == "Bajo"
    assert clasificar_compromiso(120, 2) == "Bajo"
    assert clasificar_compromiso(60, 3) == "Medio"
    assert procesar_sesiones([[1, 200, 10], [2, 50, 10], [3, 100, 5]]) == [
        (1, "Alto"),
        (2, "Bajo"),
        (3, "Medio"),
    ]
    print("Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    ejecutar_pruebas()
