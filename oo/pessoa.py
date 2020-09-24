# Pep8 CamelCase para classes
class Pessoa:
    OLHOS = 2

    def __init__(self, *filhos, nome=None, idade=30):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    # Pep8 snack_case para functions
    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_De_classe(cls):
        return f'{cls} - olhos - {cls.OLHOS}'


class Homem(Pessoa):
    pass


class Mutante(Pessoa):
    OLHOS = 4

    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Eis um mutante.'


if __name__ == '__main__':
    renzo = Mutante(nome='Renzo', idade=30)
    luciano = Homem(renzo, nome='Luciano', idade=40)
    print(luciano.nome)
    print(luciano.idade)
    for filhos in luciano.filhos:
        print(filhos.nome)
    print(renzo.OLHOS)
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_De_classe(),
          luciano.nome_e_atributos_De_classe())

    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))

    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(renzo.OLHOS)
    print(renzo.cumprimentar())
