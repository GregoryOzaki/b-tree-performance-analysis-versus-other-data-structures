from medidor_tempos import medir_tempo

class No:
    def __init__(self, folha=False):
        self.folha = folha
        self.chaves = []
        self.filhos = []

class ArvoreB:
    def __init__(self, ordem):
        self.ordem = ordem
        self.raiz = No(folha=True)

    @medir_tempo
    def busca(self, id_busca, no=None):
        if no is None:
            no = self.raiz
        for i, chave in enumerate(no.chaves):
            if chave == id_busca:
                return True
            elif chave > id_busca:
                if not no.folha:
                    return self.busca(id_busca, no.filhos[i])
                return False
        if not no.folha:
            return self.busca(id_busca, no.filhos[len(no.chaves)])
        return False
        
    @medir_tempo
    def insercao(self, id_inserir):
        raiz = self.raiz
        if len(raiz.chaves) == 2 * self.ordem - 1:
            nova_raiz = No()
            nova_raiz.filhos.append(self.raiz)
            self.dividir(nova_raiz, 0)
            self.raiz = nova_raiz

        self.inserir_nao_cheio(self.raiz, id_inserir)
        
    def dividir(self, no, indice):
        ordem = self.ordem
        no_filho = no.filhos[indice]
        meio = ordem - 1
        
        novo_no = No(folha=no_filho.folha)
        no.chaves.insert(indice, no_filho.chaves[meio])
        no.filhos.insert(indice + 1, novo_no)

        novo_no.chaves = no_filho.chaves[meio + 1:]
        no_filho.chaves = no_filho.chaves[:meio]
        
        if not no_filho.folha:
            novo_no.filhos = no_filho.filhos[meio + 1:]
            no_filho.filhos = no_filho.filhos[:meio + 1]

    def inserir_nao_cheio(self, no, id_inserir):
        i = len(no.chaves) - 1
        if no.folha:
            while i >= 0 and id_inserir < no.chaves[i]:
                i -= 1
            no.chaves.insert(i + 1, id_inserir)
        else:
            while i >= 0 and id_inserir < no.chaves[i]:
                i -= 1
            i += 1
            if len(no.filhos[i].chaves) == (2 * self.ordem) - 1:
                self.dividir(no, i)
                if id_inserir > no.chaves[i]:
                    i += 1
            self.inserir_nao_cheio(no.filhos[i], id_inserir)
            
    @medir_tempo
    def remover(self, id_remover):
        self.remover_recursivo(self.raiz, id_remover)
        if len(self.raiz.chaves) == 0:
            if self.raiz.filhos:
                self.raiz = self.raiz.filhos[0]
            else:
                self.raiz = None

    def remover_recursivo(self, no, id_remover):
        i = 0
        while i < len(no.chaves) and no.chaves[i] < id_remover:
            i += 1

        if i < len(no.chaves) and no.chaves[i] == id_remover:
            if no.folha:
                no.chaves.pop(i)
            else:
                if len(no.filhos[i].chaves) >= self.ordem:
                    no.chaves[i] = self.get_maximo(no.filhos[i])
                    self.remover_recursivo(no.filhos[i], no.chaves[i])
                elif len(no.filhos[i + 1].chaves) >= self.ordem:
                    no.chaves[i] = self.get_minimo(no.filhos[i + 1])
                    self.remover_recursivo(no.filhos[i + 1], no.chaves[i])
                else:
                    self.mesclar(no, i)
                    self.remover_recursivo(no.filhos[i], id_remover)
        elif not no.folha:
            if len(no.filhos[i].chaves) < self.ordem:
                self.balancear_filho(no, i)
            if i < len(no.filhos):
                self.remover_recursivo(no.filhos[i], id_remover)

    def balancear_filho(self, no, indice):
        filho = no.filhos[indice]
        if indice > 0 and len(no.filhos[indice - 1].chaves) >= self.ordem:
            # Redistribui com o irmão esquerdo
            irmao = no.filhos[indice - 1]
            filho.chaves.insert(0, no.chaves[indice - 1])
            no.chaves[indice - 1] = irmao.chaves.pop()
            if not irmao.folha:
                filho.filhos.insert(0, irmao.filhos.pop())
        elif indice + 1 < len(no.filhos) and len(no.filhos[indice + 1].chaves) >= self.ordem:
            # Redistribui com o irmão direito
            irmao = no.filhos[indice + 1]
            filho.chaves.append(no.chaves[indice])
            no.chaves[indice] = irmao.chaves.pop(0)
            if not irmao.folha:
                filho.filhos.append(irmao.filhos.pop(0))
        else:
            # Mesclar com o irmão
            if indice < len(no.filhos) - 1:
                self.mesclar(no, indice)
            else:
                self.mesclar(no, indice - 1)

    def mesclar(self, no, indice):
        filho_esquerdo = no.filhos[indice]
        filho_direito = no.filhos[indice + 1]
        filho_esquerdo.chaves.append(no.chaves[indice])
        filho_esquerdo.chaves.extend(filho_direito.chaves)
        filho_esquerdo.filhos.extend(filho_direito.filhos)
        no.chaves.pop(indice)
        no.filhos.pop(indice + 1)

    def get_maximo(self, no):
        while not no.folha:
            no = no.filhos[-1]
        return no.chaves[-1]

    def get_minimo(self, no):
        while not no.folha:
            no = no.filhos[0]
        return no.chaves[0]
        
    def imprimir(self):
        if not self.raiz:
            print("Árvore está vazia.")
            return
        self._imprimir_recursivo(self.raiz, nivel=0, tipo=" Raiz")

    def _imprimir_recursivo(self, no, nivel, tipo):
        # Determina o tipo de nó (Raiz, Galho ou Folha)
        tipo_no = tipo if nivel == 0 else (" Folha" if no.folha else " Galho")
        
        # Exibe o tipo do nó, o nível e as chaves
        indentacao = "    " * nivel  # Indentação para a visualização hierárquica
        print(f"{indentacao}{tipo_no} (Nível {nivel}): {no.chaves}")

        # Mostra os filhos, se houver
        if not no.folha:
            for i, filho in enumerate(no.filhos):
                # Define o tipo do próximo nó
                proximo_tipo = "Folha" if filho.folha else "Galho"
                #print(f"{indentacao}  Filho {i + 1} do {tipo_no}:")
                self._imprimir_recursivo(filho, nivel + 1, proximo_tipo)
