class No():
    def __init__(self,sintoma):
        self.sintoma = sintoma
        self.esquerda = None
        self.direita = None

def mostrar_arvore(no, nivel=0):
    if no is not None:
        print(" " * nivel + str(no,no.sintoma))
        mostrar_arvore(no.esquerda, nivel+1)
        mostrar_arvore(no.direita, nivel + 1)

def diagnostico(no):
    while no.esquerda or no.direita:
        resposta = input(no.sintoma + "(sim/nao:)").strip().lower()
        if resposta == "sim":
            no = no.esquerda
        elif resposta == "nao":
            no = no.direita
        else:
            print("Por favor, digite corretamente")
    print("Diagnostico: " + no.sintoma)


#instanciando arvore
raiz = No("Você está com dor de cabeça?")
raiz.esquerda = No("Está vomitando?")
raiz.direita = No("Está com febre?")
raiz.esquerda.esquerda = No("Você está com dengue.")
raiz.esquerda.direita = No ("Você está com enxaqueca.")
raiz.direita.direita = No ("Está com dor de garganta?")
raiz.direita.esquerda = No ("Você possui uma infecção bacteriana.")
raiz.direita.direita.direita = No ("Você está saudavel.")
raiz.direita.direita.esquerda = No ("Você possui uma infeção viral.")

#main
def main():
    while True:
        print("\n Gerenciamento de Diagnóstico")
        print("1. Mostrar todos os resultados")
        print("2. Diagnosticar")
        print("3. Sair")

        escolha = int(input("Faça sua escolha:"))
        if escolha == 1:
            mostrar_arvore(raiz)
        elif escolha == 2:
            diagnostico(raiz)
        elif escolha == 3:
            print("Saindo...")
        else:
            print("Escolha inválida.")

if __name__ == "__main__":
    main()