import os
import sys
import joblib

def carregar_artefatos():
    #Procura os arquivos de modelo, scaler e label encoder na pasta 'modelo/'
    caminho_base = os.path.dirname(os.path.abspath(__file__))
    pasta_models = os.path.join(caminho_base, "modelo")
    
    caminho_rf = os.path.join(pasta_models, "modelo_rf_final.joblib")
    caminho_scaler = os.path.join(pasta_models, "scaler_original.joblib")
    caminho_le = os.path.join(pasta_models, "label_encoder.joblib")
    
    artefatos = [(caminho_rf, "Modelo RF"), (caminho_scaler, "Scaler"), (caminho_le, "LabelEncoder")]
    for path, nome in artefatos:
        if not os.path.exists(path):
            print(f"Erro: O arquivo '{nome}' não foi encontrado em '{pasta_models}'.")
            print("Certifique-se de ter gerado os modelos na pasta 'modelo/'.")
            sys.exit(1)
            
    rf_final = joblib.load(caminho_rf)
    scaler = joblib.load(caminho_scaler)
    le = joblib.load(caminho_le)
    
    print("Artefatos carregados com sucesso!")
    return rf_final, scaler, le

if __name__ == "__main__":
    carregar_artefatos()