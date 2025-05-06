from medidor_tempos import medir_tempo, tempos_insercao, tempos_remocao, tempos_busca, tempos_total
from arvore_b import (
    ArvoreB,
)

contador_antropologicos = 0
contador_naturais = 0


def coletar_dados_usuario():
    data_registro = input("Data de Registro (dd/mm/yyyy): ")
    tipo_desastre = input("Tipo de Desastre (1 para AntropolC3gico, 2 para Natural): ")
    tipo_desastre = "A" if tipo_desastre == "1" else "N"
    return gerar_id(data_registro, tipo_desastre)


def gerar_id(data_registro, tipo_desastre):
    global contador_antropologicos, contador_naturais

    if tipo_desastre == "A":
        contador_antropologicos += 1
        numero_desastre = contador_antropologicos
    elif tipo_desastre == "N":
        contador_naturais += 1
        numero_desastre = contador_naturais

    ano = data_registro.split("/")[2]
    id_novo = f"DAM{ano}{str(numero_desastre).zfill(2)}{tipo_desastre}"
    return id_novo

def exibir_tempos():
    # Exibir tempos de inserção por ID
    print("\nTempos de execução de inserção por ID:")
    total_insercao = 0  # Variável para acumular os tempos de inserção
    for id_inserir, tempos in tempos_insercao.items():
        total_insercao_id = sum(tempos)  # Somando todos os tempos de um ID
        print(f"tempo de execução de inserção do ID {id_inserir} = {total_insercao_id:.6f}")
        total_insercao += total_insercao_id  # Acumula o tempo total de inserção

    # Exibir tempo total de inserção e média
    media_insercao = total_insercao / len(tempos_insercao) if tempos_insercao else 0
    print(f"\ntempo de execução total função inserção = {total_insercao:.6f}")  # Soma dos tempos de execução de inserção
    print(f"tempo de execução média função inserção = {media_insercao:.6f}")  # Média de execução de inserção

    # Exibir tempos de remoção por ID
    print("\nTempos de execução de remoção por ID:")
    total_remocao = 0  # Variável para acumular os tempos de remoção
    for id_remover, tempos in tempos_remocao.items():
        total_remocao_id = sum(tempos)  # Somando todos os tempos de um ID
        print(f"tempo de execução de remoção do ID {id_remover} = {total_remocao_id:.6f}")
        total_remocao += total_remocao_id  # Acumula o tempo total de remoção

    # Exibir tempo total de remoção e média
    media_remocao = total_remocao / len(tempos_remocao) if tempos_remocao else 0
    print(f"\ntempo de execução total função remoção = {total_remocao:.6f}")  # Soma dos tempos de execução de remoção
    print(f"tempo de execução média função remoção = {media_remocao:.6f}")  # Média de execução de remoção

    # Exibir tempos de busca por ID
    print("\nTempos de execução de busca por ID:")
    total_busca = 0  # Variável para acumular os tempos de busca
    for id_busca, tempos in tempos_busca.items():
        total_busca_id = sum(tempos)  # Somando todos os tempos de um ID
        print(f"tempo de execução de busca do ID {id_busca} = {total_busca_id:.6f}")
        total_busca += total_busca_id  # Acumula o tempo total de busca

    # Exibir tempo total de busca e média
    media_busca = total_busca / len(tempos_busca) if tempos_busca else 0
    print(f"\ntempo de execução total função busca = {total_busca:.6f}")  # Soma dos tempos de execução de busca
    print(f"tempo de execução média função busca = {media_busca:.6f}")  # Média de execução de busca

    # Exibir tempos totais e médios de todas as operações
    print("\nTempos totais e médios de todas as funções:")
    total_tempo = total_insercao + total_remocao + total_busca
    media_tempo = total_tempo / 3 if 3 > 0 else 0  # Média do total de execução das funções
    print(f"tempo de execução total das funções = {total_tempo:.6f}")  # Soma total dos tempos das funções
    print(f"tempo de execução média das funções = {media_tempo:.6f}")  # Média total de execução das funções


