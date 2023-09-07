class TestPhonebook:

    # Comparação entre numeros com valores diferentes
    def test_add_1(self):
        assert 1 == 2

    # Comparação entre numeros com valor o mesmo valor, porém de String e Inteiro
    def test_add_2(self):
        assert "1" == 1

    # Comparação entre 2 caracteres iguals, porém entre maiuscula e minuscula
    def test_add_3(self):
        assert "F" == "f"

    # Asserção com booleano com valor falso, resultando o teste como falso
    def test_add_4(self):
        assert False

    # Asserção com booleano com valor verdadeiro, resultando o teste como verdadeiro
    def test_add_5(self):
        assert True
