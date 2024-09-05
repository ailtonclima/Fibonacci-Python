def pertence_fibonacci(numero):
    """Verifica se um número pertence à sequência de Fibonacci.

    Args:
        numero: O número a ser verificado.

    Returns:
        bool: True se o número pertence à sequência, False caso contrário.
    """

    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

# Obtendo o número a ser verificado
numero = int(input("Digite um número: "))

# Verificando se o número pertence à sequência e imprimindo o resultado
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
