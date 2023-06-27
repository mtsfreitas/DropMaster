# Problema: Análise de preços e popularidade de produtos em diferentes categorias

## Descrição
O objetivo deste projeto é analisar os preços e a popularidade de produtos em diferentes categorias do Mercado Livre. Inicialmente, a intenção era utilizar a API do Mercado Livre, mas essa abordagem apresentou uma limitação crucial: a API não disponibiliza a quantidade de vendas ao longo do tempo, apenas a quantidade total vendida de um produto até o momento.

Dessa forma, para realizar uma análise temporal mais precisa, optou-se por um conjunto de dados alternativo, disponível no Kaggle. Este dataset russo fornece dados históricos diários, desde janeiro de 2013 até outubro de 2015, o que permitirá identificar tendências, popularidade e padrões de comportamento do consumidor ao longo do tempo.

Por meio desta análise, será possível auxiliar vendedores a otimizar suas estratégias de preços e estoque. Modelos preditivos utilizando métodos como: regressão, árvores de decisão ou redes neurais podem ser utilizados.

## Coleta de dados
Embora a coleta de dados através da API do Mercado Livre tenha sido inicialmente considerada, a ausência de dados temporais sobre a quantidade vendida para cada produto tornou inviável essa abordagem. Em vez disso, optou-se por utilizar um conjunto de dados disponível no Kaggle, que apresenta informações detalhadas sobre as vendas diárias de diferentes produtos em várias lojas.

Esse conjunto de dados pode ser encontrado no seguinte link: https://www.kaggle.com/competitions/competitive-data-science-predict-future-sales/data

Portanto, o principal desafio deste projeto passou a ser a previsão de preços e quantidade de estoque recomendada ao longo dos meses para produtos de diferentes categorias, com base nos dados históricos disponíveis.
