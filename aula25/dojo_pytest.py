def soma(numero1,numero2):
    return numero1 + numero2

def test_soma_numero_negativo():
    assert soma(2,-2) == 0, "A funcao soma esta errada"

def test_soma():
    assert soma(2, 2) == 4

if __name__ == '__main__':
    test_soma()
    test_soma_numero_negativo()
    #test_valida_numero