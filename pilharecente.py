
class PilhaRecentes:
    def __init__(self, limite=20):
        self.dados = []
        self.limite = limite

    def push(self, jogo):
        indice = -1
        for i in range(len(self.dados)):
            if self.dados[i].id == jogo.id:
                indice = i
                break
        if indice != -1:
            self.dados.pop(indice)

        self.dados.append(jogo)

        if len(self.dados) > self.limite:
            self.dados.pop(0)

    def pop(self):

        if self.is_empty():
            return None
        return self.dados.pop()

    def topo(self):

        if self.is_empty():
            return None
        return self.dados[-1]

    def is_empty(self):

        return len(self.dados) == 0

    def tamanho(self):

        return len(self.dados)

    def mostrar(self):

        if self.is_empty():
            print("  Nenhum jogo recente.")
            return
        print(f"\n  {'='*45}")
        print(f"  {'JOGOS RECENTES':^45}")
        print(f"  {'='*45}")
        posicao = 1
        for i in range(len(self.dados) - 1, -1, -1):
            jogo = self.dados[i]
            label = " << MAIS RECENTE" if posicao == 1 else ""
            print(f"  {posicao}. [{jogo.console}] {jogo.titulo}{label}")
            posicao += 1
        print(f"  {'='*45}")
        print(f"  Total: {self.tamanho()} jogo(s) recente(s)")

    def contem(self, jogo_id):

        for j in self.dados:
            if j.id == jogo_id:
                return True
        return False

    def salvar(self, nome_arquivo="recentes.txt"):

        try:
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                f.write("id;titulo;console\n")
                for jogo in self.dados:
                    f.write(jogo.linha_recentes() + "\n")
            print(f"  Recentes salvos em '{nome_arquivo}'.")
        except Exception as e:
            print(f"  Erro ao salvar recentes: {e}")

    def carregar(self, catalogo_dict, nome_arquivo="recentes.txt"):

        try:
            with open(nome_arquivo, "r", encoding="utf-8") as f:
                linhas = f.readlines()
            self.dados = []
            carregados = 0
            for linha in linhas[1:]: 
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(";")
                if len(partes) < 1:
                    continue
                jogo_id = int(partes[0])
                if jogo_id in catalogo_dict:
                    self.dados.append(catalogo_dict[jogo_id])
                    carregados += 1
            print(f"  Recentes carregados: {carregados} jogo(s).")
        except FileNotFoundError:
            print("  Nenhum histórico de recentes encontrado.")
        except Exception as e:
            print(f"  Erro ao carregar recentes: {e}")