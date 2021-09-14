# Projeto da mentoria Data Science Academy

[![author](https://img.shields.io/badge/author-RafaelGallo-red.svg)](https://github.com/RafaelGallo?tab=repositories) 
[![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-374/) 
[![](https://img.shields.io/badge/Pandas-blue.svg)](https://pandas.pydata.org/) 
[![](https://img.shields.io/badge/Matplotlib-blue.svg)](https://matplotlib.org/)
[![](https://img.shields.io/badge/plotly-green.svg)](https://plotly.com/)
[![](https://img.shields.io/badge/Seaborn-green.svg)](https://seaborn.pydata.org/)
[![](https://img.shields.io/badge/Matplotlib-orange.svg)](https://scikit-learn.org/stable/) 
[![](https://img.shields.io/badge/Scikit_Learn-green.svg)](https://scikit-learn.org/stable/)
[![](https://img.shields.io/badge/Numpy-White.svg)](https://numpy.org/)

![](https://github.com/RafaelGallo/Mentoria-machine-learning---DSA-2021/blob/main/src/25332.jpg)

# Projeto 01 - Churn
Customer Churn (ou Rotatividade de Clientes, em uma tradução livre) refere-se a uma decisão tomada pelo cliente sobre o término do relacionamento comercial. Refere-se também à perda de clientes. A fidelidade do cliente e a rotatividade de clientes sempre somam 100%. Se uma empresa tem uma taxa de fidelidade de 60%, então a taxa de perda de clientes é de 40%. De acordo com a regra de lucratividade do cliente 80/20, 20% dos clientes estão gerando 80% da receita. Portanto, é muito importante prever os usuários que provavelmente abandonarão o relacionamento comercial e os fatores que afetam as decisões do cliente.

Neste projeto, você deve prever o Customer Churn em uma Operadora de Telecom.

* O que é Churn? **

Churn, numa definição mais generalista, é uma métrica que indica o número de clientes que cancelam em determinado período de tempo. Para calcular o churn, o que você precisa fazer é somar o número de clientes que cancelou seu produto/serviço no período analisado.

Churn = total de clientes cancelados
Para que uma empresa consiga fazer a expansão da sua base de clientes, é preciso que o número de novos clientes exceda o seu churn rate – a taxa de clientes cancelados.

* Como fazer para calcular a sua taxa de churn?**
A taxa de churn geralmente é calculada num determinado período, seja anual, semestral ou mensal.

Por exemplo: se 1 de cada 20 clientes cancelam seu produto todo mês, isso representa que a taxa de churn para seu produto será de 5%.

Você também pode calcular a taxa de churn, que irá representar o percentual de contas que estão cancelando em comparação com a base de cliente ativos, da seguinte forma:

Churn Rate: total de clientes cancelados / número total de clientes ativos do último mês

* Qual a diferença entre Churn e Churn de receita (ou MRR Churn)?**
A diferença é simples. *Churn rate* representa o número de clientes que cancelam num determinado período, já o *Churn de Receita* representa o quanto de receita é perdida dentro desse lote de clientes.


![image](https://user-images.githubusercontent.com/72530507/131258231-370315c1-dc6a-482d-88fd-c5aa2351944f.png)


* Churn de Receita ou MRR Churn**
MRR significa Monthly Recurring Revenue (receita recorrente mensal). Vamos explicar usando um exemplo simples onde 3 clientes cancelaram a assinatura num determinado mês.

Digamos que o primeiro cliente pagava R$100/mês, o segundo R$200/mês e o terceiro R$250/mês. O seu churn de receita nesse período será a soma dos valores que os clientes pagavam, encontrando o seu MRR Churn.

MRR CHURN = SUM (MRR dos clientes cancelados)
O MRR Churn também pode ser calculado em percentuais, representando o quanto isso equivale quando olharmos para o total de MRR do mês.

MRR CHURN % = MRR Churn / MRR último mês
Algo interessante sobre a análise do MRR churn é o insight que ele possibilita sobre downgrades e upgrades, duas métricas muito importantes que não são medidas pelo churn rate, por exemplo.

Em muitos casos o MRR Churn acaba sendo mais importante que o churn rate, isso somente se as contas que estão saindo são contas de baixa receita. Porém, existe um contrapeso para compensar esse furo. É importante que seus maiores e mais importantes clientes continuem ativos e crescendo, o que significa trazer mais receita.


# Projeto 02 - Bitcoin

Título: Análise de dados de criptomoedas para predição do seu valor no mercado
1)Descrição

Criptomoedas são moedas digitais que não existem fisicamente e não são emitidas por nenhum governo. Elas têm três principais funções: 1) servir como meio de troca, facilitando as transações comerciais; 2) reserva de valor, para a preservação do poder de compra no futuro; 3) unidade de conta, quando os produtos são precificados e o cálculo econômico é realizado em função dela (Infomoney, 2021).

Uma desvantagem importante é que o preço das criptomoedas apresenta grande volatilidade (Infomoney, 2021). Seu preço varia conforme oferta e demanda. Além disso, elas ainda possuem baixo grau de aceitação nos estabelecimentos, por enquanto. Existe um risco de que os usuários apaguem ou percam suas moedas além de ser necessário se proteger da ação de hackers (Infomoney, 2021).

Algoritmos de Machine Learning têm sido amplamente utilizados no mercado financeiro com o intuito de prever preço de ações (listei referencias para ler depois no tópico). Os modelos mais utilizados para essa tarefa são métodos ensemble LSTMs e redes neurais recorrentes.

2)Problema a ser analisado:

O problema a ser analisado aqui será prever o preço de criptomoedas baseado em dados disponíveis de mercado. Além disso, notícias e interações nas redes sociais tem impacto no preço e, portanto, serão adicionados a análise.

Inicialmente o modelo será treinado com dados de valores de Bitcoin (BTC) por ser a mais famosa e depois de ter um modelo e estratégia clara funcionando, testar com outras criptomoedas. Outras criptomoedas: Bitcoin Cash (nova versão do Bitcoin), Ethereum (ETH), Tether (USDT), Ripple (XRP), Litecoin (LTC) etc.

3) Dicionário de dados:

• Os dados utilizados serão preços das ações num intervalo de tempo.

• Tweets de páginas e assuntos que possam ter impacto no modelo.

• Podem ser incorporados notícias e outras fontes futuramente.

4)Objetivos:

• Modelo de Machine Learning para preços das açoes

o Conexão do python com o site que possui os valores das ações através da API ou pacote binance.

o Revisão de literatura para ver ferramentas que já estão sendo usadas

o Treinamento do modelo-base – provavelmente uma rede neural

o Avaliação do modelo e ajustes

• Análise de Sentimento dos Tweets para incorporar ao modelo

o Coleta dos tweets através da API

o Análise de sentimento e rankeamento dos tweets relacionados ao tema

• Incorporar análise de sentimentos ao modelo de predição das ações

o Revisão de literatura sobre o tema e como fazer

• Relatório e deploy

5)Datas :

1 etapa : 22/08 - etl, decomposição série temporal, verificar estacionaridade

2 etapa : 19/09 - forecasting : ARIMA, SARIMA, ARMA, Prophet, Kats, LSTM

3 etapa : 26/09 - relatorio final