def exemplo():
    arvore_b = ArvoreB(3)
    
    cont_insercoes = 0
    cont_buscas = 0
    cont_remocoes = 0
    cont_buscas_encontradas = 0
    cont_buscas_nao_encontradas = 0
    cont_remocoes_sucesso = 0
    
    for _ in range(0):
        id_novo = coletar_dados_usuario()
        arvore_b.insercao(id_novo)
        cont_insercoes += 1
    arvore_b.imprimir()
    
    # Inserção de IDs na árvore B
    ids = [
        "DAM204801N", "DAM199112A", "DAM201715N", "DAM208906A", "DAM197310N", "DAM198701N",
        "DAM207801A", "DAM197106N", "DAM215215N", "DAM195701N", "DAM202309A", "DAM199102N",
        "DAM201803A", "DAM206712N", "DAM198512N", "DAM200404N", "DAM205908A", "DAM196111N",
        "DAM203202N", "DAM198811A", "DAM208004N", "DAM199702A", "DAM214315N", "DAM197802N",
        "DAM201109A", "DAM207715N", "DAM200103N", "DAM199804A", "DAM213514N", "DAM197901A",
        "DAM210213N", "DAM198608A", "DAM205905N", "DAM202702A", "DAM200508N", "DAM196404N",
        "DAM212013N", "DAM199805A", "DAM206601N", "DAM198712N", "DAM203906A", "DAM197501N",
        "DAM209715N", "DAM201214A", "DAM199905N", "DAM205111A", "DAM208412N", "DAM197208N",
        "DAM211307A", "DAM200812N", "DAM199410A", "DAM197906N", "DAM203508A", "DAM214102N",
        "DAM202608A", "DAM198910N", "DAM211112A", "DAM199602N", "DAM205310A", "DAM206108N",
        "DAM201902A", "DAM197412N", "DAM203215A", "DAM209618N", "DAM210507A", "DAM198604N",
        "DAM207408A", "DAM199304N", "DAM211711A", "DAM200906N", "DAM196309A", "DAM213610N",
        "DAM208208A", "DAM199601N", "DAM199900A", "DAM202101A", "DAM203305A", "DAM199813N",
        "DAM204702A", "DAM207309N", "DAM198502A", "DAM211008N", "DAM199617A", "DAM202506A",
        "DAM209901N", "DAM198402N", "DAM210504A", "DAM207612A", "DAM199612A", "DAM199806A",
        "DAM205709N", "DAM200702N", "DAM196910A", "DAM200302N", "DAM204214A", "DAM198103N",
        "DAM201511A", "DAM206309A", "DAM289408A", "DAM199507A"
    ]
    
    for id in ids:
        arvore_b.insercao(id)
        cont_insercoes += 1
    
    # Exibe a árvore após todas as inserções
    arvore_b.imprimir()
    
    # IDs para busca
    id_busca = [
        'DAM205310A', 'DAM199905N', 'DAM204801N', 'DAM201803A', 'DAM201902A', 'DAM207309N',
        'DAM203508A', 'DAM203305A', 'DAM204214A', 'DAM199806A', 'DAM199805A', 'DAM207612A',
        'DAM201214A', 'DAM201715N', 'DAM199410A', 'DAM198502A', 'DAM210213N', 'DAM208906A',
        'DAM207408A', 'DAM207418N', 'DAM213610N', 'DAM214102N', 'DAM198712N', 'DAM205111A',
        'DAM198402N', 'DAM199813N', 'DAM210507A', 'DAM197310N', 'DAM200508N', 'DAM203906A',
        'DAM207715N', 'DAM197901A', 'DAM209901N', 'DAM208004N', 'DAM199617A', 'DAM207801A',
        'DAM198608A', 'DAM199900A', 'DAM212013N', 'DAM206108N', 'DAM200812N', 'DAM201109A',
        'DAM199112A', 'DAM199702A', 'DAM195701N', 'DAM198811A', 'DAM206601N', 'DAM200404N',
        'DAM197106N', 'DAM198512A'
    ]
    
    for id_item in id_busca:
        cont_buscas += 1
        resultado_b = arvore_b.busca(id_item)
        if resultado_b:
            cont_buscas_encontradas += 1
            print(f"ID {id_item} encontrado na Árvore B!")
        else:
            cont_buscas_nao_encontradas += 1
            print(f"ID {id_item} não encontrado na Árvore B!")
    
    print("\nRemovendo IDs da Árvore B...")
    for id_item in id_busca:
        #cont_buscas += 1
        resultado_b = arvore_b.busca(id_item)
        if resultado_b:
            print(f"ID {id_item} encontrado na Árvore B!")
            print(f"Removendo ID: {id_item} da Árvore B")
            arvore_b.remover(id_item)
            cont_remocoes += 1
            #cont_buscas_encontradas += 1
        else:
            print(f"ID {id_item} não encontrado na Árvore B!")
            #cont_buscas_nao_encontradas += 1
            
    quantidade_final = cont_insercoes - cont_remocoes
    
    print("\n Relatório Final:")
    print(f" Quantidade inicial de IDs na árvore: {cont_insercoes}")
    print(f" Número total de buscas realizadas: {cont_buscas}")
    print(f" Número de buscas encontradas: {cont_buscas_encontradas}")
    print(f" Número de buscas não encontradas: {cont_buscas_nao_encontradas}")
    print(f" Número total de remoções realizadas: {cont_remocoes}")
    print(f" Quantidade final de IDs na árvore: {quantidade_final}")
    print(f" Árvore B imprimida:")
    arvore_b.imprimir()
    
if __name__ == "__main__":
    exemplo()

exibir_tempos()
