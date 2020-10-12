
operadores = {
    '+'
    ,'-'
    ,'/'
    ,'*'
    ,'**'
    ,'//'
    ,'%'
}

def calcular(expressao):
        if expressao.isdigit():
            return expressao
        for op in operadores:
            esquerda , operador , direita = expressao.partition(op)
            if operador in operadores:
                res = str(calcular(esquerda)) + op + str(calcular(direita))
                return eval(res)

while True:
    try:
        print('\tResultado:' + str(calcular(input("Calcular:"))))
    except:
        print('\tErro no calculo')
