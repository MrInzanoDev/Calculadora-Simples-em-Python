#Calculadora Simples p/ Estudo de Iniciantes
#IMPORTANTE: A calculadora funciona através do terminal. Se estiver usando o VS Studio, faça o download da extensão Python para
#facilitar o uso :)

#Variáveis
numero1 = 0
numero2 = 0
operacao = ''
resulatdo = 0

#Solicitação dos Valores
#Para trocar a frase apenas mude o que há dentro das ''
numero1 = int(input ('Digite o 1° digito da operação:'))
operacao = input ('Digite a operação: ')
numero2 = int(input ('Digite o 2° digito da operação:'))

#Operações
#Operação de Soma
if operacao == '+':
    resultado = numero1 + numero2  
#Operação de Subtração
elif operacao == '-':
    resultado = numero1 - numero2 
#Operação de Divisão
elif operacao == '/':
    resultado = numero1 / numero2
#Operação de Multiplicação
elif operacao == '*':
    resultado = numero1 * numero2
#Operação de Potenciação
elif operacao == '^':
    resultado  = numero1 ** numero2

#Exibição do Resultado c/ a Conta
print (str(numero1) + '' + str(operacao) + '' + str(numero2) + '' + '=' + str(resultado))

#Se te ajudou, me siga nas redes sociais
#Twitter: @MrInzanoUwU
#Youtube: https://youtube.com/@mrinzanooficial

#Espero ter ajudado :)

