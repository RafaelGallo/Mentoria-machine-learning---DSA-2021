![image](https://user-images.githubusercontent.com/72530507/131258205-918dcf59-d592-4780-85b8-0233ba24d737.png)




# Analise de Churn

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
