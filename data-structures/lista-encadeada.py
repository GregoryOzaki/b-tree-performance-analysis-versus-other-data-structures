from medidor_tempos import medir_tempo

class No:
    def __init__(self, chave):
        self.chave = chave  # Valor do nó
        self.proximo = None  # Ponteiro para o próximo nó

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None  # Ponteiro para o primeiro nó

    @medir_tempo
    def busca(self, id_busca):
        atual = self.cabeca
        while atual is not None:
            if atual.chave == id_busca:
                return True
            atual = atual.proximo
        return False

    @medir_tempo
    def insercao(self, id_inserir):
        novo_no = No(id_inserir)
        if self.cabeca is None or id_inserir < self.cabeca.chave:
            # Inserção no início da lista
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
        else:
            # Inserção ordenada no meio ou no final
            atual = self.cabeca
            while atual.proximo is not None and atual.proximo.chave < id_inserir:
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no

    @medir_tempo
    def remover(self, id_remover):
        atual = self.cabeca
        anterior = None
        while atual is not None:
            if atual.chave == id_remover:
                if anterior is None:
                    # Remoção no início da lista
                    self.cabeca = atual.proximo
                else:
                    # Remoção no meio ou no final
                    anterior.proximo = atual.proximo
                return
            anterior = atual
            atual = atual.proximo

    def imprimir(self):
        atual = self.cabeca
        elementos = []
        while atual is not None:
            elementos.append(atual.chave)
            atual = atual.proximo
        print("Lista Encadeada:", " -> ".join(elementos))
