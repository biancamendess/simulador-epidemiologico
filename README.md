# Simulador Epidemiológico Vetorial

Um simulador computacional de propagação de doenças em ambientes bidimensionais, desenvolvido com Python e NumPy.

O projeto tem como objetivo modelar como uma infecção se espalha pelo espaço e evolui ao longo do tempo, explorando operações vetorizadas, autômatos celulares e modelagem de sistemas dinâmicos.

A proposta é construir progressivamente um modelo capaz de representar diferentes cenários de disseminação, visualizar a evolução de uma epidemia e investigar como fatores espaciais e regras de transmissão influenciam sua propagação.

## Visão do projeto

O ambiente é representado inicialmente por uma grade bidimensional, em que cada célula corresponde a uma posição da área simulada. A infecção começa em uma célula inicial, o paciente zero, e se propaga para as posições vizinhas de acordo com as regras definidas no modelo.

A cada rodada, o simulador atualiza o estado das células, permitindo acompanhar a expansão da infecção ao longo do tempo.

A implementação parte de um modelo determinístico simples e será ampliada gradualmente para explorar regras epidemiológicas mais sofisticadas e cenários ambientais.

## O que o simulador pretende fazer

- **Simular a propagação espacial:** representar a disseminação de uma infecção entre células vizinhas em uma grade bidimensional.
- **Acompanhar a evolução temporal:** executar múltiplas rodadas e observar como a região infectada se expande.
- **Visualizar a disseminação:** transformar as matrizes em representações visuais e desenvolver uma animação que permita acompanhar a progressão da infecção.
- **Explorar diferentes cenários de transmissão:** investigar como regras alternativas, probabilidades de contágio e condições ambientais podem alterar os resultados da simulação.
- **Incorporar dinâmica epidemiológica:** evoluir de um modelo binário para uma representação inspirada no modelo SEIR, distinguindo indivíduos suscetíveis, expostos, infecciosos e recuperados.
- **Investigar a influência do ambiente:** explorar fatores como direção predominante de propagação, barreiras espaciais e características do terreno na dinâmica da infecção.

Essas funcionalidades serão desenvolvidas por etapas, começando pela propagação espacial e avançando para modelos mais elaborados.

## Como o modelo funciona

O simulador utiliza uma matriz NumPy para representar o ambiente. Cada posição contém um estado que determina a condição daquela célula.

No protótipo atual, os estados são:

- `0`: saudável.
- `1`: infectada.

A simulação começa com uma célula infectada. Em cada rodada, o algoritmo identifica os vizinhos ortogonais das células infectadas, seleciona as células saudáveis que estão ao lado delas e atualiza seus estados.

A propagação considera as quatro direções principais: cima, baixo, esquerda e direita. As bordas da matriz são tratadas explicitamente para impedir que posições opostas do ambiente sejam consideradas vizinhas por causa dos deslocamentos circulares.

O processo é repetido usando o resultado da rodada anterior, permitindo observar a expansão progressiva da região infectada.

## Desenvolvimento atual

O projeto está em desenvolvimento incremental.

- [x] Construção da grade bidimensional.
- [x] Definição do paciente zero.
- [x] Identificação de vizinhos com `np.roll`.
- [x] Operações vetorizadas e máscaras booleanas para identificar novas infecções.
- [x] Tratamento das bordas da matriz.
- [x] Propagação da infecção em múltiplas rodadas.
- [ ] Visualização espacial com Matplotlib.
- [ ] Animação da evolução da infecção.
- [ ] Experimentação com diferentes regras e probabilidades de transmissão.
- [ ] Introdução de estados epidemiológicos e períodos de incubação.
- [ ] Exploração de fatores ambientais e barreiras espaciais.

## Tecnologias e conceitos

**Tecnologias**
- Python
- NumPy
- Matplotlib
- Git e GitHub

**Conceitos explorados**
- Computação científica com Python.
- Manipulação vetorizada de matrizes.
- Indexação e máscaras booleanas.
- Autômatos celulares.
- Simulação de sistemas dinâmicos.
- Modelagem e visualização de processos espaciais.

## Como executar

Clone o repositório:

```bash
git clone https://github.com/biancamendess/simulador-epidemiologico.git
cd simulador-epidemiologico
```

Crie e ative um ambiente virtual no Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instale o NumPy:

```bash
python -m pip install numpy
```

Execute o protótipo:

```bash
python main.py
```

## Limitações

O modelo atual utiliza regras simplificadas e determinísticas. Ele não considera, nesta etapa, fatores como probabilidade de transmissão, duração da infecção, recuperação ou dados epidemiológicos reais.

O simulador é um projeto de estudo em modelagem computacional e programação científica, não uma ferramenta de previsão ou apoio a decisões epidemiológicas reais.

## Objetivo de aprendizagem

Desenvolver um projeto de software incremental para explorar, na prática, como estruturas de dados, operações vetorizadas, visualização e regras matemáticas podem ser combinadas na construção de uma simulação espacial e temporal.
