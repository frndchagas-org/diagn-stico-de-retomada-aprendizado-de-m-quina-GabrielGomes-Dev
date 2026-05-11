[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ARkoM8Jo)
# Diagnóstico de retomada - Aprendizado de Máquina

Esta atividade serve para mapear o que você já domina em Aprendizado de Máquina depois das atividades anteriores da disciplina.

Responda individualmente. Use suas palavras. Rode o código quando possível. Se usar IA depois da primeira tentativa, registre o uso na seção 8.

Prazo: 11/05/2026 às 23:59, horário de Fortaleza.

## 1. Mapa do que eu lembro

Marque cada tópico como: lembro bem, lembro parcialmente, não lembro, nunca vi ou não tenho certeza.

- vetores, matrizes e produto escalar: lembro bem
- média, desvio padrão e correlação: lembro bem
- probabilidade condicional e Teorema de Bayes: lembro bem
- regressão linear: lembro bem
- classificação supervisionada: lembro bem
- treino, teste e validação: lembro bem
- normalização ou padronização de dados: lembro bem
- KNN: lembro parcialmente
- árvore de decisão: lembro bem
- matriz de confusão: lembro parcialmente
- acurácia, precisão, recall e F1-score: lembro bem
- overfitting e underfitting: lembro bem
- validação cruzada: lembro bem
- Random Forest: lembro bem
- XGBoost ou boosting: não lembro
- `predict_proba()`: lembro bem
- SQL/ETL aplicado a dados: lembro parcialmente
- simulação de Monte Carlo: lembro bem

## 2. O que foi trabalhado antes

Explique, em 8 a 12 linhas:

### 1. quais desses tópicos você lembra de ter trabalhado na disciplina;
R: Lembro-me de trabalhar com todos esses temas nas atividades da disciplina. No entanto, certos conteúdos (como KNN, Matriz de Confusão, XGBoost e SQL/ETL) não foram executados diretamente por mim, pois os trabalhos eram realizados em grupo, o que limitou meu aprofundamento prático nessas frentes. Por outro lado, participei ativamente das pesquisas e elaborações das demais soluções, o que contribuiu para o meu entendimento do conteúdo como um todo.

### 2. quais atividades ou exemplos você lembra;
R: Uma das primeiras atividades desenvolvidas consistiu na resolução de problemas em Python, onde implementamos conceitos fundamentais para o Aprendizado de Máquina, como Média e Desvio Padrão para estatísticas de notas de alunos, Probabilidade Condicional (P(A|B)), Teorema de Bayes, entre outros. Outra entrega relevante foi o desenvolvimento de um modelo de Regressão Linear para estimar valores de aluguéis. Esse projeto permitiu uma imersão profunda no ciclo de vida de um projeto de Ciência de Dados: pré-processamento, divisão de dados (treino/teste), ajuste de coeficientes e avaliação de métricas. Essas experiências foram fundamentais para despertar meu interesse por essa área, que anteriormente parecia complexa e distante.

### 3. o que você conseguiu fazer com autonomia;
R: As atividades sob minha responsabilidade foram conduzidas com autonomia. Utilizei, como fonte primária de conhecimento, os materiais (livros e artigos) indicados pelo professor e, de forma complementar, pesquisas na internet e revisões por meio de Inteligência Artificial. Como resultado, considero ter consolidado a maior parte do conteúdo e entregado resultados tecnicamente consistentes.

### 4. o que você só conseguiu fazer seguindo roteiro;
R: O suporte prático fornecido pelo docente, por meio de um roteiro estruturado, foi determinante para a compreensão da sequência lógica de desenvolvimento de um modelo de Regressão Linear. Sem esse passo a passo inicial, a articulação das etapas do processo seria uma barreira razoavelmente complexa para o grupo. Esse exemplo serviu como uma base sólida que nos permitiu organizar o fluxo de trabalho (pipeline) e entender a maneira ideal de conduzir e dividir cada fase do projeto.

### 5. qual assunto precisa ser retomado com mais urgência.
R: Quanto ao conteúdo de XGBoost, considero que o nível de aprendizado foi inferior aos demais tópicos. A discussão em sala de aula não foi exaustiva e a dinâmica de divisão de tarefas no grupo resultou na execução desse método por apenas um membro. Por esse motivo, sinto que o meu contato com a ferramenta foi superficial, restando como um tópico que demanda estudo autônomo posterior para uma compreensão plena de seu funcionamento e aplicação.

## 3. Conceitos essenciais

Responda com suas palavras e dê um exemplo simples.

### 1. O que é aprendizado supervisionado?
R: Aprendizado supervisionado é uma técnica que usa conjuntos de dados rotulados para treinar algoritmos. Nesse processo, o modelo recebe pares de entrada e saída, aprendendo a relacionar variáveis que, posteriormente, permitirão que o modelo faça previsões ou classificações com dados novos. Um exemplo prático desenvolvido na disciplina foi o modelo de Regressão Linear, que utilizou um DataFrame contendo características de imóveis para prever seus respectivos valores de aluguel.

