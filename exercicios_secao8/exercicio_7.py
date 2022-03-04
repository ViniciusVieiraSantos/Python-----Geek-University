"""
7) Faça uma função que receba uma temperatura en graus Celsius e retorne-a
convertida em graus Fahrenheit. A fórmula de conversão é: F = C * (9.0/5.0) + 32.0,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""


def converter_fahrenheit(graus_celsius):
    f = graus_celsius * (9.0/5.0) + 32.0
    return print(f' {graus_celsius}°C = {f}°F')


converter_fahrenheit(float(input("Digite a temperatura em graus celsius para converter em graus Fahrenheit: ")))
