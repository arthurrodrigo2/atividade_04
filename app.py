'''
Crie um app de compras de ingressos para o cinema. O programa irá receber (uma única vez) o nome e a idade do usuário, e em seguida, o programa exibe uma lista de filmes, suas salas e suas respectivas classificações indicativas (idade mínima para ver o fime). O usuário deverá escolher a sala do filme desejado e o programa deverá informar se o usuário tem idade para ver o filme ou não. Caso tenha a idade mínima para ver o filme, o programa irá imprimir o ingresso seguida da mensagem "Bom filme!". Caso o usuário não tenha a idade mínima para ver o filme, o programa irá impedir a entrada do usuário e iá re-exibir a lista de filmes para ele escolher outro.
'''

# App de compras de ingressos para o cinema

def main():
    # Dados dos filmes
    filmes = [
        {"título": "Velozes e furiosos", "sala": "Sala 1", "classificacao": 18},
        {"título": "Exterminador do futuro", "sala": "Sala 2", "classificacao": 16},
        {"título": "The Flash", "sala": "Sala 3", "classificacao": 14},
        {"título": "Super Man - Desenho", "sala": "Sala 4", "classificacao": 0}  # Livre
    ]

    # Entrada de dados
    nome = str(input("Informe seu nome: "))
    idade = int(input("Informe sua idade: "))
            
    while True:
        # Exibe os filmes
        print("\nLista de Filmes:")
        for i, filme in enumerate(filmes):
            print(f"{i + 1}. {filme['título']} - Sala: {filme['sala']} - Classificação: {filme['classificacao']} anos")

        # Escolha do filme
        escolha = int(input("Escolha o número do filme que deseja assistir: ")) - 1

        # Verifica se a escolha é válida
        if 0 <= escolha < len(filmes):
            filme_selecionado = filmes[escolha]
            # Verifica idade
            if idade >= filme_selecionado['classificacao']:
                print(f"\nIngresso para '{filme_selecionado['título']}' - Sala: {filme_selecionado['sala']}")
                print("Bom filme!")
                break
            else:
                print("Você não tem idade suficiente para assistir a este filme. Escolha outro filme.")
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
