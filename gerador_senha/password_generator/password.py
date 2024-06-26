from os import system
from internal_construction.generating import building, shuffling, forming

def standard(x):
    while True:
        if len(x) != 0:
            # Verificando se o usuário inseriu algo para ser recebido
            if x not in options:
                # Verificando se o dado recebido é válido para o funcionamento do código
                system('cls')
                print(f'Error! "{x}" NÃO É UMA OPÇÃO LISTADA! INSIRA UM VALOR VÁLIDO')
                print('-=-=-=-=-=-=-=-=-=-')
            else:
                system('cls')
                confirmation_boolean = boolean[x]
                return confirmation_boolean
        else:
            system('cls')
            print('Error! VOCÊ DEIXOU O CAMPO EM BRANCO, POR FAVOR, INSIRA UMA OPÇÃO!')
            print('-=-=-=-=-=-=-=-=-=-')
        
        # Solicite novamente a entrada do usuário se a entrada anterior for inválida
        x = input('Digite novamente: ').strip()

boolean = {
    '1': True,
    '2': False,  
}

options = '1', '2'

while True:
    confirmation = input(
        'Deseja que o programa gere uma senha segura?\n'
        '[ 1 ] - sim\n'
        '[ 2 ] - não\n'
        '----------------\n'
        '-> '
    ).strip()

    returning = standard(confirmation)
    if returning is False:
        system('cls')
        print('ENCERRANDO PROGRAMA!')
        break
    else:
        system('cls')
        print('Processando senha...')

        # Criando a senha
        processing = building()
        almost = shuffling(processing)
        generated_password = forming(almost)
        # Criando a senha

        print(f'Senha gerada -> {generated_password}')

        approved = input(
            'Considera a senha gerada segura?\n'
            '[ 1 ] - sim\n'
            '[ 2 ] - não\n'
            '----------------\n'
            '-> '
        ).strip()
        returning = standard(approved)

        if returning is False:
            print('Sentimos muito por não ser o que você esperava!')
            break
        else:
            print('Obrigado pelo feedback positivo, nosso sistema estará disponível para quantas vezes você quiser utilizar')
            break