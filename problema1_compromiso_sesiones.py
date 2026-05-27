"""
Fase 5 - Evaluacion Final POA
Curso: Fundamentos de Programacion - UNAD
Estudiante: Juan Fernando Duque Gutierrez
Problema 1: Clasificacion del nivel de compromiso de sesiones de clientes.

Una matriz almacena datos de sesiones con formato:
[ID Cliente, Duracion en segundos, Eventos Clics]

Reglas de negocio:
- Alto: duracion > 180 segundos y clics > 8
- Bajo: duracion < 60 segundos o clics < 3
- Medio: todos los demas casos
"""

from typing import Any, List, Sequence, Tuple

# Matriz inicial solicitada: al menos 5 filas de datos.
SESIONES_CLIENTES: List[List[Any]] = [
    [1001, 245, 12],
    [1002, 45, 7],
    [1003, 120, 5],
    [1004, 190, 2],
    [1005, 181, 9],
    [1006, 60, 3],
]


def clasificar_compromiso(duracion_segundos: int | float, clics: int | float) -> str:
    """
    Calcula la clasificacion de compromiso de una sesion.

    Args:
        duracion_segundos: Duracion de la sesion en segundos.
        clics: Cantidad de eventos de clic registrados.

    Returns:
        Una cadena con la clasificacion: "Alto", "Medio" o "Bajo".

    Raises:
        ValueError: Si duracion_segundos o clics son valores negativos.
        TypeError: Si los datos recibidos no son numericos.
    """
    if not isinstance(duracion_segundos, (int, float)) or not isinstance(clics, (int, float)):
        raise TypeError("La duracion y los clics deben ser valores numericos.")

    if duracion_segundos < 0 or clics < 0:
        raise ValueError("La duracion y los clics no pueden ser negativos.")

    if duracion_segundos > 180 and clics > 8:
        return "Alto"
    if duracion_segundos < 60 or clics < 3:
        return "Bajo"
    return "Medio"


def procesar_sesiones(sesiones: Sequence[Sequence[Any]]) -> List[Tuple[Any, str]]:
    """
    Procesa una matriz de sesiones y retorna el ID de cliente con su clasificacion.

    Args:
        sesiones: Matriz con filas en formato [ID Cliente, Duracion, Clics].

    Returns:
        Lista de tuplas (id_cliente, clasificacion).

    Raises:
        ValueError: Si una fila no tiene exactamente tres columnas.
    """
    informe: List[Tuple[Any, str]] = []

    for indice, sesion in enumerate(sesiones, start=1):
        if len(sesion) != 3:
            raise ValueError(
                f"La fila {indice} no cumple el formato [ID Cliente, Duracion, Clics]."
            )

        id_cliente, duracion, clics = sesion
        clasificacion = clasificar_compromiso(duracion, clics)
        informe.append((id_cliente, clasificacion))

    return informe


def mostrar_informe(sesiones: Sequence[Sequence[Any]]) -> None:
    """Imprime en consola el informe final solicitado por el problema."""
    informe = procesar_sesiones(sesiones)

    print("=" * 58)
    print("INFORME DE COMPROMISO DE SESIONES DE CLIENTES")
    print("=" * 58)
    print(f"{'ID Cliente':<15}{'Clasificacion final':<25}")
    print("-" * 58)

    for id_cliente, clasificacion in informe:
        print(f"{str(id_cliente):<15}{clasificacion:<25}")

    print("-" * 58)
    print(f"Total de sesiones evaluadas: {len(informe)}")


def main() -> None:
    """Punto de entrada principal del programa."""
    mostrar_informe(SESIONES_CLIENTES)


if __name__ == "__main__":
    main()
