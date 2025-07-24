"""
    3- Verificador de Senhas Fortes
    Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

    * Solicitar a senha até que o usuário digite "sair".  
    * Verificar se a senha possui pelo menos 8 caracteres.  
    * Verificar se contém pelo menos um número.  
    * Informar se a senha é fraca ou forte.  
    * Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair".  
"""


while True:
    senha = input('Digite uma senha (ou "sair" para encerrar): ')
    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break

    comprimento_ok = len(senha) >= 8
    tem_numero = any(caracter.isdigit() for caracter in senha)

    if comprimento_ok and tem_numero:
        print("Senha forte! Programa encerrado.")
        break
    else:
        print("Senha fraca. Certifique-se de ter ao menos 8 caracteres e pelo menos um número.")

