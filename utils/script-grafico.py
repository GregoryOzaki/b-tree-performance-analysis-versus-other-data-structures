import matplotlib.pyplot as plt

# Dados de entrada (tempo de execução em segundos)
dados = {
    "Árvore B": {
        10: [0.000022, 0.000025, 0.000041],  # [Inserção, Busca, Remoção]
        100: [0.000261, 0.000335, 0.000346],
        1000: [0.004039, 0.008891, 0.003223],
    },
    "Árvore AVL": {
        10: [0.000058, 0.000008, 0.000036],
        100: [0.000553, 0.000081, 0.000391],
        1000: [0.010116, 0.001389, 0.006978],
    },
    "Lista Encadeada": {
        10: [0.000009, 0.000005, 0.000007],
        100: [0.000588, 0.000329, 0.000256],
        1000: [0.035778, 0.045220, 0.020714],
    },
}

# Função para criar os gráficos
def plot_comparacao(dados, entrada, ax):
    funcionalidades = ["Inserção", "Busca", "Remoção"]
    cores = {"Árvore B": "red", "Árvore AVL": "green", "Lista Encadeada": "blue"}
    
    for estrutura, tempos in dados.items():
        ax.plot(funcionalidades, tempos[entrada], label=estrutura, color=cores[estrutura], marker='o')
    
    ax.set_title(f"Entrada {entrada}")
    ax.set_xlabel("Funcionalidade")
    ax.set_ylabel("Tempo de Execução (s)")
    
    # Ajuste da posição da legenda
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), borderaxespad=0.)

    ax.grid(True)

# Criando os subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Gerando gráficos para entrada 10, 100 e 1000
plot_comparacao(dados, 10, axs[0])
plot_comparacao(dados, 100, axs[1])
plot_comparacao(dados, 1000, axs[2])

# Ajustando layout
plt.tight_layout()

# Salvar o gráfico como uma imagem
output_path = "grafico_comparacao.png"  # Definir o caminho correto para salvar
plt.savefig(output_path)  # Salva o gráfico como imagem
print(f"Gráfico salvo como '{output_path}'")

# Exibir o gráfico
plt.show()
