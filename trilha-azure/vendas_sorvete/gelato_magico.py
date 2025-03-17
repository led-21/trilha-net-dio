import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
import mlflow.sklearn

# 1. Geração de Dados Fictícios
def generate_data(file_path='sales_data.csv'):
    np.random.seed(42)
    temperaturas = np.random.uniform(15, 35, 100)  # Temperaturas entre 15°C e 35°C
    vendas = 50 + 10 * temperaturas + np.random.normal(0, 20, 100)  # Relação linear com ruído
    data = pd.DataFrame({'temperatura': temperaturas, 'vendas': vendas})
    data.to_csv(file_path, index=False)
    print(f"Dados gerados e salvos em {file_path}")

# 2. Pré-processamento dos Dados
def load_and_split_data(file_path='sales_data.csv'):
    data = pd.read_csv(file_path)
    X = data[['temperatura']]  # Feature
    y = data['vendas']         # Target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# 3. Treinamento e Registro com MLflow
def train_and_log_model():
    X_train, X_test, y_train, y_test = load_and_split_data()
    
    # Configurar MLflow
    mlflow.set_experiment("Gelato_Magico_Prediction")
    with mlflow.start_run():
        # Treinar modelo
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Avaliar modelo
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        # Logar parâmetros, métricas e modelo
        mlflow.log_param("model_type", "LinearRegression")
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2", r2)
        mlflow.sklearn.log_model(model, "model")

        print(f"Modelo treinado - MSE: {mse:.2f}, R2: {r2:.2f}")
        return mlflow.active_run().info.run_id  # Retorna o run_id para uso posterior

# 4. Pipeline Estruturado
def build_and_run_pipeline():
    X_train, X_test, y_train, y_test = load_and_split_data()

    # Criar pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),      # Normalizar os dados
        ('regressor', LinearRegression())  # Modelo de regressão
    ])

    # Treinar pipeline
    pipeline.fit(X_train, y_train)

    # Avaliar
    score = pipeline.score(X_test, y_test)
    print(f"R2 Score do Pipeline: {score:.2f}")

    # Logar com MLflow
    with mlflow.start_run():
        mlflow.sklearn.log_model(pipeline, "pipeline_model")
        mlflow.log_metric("r2_score", score)

# 5. Previsão em Tempo Real
def predict_sales(temperature, run_id):
    model_uri = f"runs:/{run_id}/model"
    model = mlflow.sklearn.load_model(model_uri)
    prediction = model.predict([[temperature]])[0]
    return prediction

# 6. Função Principal
def main():
    # Gerar dados
    generate_data()

    # Treinar e registrar modelo
    run_id = train_and_log_model()

    # Executar pipeline
    build_and_run_pipeline()

    # Fazer uma previsão exemplo
    temp = 28.0  # Temperatura exemplo
    sales_pred = predict_sales(temp, run_id)
    print(f"Previsão de vendas para {temp}°C: {sales_pred:.2f} sorvetes")

if __name__ == "__main__":
    main()
