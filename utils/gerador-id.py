# Inicializacao das variaveis globais
contador_antropologicos = 0
contador_naturais = 0


def coletar_dados_usuario():
    data_registro = input("Data de Registro (dd/mm/yyyy): ")
    tipo_desastre = input("Tipo de Desastre (1 para Antropologico, 2 para Natural): ")
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
