class FilaPreferencial:
    def __init__(self):
        # Inicializa quatro listas vazias para representar as filas de diferentes níveis de urgência
        self.emergencia = []
        self.risco_consideravel = []
        self.normal = []
        self.leve = []

    def entrar_fila(self, nome, nivel_urgencia):
        # Adiciona a pessoa à fila correta com base no nível de urgência

        # Se a urgência for EMERGENCIA, adiciona à fila de emergência
        if nivel_urgencia == "EMERGENCIA":
            self.emergencia.append(nome)
        # Se a urgência for RISCO CONSIDERAVEL, adiciona à fila de risco considerável
        elif nivel_urgencia == "RISCO CONSIDERAVEL":
            self.risco_consideravel.append(nome)
        # Se a urgência for NORMAL, adiciona à fila normal
        elif nivel_urgencia == "NORMAL":
            self.normal.append(nome)
        # Se a urgência for LEVE, adiciona à fila leve
        elif nivel_urgencia == "LEVE":
            self.leve.append(nome)
        else:
            # Se o nível de urgência não for válido, mostra uma mensagem de erro
            print(
                "Nível de urgência inválido. Escolha EMERGENCIA, RISCO CONSIDERAVEL, NORMAL ou LEVE")

    def atender_proximo(self):
        # Atende a próxima pessoa na fila, dando prioridade aos níveis mais altos de urgência

        # Se houver pessoas na fila de emergência, atende a próxima dessa fila
        if self.emergencia:
            return self.emergencia.pop(0)
        # Se não houver pessoas na fila de emergência, verifica a fila de risco considerável
        elif self.risco_consideravel:
            return self.risco_consideravel.pop(0)
        # Se não houver pessoas nas filas anteriores, verifica a fila normal
        elif self.normal:
            return self.normal.pop(0)
        # Se não houver pessoas nas filas anteriores, verifica a fila leve
        elif self.leve:
            return self.leve.pop(0)
        else:
            # Se todas as filas estiverem vazias, retorna uma mensagem informando que não há ninguém na fila
            return "Ninguém na fila."


# Exemplo de uso
fila = FilaPreferencial()

while True:
    print("Opções:")
    print("1 - Entrar na fila")
    print("2 - Atender próximo")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        urgencia = input(
            "Nível de urgência (EMERGENCIA, RISCO CONSIDERAVEL, NORMAL, LEVE): ")
        fila.entrar_fila(nome, urgencia)
    elif opcao == "2":
        proximo = fila.atender_proximo()
        print(f"Atendendo: {proximo}")
    elif opcao == "3":
        break