### 2. O que é uma tarefa de classificação?
R: A classificação é uma tarefa de aprendizado supervisionado que visa predizer a qual categoria ou classe uma determinada instância pertence. O modelo é treinado para mapear um conjunto de atributos e associá-los a um rótulo predefinido. Um exemplo prático abordado na disciplina foi a aplicação dos algoritmos KNN e XGBoost para a classificação binária de pacientes (doentes vs. saudáveis), permitindo a identificação de padrões em dados clínicos para dar suporte ao diagnóstico.

### 3. O que são features e target?
R: As features (ou atributos) compreendem o conjunto de variáveis independentes que servem como dados de entrada para o modelo; são os fatores analisados pelo algoritmo para a identificação de padrões. Já o target representa a variável dependente, ou alvo, que o modelo deve aprender a predizer. No cenário clínico citado anteriormente, as features seriam os indicadores dos pacientes (como idade, pressão arterial e níveis de glicose), enquanto o target seria a classe diagnóstica final ("Saudável" ou "Doente").

### 4. Para que serve separar treino e teste?
R: A separação entre conjuntos de treino e teste é fundamental para avaliar a capacidade de generalização do modelo. O conjunto de treino é utilizado para o ajuste dos parâmetros do algoritmo, permitindo que ele aprenda os padrões intrínsecos aos dados. Já o conjunto de teste atua como um simulador de "dados do mundo real", servindo para validar o desempenho final. No modelo de previsão de aluguéis, por exemplo, ao utilizarmos uma proporção de 80% para treino e 20% para teste, submetemos o modelo a dados que ele não conheceu durante o ajuste. Isso nos permite comparar estatisticamente o valor previsto com o valor real, aferindo a precisão da ferramenta antes de sua aplicação prática.

### 5. O que é overfitting?
R: O overfitting (ou sobreajuste) acontece quando o modelo "decora" os dados de treinamento em vez de aprender os padrões gerais. Ele se torna tão específico para aquele conjunto inicial (capturando até mesmo erros) que acaba perdendo a capacidade de acertar novos casos. No modelo de previsão de aluguéis, o overfitting ocorreria se o algoritmo desse importância a um detalhe irrelevante dos dados de treino (como uma cor de parede muito específica) para definir o preço.

### 6. Por que acurácia pode ser uma métrica enganosa?
R: A acurácia pode ser uma métrica enganosa em conjuntos de dados desbalanceados, onde a frequência de uma classe supera drasticamente a outra. Nesses cenários, o modelo pode atingir um alto índice de acerto apenas ao predizer a classe majoritária, falhando em identificar a classe minoritária que, geralmente, é o alvo de maior interesse. No caso da classificação de pacientes (Doente vs. Saudável), em um grupo de 100 indivíduos onde 99 são saudáveis e apenas 1 está doente, um modelo que classifique todos como "saudáveis" atingiria 99% de acurácia. Contudo, esse resultado oculta a incapacidade total do sistema em detectar o único paciente que necessita de tratamento, o que evidencia que a acurácia, isoladamente, é insuficiente para validar a precisão do modelo.

## 4. Diagnóstico prático com Scikit-Learn

No arquivo `diagnostico_ml.py`, use o dataset `load_breast_cancer` do Scikit-Learn e faça:

1. carregue os dados;
2. separe `X` e `y`;
3. divida em treino e teste;
4. treine uma regressão logística;
5. treine uma árvore de decisão;
6. mostre matriz de confusão, acurácia, precisão, recall e F1-score para cada modelo;
7. compare o desempenho em treino e teste;
8. escreva aqui qual modelo generalizou melhor e por quê.

Se não conseguir terminar tudo, registre até onde chegou e qual erro apareceu.

### Resultados

Cole aqui os principais resultados do seu código.

```text

```

### Interpretação

Qual modelo generalizou melhor? Explique usando as métricas e a comparação entre treino e teste.

Resposta:

## 5. Probabilidade e interpretação

Escolha um dos modelos treinados e responda:

1. O modelo produz probabilidade com `predict_proba()`?
2. O que significa uma probabilidade alta para uma classe?
3. Probabilidade alta garante que a previsão está correta? Explique.
4. Em um problema real, qual seria o risco de confiar cegamente nessa previsão?

Resposta:

## 6. Generalização

Compare treino e teste:

1. Há sinal de overfitting?
2. Há sinal de underfitting?
3. O que você tentaria mudar para melhorar o resultado?
4. O que você precisaria estudar melhor para responder com mais segurança?

Resposta:

## 7. Ponto de dificuldade

Escolha um tópico da lista inicial e escreva:

1. o que você entende dele;
2. onde você se confunde;
3. que tipo de explicação ajudaria: exemplo no quadro, notebook guiado, exercício curto, revisão matemática, visualização ou projeto pequeno.

Resposta:

## 8. Uso de IA, se houver

Se você usou IA depois da primeira tentativa, registre:

```text
Pergunta feita:
Resumo da resposta:
Como eu verifiquei:
O que eu alterei na minha resposta:
O que ainda não entendi:
```

## Submissão no Moodle

Depois de finalizar, copie no Moodle:

```text
Repositório:
Commit final:
Autoavaliação: nível atual, maior dificuldade e tópico que precisa ser retomado.
```
