# Sistema de Predição de Risco de Crédito

Plataforma end-to-end para análise e classificação de risco de crédito, desenvolvida com foco em alta performance, controle de memória e modularidade. Este projeto demonstra o ciclo de vida completo de Machine Learning sem dependência exclusiva de bibliotecas de alto nível.

# Arquitetura de diretorios

*   `api/` - Responsável por receber e enviar requisições por meio de uma api rest para se comunicar com o core de treinamento.
*   `core/` - Faz o treinamento de Machine Learning utilizando o algoritmo de Random Forest.
*   `frontend/` - Utiliza o streamlit para fazer a comunicação e interação do usuário com a api. 