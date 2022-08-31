def soma(a,b):return a+b
def sub(a,b):return a-b
def mult(a,b):return a*b
def div(a,b):return a/b

def calculadora(op,a,b):
    operações = {
        '+': soma,
        '-': sub,
        '/': div,
        '*': mult,
    }
    return operações[op](a,b)
