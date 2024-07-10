def BoasVindas():
    print('\nBem vindo ao meu primeiro projeto em Python!\n');
    print('Calculadora Python\n');

BoasVindas();

PrimeiroValor = int(input('\nDigite o primeiro Numero: \n'));

SegundoValor = int(input('\nDigite o segundo Numero: \n'));

def operações(PrimeiroValor, SegundoValor):

 soma = PrimeiroValor + SegundoValor;
 subtração = PrimeiroValor - SegundoValor;
 multiplicação = PrimeiroValor * SegundoValor;
 divisão = float(PrimeiroValor / SegundoValor);
 return soma, subtração, multiplicação, divisão;

soma, subtração, multiplicacao, divisao = operações(PrimeiroValor, SegundoValor);

print('\nO resultado da adição: ' + str(soma))
print('\nO resultado da subtração: ' + str(subtração))
print('\nO resultado da multiplicação: ' + str(multiplicacao))
print('\nO resultado da divisão: ' + str(divisao))