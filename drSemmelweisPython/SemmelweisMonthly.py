import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#utilizando o metodo read da dependencia pandas para ler documento csv
monthly = pd.read_csv(r"C:\Users\bberi\OneDrive\Área de Trabalho\projeto python\monthly_deaths.csv", parse_dates=['date'])

#criando uma nova tabela "proportion_deaths" que recebera a porcentagem de mortes por nascimento mensalmente
monthly['proportion_deaths'] = monthly['deaths'] / monthly['births'] * 100

#a variavel handwashing start funciona de maneira semelhante a um ponto de inflexao, a partir dele, o grafico muda de comportamento
handwashing_start = pd.to_datetime('1847-06-01')

#a dataFrame before_washing recebe os dados referentes a antes do periodo onde as clinicas passaram a lavar as maos
before_washing = monthly[monthly['date'] < handwashing_start]

#a dataFrame after_washing recebe os dados referentes a depois do periodo onde as clinicas passaram a lavar as maos
after_washing = monthly[monthly['date'] > handwashing_start]

#a dataFrame at_washing recebe os dados referentes ao ponto onde se passou a lavar as maos
at_washing = monthly[monthly['date'] == handwashing_start]

#a lista boot_mean_diff receber as medias de mortes obtidas atraves do metodo bootstrap
boot_mean_diff = []

#laco onde serao calculadas as medias bootstrap com um intervalo de confianca
for i in range(3000):
    boot_before = before_washing.sample(frac=1, replace=True)['proportion_deaths']
    boot_after = after_washing.sample(frac=1, replace=True)['proportion_deaths']
    boot_mean_diff.append(boot_before.mean() - boot_after.mean())

confidence_interval = np.percentile(boot_mean_diff, [2.5, 97.5])

print("confidence interval: ", confidence_interval)

#declarando os componentes graficos
fig, ax = plt.subplots()

#plotando ambos os graficos
before_washing.plot(x='date', y='proportion_deaths', label='death percentage before', ax=ax, legend=True)
after_washing.plot(x='date', y='proportion_deaths', label='death percentage after', ax=ax, legend=True)

#plotando o ponto referente a onde se passou a lavar as maos
ax.scatter(x=at_washing['date'], y=at_washing['proportion_deaths'], color='green', marker='o', label='at washing')

ax.set_xlabel('date')
ax.set_ylabel('proportion deaths')
ax.set_title('comparison of death percentage')
ax.legend()
ax.grid()

plt.show()

#consideracao final
doctor_should_wash_their_hands = True