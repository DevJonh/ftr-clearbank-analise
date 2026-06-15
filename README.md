# Desafio Prático - Análise Financeira com Python

Projeto desenvolvido como requisito avaliativo da disciplina **Análise de Dados e Inteligência de Negócios com IA** da **FTR - Faculdade de Tecnologia Rocketseat**.

## Descrição

Este projeto realiza a análise de transações bancárias a partir de um arquivo CSV, aplicando validações, tratamento de dados, agrupamento por mês e geração de relatórios financeiros.

Além da implementação utilizando bibliotecas nativas do Python, também foram desenvolvidas as atividades opcionais com **Pandas** e **Matplotlib**.

## Funcionalidades Implementadas

### Leitura e Validação de Dados

- Leitura do arquivo `transacoes.csv` utilizando `csv.DictReader`;
- Tratamento de erro para arquivo inexistente;
- Validação dos campos:
  - id;
  - data;
  - cliente_id;
  - tipo;
  - valor.

### Processamento dos Dados

- Conversão de datas com `datetime`;
- Agrupamento das transações por mês;
- Cálculo das métricas financeiras:
  - quantidade de transações;
  - total de créditos;
  - total de débitos;
  - saldo mensal;
  - média das transações;
  - maior valor;
  - menor valor.

### Transações Suspeitas

- Identificação de movimentações acima de R$ 10.000,00.

### Exportação

- Geração do arquivo `relatorio.json`.

## Requisitos Opcionais Implementados

### RO1 - Pandas

Arquivo:

```text
analise_pandas.py
```

Implementação alternativa utilizando:

- pandas.read_csv()
- groupby()
- sum()
- mean()
- max()
- min()

### RO2 - Matplotlib

Arquivo:

```text
grafico.png
```

Gráfico gerado a partir dos resultados da análise financeira.

## Estrutura do Projeto

```text
clearbank-analise/
├── desafio-final.ipynb
├── transacoes.csv
├── relatorio.json
├── analise_pandas.py
├── grafico.png
└── README.md
```

## Como Executar

### Google Colab

1. Abrir o arquivo `desafio-final.ipynb`;
2. Executar todas as células em ordem;
3. Verificar o relatório exibido no notebook;
4. Conferir os arquivos gerados.

### Jupyter Notebook

1. Abrir o arquivo `desafio-final.ipynb`;
2. Executar todas as células;
3. Verificar a saída do relatório e os arquivos gerados.

## Arquivos Gerados

| Arquivo | Descrição |
|----------|----------|
| relatorio.json | Relatório consolidado da análise |
| grafico.png | Gráfico gerado com matplotlib |
| analise_pandas.py | Implementação alternativa utilizando pandas |

## Autor

Jônatas Senna

FTR - Faculdade de Tecnologia Rocketseat
