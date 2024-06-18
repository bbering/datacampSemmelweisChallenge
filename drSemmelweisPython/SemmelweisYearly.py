import pandas as pd
import matplotlib.pyplot as plt

#utilizando o metodo read da dependencia pandas para ler documento csv
yearly = pd.read_csv(r"C:\Users\bberi\OneDrive\Área de Trabalho\drSemmelweisChallenge\datacampSemmelweisChallenge\drSemmelweisPython\yearly_deaths_by_clinic.csv")

#criando uma nova tabela "proportion_deaths" que recebera a porcentagem de mortes por nascimento anualmente
yearly['proportion_deaths'] = yearly['deaths'] / yearly['births'] * 100

#atribuindo todos os dados referentes a clinica 1 a dataFrame clinic1
clinic1 = yearly[yearly['clinic']=='clinic 1']

#atribuindo todos os dados referentes a clinica 2 a dataFrame clinic2
clinic2 = yearly[yearly['clinic']== 'clinic 2']

#utilizando o metodo loc para determinar um ponto de partida, a coluna deaths_mean_clinic1 recebe a media de mortes da clinica1
yearly.loc[0, 'deaths_mean_clinic'] = clinic1['proportion_deaths'].mean()

#utilizando o metodo loc para determinar um ponto de partida, a coluna deaths_mean_clinic2 recebe a media de mortes da clinica2
yearly.loc[6, 'deaths_mean_clinic'] = clinic2['proportion_deaths'].mean()

#declarando o componente grafico e seus atributos para plotar o grafico
ax = clinic1.plot(x='year', y='proportion_deaths', label = 'testesmanufaturadosclinica1', legend=True)
clinic2.plot(x='year', y='proportion_deaths', label = 'testesmanufaturadosclinica2', ax=ax, legend=True)

ax.set_ylabel("proportion deaths")

plt.show()