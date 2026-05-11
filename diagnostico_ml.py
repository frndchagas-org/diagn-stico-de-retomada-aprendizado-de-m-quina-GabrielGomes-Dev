"""Diagnóstico de retomada em Aprendizado de Máquina.

Complete os TODOs, rode o arquivo e copie os resultados principais para o
README.md.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def avaliar_modelo(nome, modelo, x_train, x_test, y_train, y_test):
    """Treina, prediz e imprime métricas simples."""
    print(f"\n{'='*40}")
    print(f"Avaliação do Modelo: {nome}")
    print(f"\n{'='*40}")
    
    # TODO 5: treine o modelo com os dados de treino.
    modelo.fit(x_train, y_train)

    # TODO 6: gere as previsões para treino e teste.
    y_pred_train = modelo.predict(x_train)
    y_pred_test= modelo.predict(x_test)

    # TODO 7: imprima acurácia de treino, acurácia de teste, precisão, recall,
    # F1-score e matriz de confusão usando as funções importadas acima.
    print(f"Acurácia (Treino): {accuracy_score(y_train, y_pred_train):.4f}")
    print(f"Acurácia (Teste): {accuracy_score(y_test, y_pred_test):.4f}")
    print(f"Precisão (Teste): {precision_score(y_test, y_pred_test):.4f}")
    print(f"Recall (Teste): {recall_score(y_test, y_pred_test):.4f}")
    print(f"F1-Score (Teste): {f1_score(y_test, y_pred_test):.4f}")
    print("\nMatriz de Confusão (Teste):")
    print(confusion_matrix(y_test, y_pred_test))

    # TODO 8: se o modelo tiver predict_proba, mostre as probabilidades das
    # cinco primeiras amostras de teste.
    if hasattr(modelo, "predict_proba"):
        print("\nProbabilidades das 5 primeiras amostras de teste:", modelo.predict_proba(x_test[:5]))
        
def main():
    # TODO 1: carregue o dataset load_breast_cancer().
    data = load_breast_cancer()

    # TODO 2: separe os dados de entrada em X e o alvo em y.
    X = data.data
    y = data.target

    # TODO 3: imprima informações básicas: nomes das primeiras features,
    # classes, quantidade de exemplos e quantidade de features.
    print("--- Informações do Dataset ---")
    print(f"Primeiras features: {data.feature_names[:5]}")
    print(f"Classes: {data.target_names}")
    print(f"Quantidade total de exemplos: {X.shape[0]}")
    print(f"Quantidade de features: {X.shape[1]}")

    # TODO 4: divida X e y em treino e teste com train_test_split.
    # Use test_size=0.25, random_state=42 e stratify=y.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

    # TODO 9: crie uma regressão logística e uma árvore de decisão.
    modelo_logistico = LogisticRegression(max_iter=10000, random_state=42)
    modelo_arvore = DecisionTreeClassifier(random_state=42)

    # TODO 10: chame avaliar_modelo para os dois modelos.
    avaliar_modelo("Regressão Logística", modelo_logistico, X_train, X_test, y_train, y_test)
    avaliar_modelo("Árvore de Decisão", modelo_arvore, X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()
