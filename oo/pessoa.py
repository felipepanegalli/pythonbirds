# Pep8 CamelCase para classes
class Pessoa:
    # Pep8 snack_case para functions
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(id(p))
    print(p.cumprimentar())
