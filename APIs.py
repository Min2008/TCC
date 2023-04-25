# TCC DA YASMIN CUPARI RODRIGUES - YOUNG 1

import requests
import os

os.system('cls')


def nome_por_idade(name: str, country: str):
    url = f'https://api.agify.io?name={name}&country_id={country}'
    resposta = requests.get(url)
    idade = resposta.json()

    resposta_final = idade['age']

    return resposta_final

# NAO DEU CERTO COM ESSA API
# def abreviacao(country: str):
#     url = f'https://servicodados.ibge.gov.br/api/v1/paises/{country}'
#     resposta = requests.get(url)
#     sigla = resposta.json()

#     info_final = sigla['id']['abreviado']

#     return info_final


if __name__ == '__main__':
    name = input('digite o nome: ').capitalize()
    country = input('digite a sigla do país: ').upper()

    print(
        f'Com o nome {name} e o país {country} voce aparenta ter {nome_por_idade(name, country)} anos')
