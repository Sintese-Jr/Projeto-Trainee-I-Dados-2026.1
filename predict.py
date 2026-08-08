import argparse
import os
import sys
import pandas as pd
import joblib

def carregar_artefatos():
    #Carrega o modelo e seus artefatos.
    caminho_base = os.path.dirname(os.path.abspath(__file__))
    pasta_models = os.path.join(caminho_base, "modelo")
    
    caminho_rf = os.path.join(pasta_models, "modelo_rf_final.joblib")
    caminho_scaler = os.path.join(pasta_models, "scaler_original.joblib")
    caminho_le = os.path.join(pasta_models, "label_encoder.joblib")
    
    artefatos = [(caminho_rf, "Modelo RF"), (caminho_scaler, "Scaler"), (caminho_le, "LabelEncoder")]
    for path, nome in artefatos:
        if not os.path.exists(path):
            print(f"❌ Erro: O arquivo '{nome}' não foi encontrado em '{pasta_models}'.")
            print("Certifique-se de ter gerado os modelos na pasta 'modelo/'.")
            sys.exit(1)
            
    rf_final = joblib.load(caminho_rf)
    scaler = joblib.load(caminho_scaler)
    le = joblib.load(caminho_le)
    
    return rf_final, scaler, le

def diagnosticar(caminho_csv):
    #Parte de predição do diagnóstico
    if not os.path.exists(caminho_csv):
        print(f"\n❌ Erro: O arquivo de dados '{caminho_csv}' não foi encontrado.")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("      DIAGNÓSTICO GENÉTICO INDIVIDUAL (RNA-Seq)")
    print("=" * 60)
    
    try:
        rf_final, scaler, le = carregar_artefatos()
        df_paciente = pd.read_csv(caminho_csv)
        colunas_ignorar = ['Class', 'Unnamed: 0', 'id', 'Id']
        df_limpo = df_paciente.drop(columns=[c for c in colunas_ignorar if c in df_paciente.columns])
        
        dados_escalados = scaler.transform(df_limpo)
        df_escalado_completo = pd.DataFrame(dados_escalados, columns=scaler.feature_names_in_)
        genes_50 = list(rf_final.feature_names_in_)
        df_50_genes = df_escalado_completo[genes_50].head(1)
        
        predicao_num = rf_final.predict(df_50_genes)[0]
        diagnostico_final = le.inverse_transform([predicao_num])[0]
        probabilidades = rf_final.predict_proba(df_50_genes)[0]
        confianca = probabilidades[predicao_num] * 100

        print("\n" + "-" * 45)
        print("          RESULTADO DO DIAGNÓSTICO")
        print("-" * 45)
        print(f"  Amostra / Paciente   : {caminho_csv}")
        print(f"  Diagnóstico Previsto : {diagnostico_final}")
        print(f"  Nível de Confiança   : {confianca:.2f}%")
        print("-" * 45 + "\n")
        
    except Exception as e:
        print(f"\n❌ Erro durante o processamento do diagnóstico: {e}\n")
        sys.exit(1)

def main():
    #aceita qualquer arquivo .csv como entrada
    parser = argparse.ArgumentParser(
        description="Ferramenta de linha de comando para predição de tipo tumoral via RNA-Seq."
    )
    parser.add_argument(
        "-c", "--csv",
        type=str,
        required=True,
        help="Caminho para o arquivo CSV contendo os dados do paciente."
    )
    
    args = parser.parse_args()
    diagnosticar(args.csv)

if __name__ == "__main__":
    main()