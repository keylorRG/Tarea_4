def euler(f, x0, y0, h, n):
    """
    Método de Euler para resolver EDOs.

    Args:
        f (function): La función a integrar f(x, y).
        x0 (float): El valor inicial de x.
        y0 (float): El valor inicial de y.
        h (float): El tamaño del paso.
        n (int): El número de pasos.

    Returns:
        list: Lista de valores de y.

    Ejemplo:
        >>> f = lambda x, y: x + y
        >>> euler(f, 0, 1, 0.1, 10)
        [0, 1.1, 1.21, 1.331, ...]
    """
    x, y = x0, y0
    ys = [y0]
    for _ in range(n):
        y += h * f(x, y)
        x += h
        ys.append(y)
    return ys

def rk2(f, x0, y0, h, n):
    """
    Método de Runge-Kutta de segundo orden (RK2) para resolver EDOs.

    Args:
        f (function): La función a integrar f(x, y).
        x0 (float): El valor inicial de x.
        y0 (float): El valor inicial de y.
        h (float): El tamaño del paso.
        n (int): El número de pasos.

    Returns:
        list: Lista de valores de y.

    Example:
        >>> f = lambda x, y: x + y
        >>> rk2(f, 0, 1, 0.1, 10)
        [1, 1.105, 1.221025, ...]
    """
    x, y = x0, y0
    ys = [y0]
    for _ in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        y += k2
        x += h
        ys.append(y)
    return ys

def rk4(f, x0, y0, h, n):
    """
    Método de Runge-Kutta de cuarto orden (RK4) para resolver EDOs.

    Args:
        f (function): La función a integrar f(x, y).
        x0 (float): El valor inicial de x.
        y0 (float): El valor inicial de y.
        h (float): El tamaño del paso.
        n (int): El número de pasos.

    Returns:
        list: Lista de valores de y.

    Example:
        >>> f = lambda x, y: x + y
        >>> rk4(f, 0, 1, 0.1, 10)
        [1, 1.110341, 1.234085, ...]
    """
    x, y = x0, y0
    ys = [y0]
    for _ in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
        ys.append(y)
    return ys

