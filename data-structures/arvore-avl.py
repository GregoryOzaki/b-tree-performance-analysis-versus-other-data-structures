from medidor_tempos import medir_tempo

class NoAVL:
    def __init__(self, chave):
        self.chave = chave  # ID armazenado
        self.esquerda = None  # Filho à esquerda
        self.direita = None  # Filho à direita
        self.altura = 1  # Altura do nó (1 por padrão)

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    # Obter a altura do nó
    def _altura(self, no):
        return no.altura if no else 0

    # Calcular o fator de balanceamento
    def _fator_balanceamento(self, no):
        if not no:
            return 0
        return self._altura(no.esquerda) - self._altura(no.direita)

    # Rotação à direita
    def _rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        # Rotação
        x.direita = y
        y.esquerda = T2

        # Atualizar alturas
        y.altura = 1 + max(self._altura(y.esquerda), self._altura(y.direita))
        x.altura = 1 + max(self._altura(x.esquerda), self._altura(x.direita))

        return x

    # Rotação à esquerda
    def _rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        # Rotação
        y.esquerda = x
        x.direita = T2

        # Atualizar alturas
        x.altura = 1 + max(self._altura(x.esquerda), self._altura(x.direita))
        y.altura = 1 + max(self._altura(y.esquerda), self._altura(y.direita))

        return y

    # Inserção
    @medir_tempo
    def inserir(self, chave):
        self.raiz = self._inserir(self.raiz, chave)

    def _inserir(self, no, chave):
        # Inserção padrão de árvore binária de busca
        if not no:
            return NoAVL(chave)
        elif chave < no.chave:
            no.esquerda = self._inserir(no.esquerda, chave)
        else:
            no.direita = self._inserir(no.direita, chave)

        # Atualizar altura do nó atual
        no.altura = 1 + max(self._altura(no.esquerda), self._altura(no.direita))

        # Verificar balanceamento
        balance = self._fator_balanceamento(no)

        # Caso LL (esquerda-esquerda)
        if balance > 1 and chave < no.esquerda.chave:
            return self._rotacao_direita(no)

        # Caso RR (direita-direita)
        if balance < -1 and chave > no.direita.chave:
            return self._rotacao_esquerda(no)

        # Caso LR (esquerda-direita)
        if balance > 1 and chave > no.esquerda.chave:
            no.esquerda = self._rotacao_esquerda(no.esquerda)
            return self._rotacao_direita(no)

        # Caso RL (direita-esquerda)
        if balance < -1 and chave < no.direita.chave:
            no.direita = self._rotacao_direita(no.direita)
            return self._rotacao_esquerda(no)

        return no

    # Busca
    @medir_tempo
    def busca(self, chave):
        return self._busca(self.raiz, chave)

    def _busca(self, no, chave):
        if not no:
            return False
        if chave == no.chave:
            return True
        elif chave < no.chave:
            return self._busca(no.esquerda, chave)
        else:
            return self._busca(no.direita, chave)

    # Remoção
    @medir_tempo
    def remover(self, chave):
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, no, chave):
        if not no:
            return no

        # Remoção padrão de árvore binária de busca
        if chave < no.chave:
            no.esquerda = self._remover(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover(no.direita, chave)
        else:
            # Nó com apenas um filho ou nenhum
            if not no.esquerda:
                return no.direita
            elif not no.direita:
                return no.esquerda

            # Nó com dois filhos: obtenha o sucessor
            sucessor = self._minimo(no.direita)
            no.chave = sucessor.chave
            no.direita = self._remover(no.direita, sucessor.chave)

        # Atualizar altura
        no.altura = 1 + max(self._altura(no.esquerda), self._altura(no.direita))

        # Verificar balanceamento
        balance = self._fator_balanceamento(no)

        # Balancear a árvore
        if balance > 1 and self._fator_balanceamento(no.esquerda) >= 0:
            return self._rotacao_direita(no)
        if balance > 1 and self._fator_balanceamento(no.esquerda) < 0:
            no.esquerda = self._rotacao_esquerda(no.esquerda)
            return self._rotacao_direita(no)
        if balance < -1 and self._fator_balanceamento(no.direita) <= 0:
            return self._rotacao_esquerda(no)
        if balance < -1 and self._fator_balanceamento(no.direita) > 0:
            no.direita = self._rotacao_direita(no.direita)
            return self._rotacao_esquerda(no)

        return no

    def _minimo(self, no):
        while no.esquerda:
            no = no.esquerda
        return no

    # Impressão da árvore (em ordem)
    def imprimir(self, no=None, nivel=0):
        if no is None:
            no = self.raiz  # Se não for passado, começa da raiz

        if no is not None:
            print("  " * nivel, f"Nível {nivel}: {no.chave}")
            
            # Imprimir filhos esquerdo e direito, se existirem
            if no.esquerda:
                self.imprimir(no.esquerda, nivel + 1)
            if no.direita:
                self.imprimir(no.direita, nivel + 1)
