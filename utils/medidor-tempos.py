import time

# Dicionários para armazenar os tempos das funções
tempos_insercao = {}
tempos_remocao = {}
tempos_busca = {}
tempos_total = {}

def medir_tempo(func):
    """
    Função decoradora para medir o tempo de execução das funções
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Inicia a medição do tempo
        resultado = func(*args, **kwargs)  # Chama a função original
        end_time = time.time()  # Termina a medição do tempo
        tempo_execucao = end_time - start_time
        
        # Armazenando o tempo de execução por ID
        if func.__name__ == "insercao":
            id_inserir = args[1]  # ID inserido
            if id_inserir not in tempos_insercao:
                tempos_insercao[id_inserir] = []
            tempos_insercao[id_inserir].append(tempo_execucao)
        
        elif func.__name__ == "remover":
            id_remover = args[1]  # ID removido
            if id_remover not in tempos_remocao:
                tempos_remocao[id_remover] = []
            tempos_remocao[id_remover].append(tempo_execucao)
        
        elif func.__name__ == "busca":
            id_busca = args[1]  # ID buscado
            if id_busca not in tempos_busca:
                tempos_busca[id_busca] = []
            tempos_busca[id_busca].append(tempo_execucao)
        
        # Armazenando o tempo total da função
        if func.__name__ not in tempos_total:
            tempos_total[func.__name__] = 0
        tempos_total[func.__name__] += tempo_execucao
        
        return resultado  # Retorna o resultado da função
    
    return wrapper
