import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np

try: 
    df = pd.read_csv('C:/Users/Guilherme/Documents/faculdade/prog.sistemas especialistas/trabalho fabrica sustentavel/fabrica_energia.csv')
    print("ARQUIVO LIDO COM SUCESSO! AQUI ESTÃO AS 10 ULTIMAS LINHAS:")
    print(df.tail(10))
    print("____________________________________________________________")
    print("verificando os tipos de dados de cada coluna:")
    print(df.info())
    print("____________________________________________________________")
    
    nome_coluna_energia = 'consumo_kwh'
    df[nome_coluna_energia] = pd.to_numeric(df[nome_coluna_energia], errors='coerce')
    df.dropna(subset=[nome_coluna_energia], inplace=True)
    
    media_consumo = df[nome_coluna_energia].mean()
    desvio_padrao = df[nome_coluna_energia].std()
    energia_total = df[nome_coluna_energia].sum()
      
    print("\n--- Análise de Consumo de Energia ---")
    print(f"Energia Total Consumida: {energia_total:.2f} kWh")
    print(f"Média de Consumo por Dia: {media_consumo:.2f} kWh")
    print(f"Desvio Padrão do Consumo: {desvio_padrao:.2f} kWh")
    print("__________________________________________________________")

    print("analise por maquina")
    print("__________________________________________________________")
    grupo_por_maquina = df.groupby('maquina')
    consumo_total_por_maquina = grupo_por_maquina[nome_coluna_energia].sum()
    print("\nconsumo total por maquina:")
    print(consumo_total_por_maquina)
    
    consumo_medio_por_maquina = grupo_por_maquina[nome_coluna_energia].mean()
    print("\nconsumo medio por maquina")
    print(consumo_medio_por_maquina)
    print("__________________________________________________________")
    
    desvio_padrao_por_maquina = grupo_por_maquina[nome_coluna_energia].std()
    print("\ndesvio padrao por maquina")
    print(desvio_padrao_por_maquina)
    print("___________________________________________________________")
    
    print("resumo completo com .agg()")
    resumo_completo = df.groupby('maquina')[nome_coluna_energia].agg(['sum', 'mean', 'std'])
    
    resumo_completo.rename(columns={
        'sum': 'energia total (kwh)', 
        'mean': 'media de consumo (kwh)',
        'std': 'desvio padrao (kwh)'
    }, inplace=True)
    print(resumo_completo.round(2))
    print("__________________________________________________________")
    
    print("analise de produção")
    indice_maior_producao = df[nome_coluna_energia].idxmax()
    indice_menor_producao = df[nome_coluna_energia].idxmin()
    dia_maior_producao = df.loc[indice_maior_producao]
    dia_menor_producao = df.loc[indice_menor_producao]
    
    print("\nDIA DE MAIOR PRODUÇÃO")
    print(dia_maior_producao)
    
    print("\nDIA DE MENOR PRODUÇÃO")
    print(dia_menor_producao)
    print("___________________________________________________________")
    
    print("gerando grafico de dispersão")
    print("por favor, aguarde. o grafico sera exibido em uma nova janela")
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x='horas_trabalhadas',
        y='consumo_kwh',
        hue='maquina',
        style='maquina',
        s=100,
        data=df
    )

    plt.title('relação entre horas trabalhadas e consumo de energia', fontsize=16)
    plt.xlabel('horas trabalhadas', fontsize=12)
    plt.ylabel('consumo de energia (kwh)', fontsize=12)
    
    plt.legend(title='maquina')
    plt.show()
    
    print("gerando grafico de linhas")
    print("por favor, aguarde. o grafico sera exibido em uma nova janela")
    
    sns.set_style("whitegrid")
    plt.figure(figsize=(12,6))
    sns.lineplot(
        data=df,
        x='dia',
        y='consumo_kwh',
        hue='maquina',
        style='maquina',
        markers=True,
        dashes=False,
        linewidth=2.5
    )
    
    plt.title('consumo de energia (kwh) ao longo dos dias', fontsize=16)
    plt.xlabel('dias', fontsize=12)
    plt.ylabel('consumo de energia(kwh)',fontsize=12)
    
    plt.xticks(df['dia'])
    plt.legend(title='maquina')
    plt.show()
    
    print("adicionando coluna 'alto_consumo'")
    media_geral_consumo = df[nome_coluna_energia].mean()
    print(f"a media geral de consumo e {media_geral_consumo:.2f} kwh")
    df['alto_consumo'] = np.where(df[nome_coluna_energia]> media_geral_consumo, 1, 0)
    
    print("\n dataframe atualizado com a nova coluna 'alto_consumo'")
    print(df)
    print("analise dos dias de alto consumo")
    contagem_alto_consumo = df['alto_consumo'].sum()
    print(f"\ntotal de dias com consumo acima da media {contagem_alto_consumo}")
    
    dias_de_pico = df[df['alto_consumo'] == 1]
    print("\ndetalhes dos dias com consumo acima da media")
    print(dias_de_pico)
    
    
except FileNotFoundError:
    print("erro: o arquivo nao foi encontrado. verifique o nome e o caminho do arquivo.")
except Exception as e:
    print(f"ocorreu um erro inesperado:{e}")
