# IMPORTAÇÕES
import PySimpleGUI as pg
from  APIs import nome_por_idade


def criar_janela():
    pg.theme('LightBrown13')

    layout = [
        [pg.Text('Nome: '), pg.Input(key='NAME', size=(10, 0))],
        [pg.Text('Sigla do País: '), pg.Input(key='SIGLA', size=(10, 0))],
        [pg.HSep()],
        [pg.Output(size=(22, 5))],
        [pg.Button('ENVIAR', key='ENVIAR'), pg.Push(), pg.Button('LIMPAR', key='LIMPAR')],
    ]

    return pg.Window('Idade conforme seu nome e nacionalidade', layout)

janela = criar_janela()

while True:
    event, value = janela.read()
    nombre = value['NAME']
    nacao = value['SIGLA']

    if event == 'ENVIAR':
        idade_da_pessoa = nome_por_idade(nombre, nacao)
        print(f'Com o nome {nombre} e o país {nacao} voce aparenta ter {idade_da_pessoa} anos ')
    elif event == 'LIMPAR':
        janela.close()
        janela = criar_janela()

