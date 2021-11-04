import json

digite = 'Digite seu'
import logs.logs_erros as logs


def preencher_dados(name, email, cpf, telefone, data_nascimento, sexo, endereco):
    cliente = {'name': name, 'email': email, 'cpf': cpf, 'telefone': telefone, 'data_nascimento': data_nascimento,
               'sexo': sexo, 'endereco': endereco}
    file = open('cadastro.json', 'a')
    r = json.dumps(cliente)
    file.write(r)
    return cliente


def set_nome():
    try:
        name = input('Digite seu Nome: ')
        return name
    except Exception:
        logs.valor_invalido('Nome')


def set_email():
    try:
        email = str(input('Digite seu e-mail: '))
        return email
    except Exception:
        logs.valor_invalido('e-mail')


def set_cpf():
    try:
        cpf = int(input('Digite seu CPF: '))
        return cpf
    except Exception:
        print(logs.valor_invalido('CPF'))


def set_telefone():
    try:
        telefone = int(input('Digite seu telefone: '))
        return telefone
    except Exception:
        logs.valor_invalido('Telefone')


def set_data_nascimento():
    try:

        data_nascimento = input(f'{digite} nascimento: ')
        return data_nascimento
    except Exception:
        logs.valor_invalido('nascimento')


def set_sexo():
    try:
        sexo = input(f'{digite} sexo [M] [F] :').upper()
        if sexo == 'M' or 'F':
            return sexo
        else:
            print('Digite somente M para masculino e F para feminino.')
    except Exception:
        logs.valor_invalido('sexo')


def set_endereco():
    endereco = input(f'{digite} endereço: ')
    return endereco

