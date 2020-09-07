# Pep8 CamelCase para classes
class Pessoa:
    def __init__(self, nome=None, idade=30):
        self.nome = nome
        self.idade = idade

    # Pep8 snack_case para functions
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Felipe', 30)
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Teste'
    p.idade = 40
