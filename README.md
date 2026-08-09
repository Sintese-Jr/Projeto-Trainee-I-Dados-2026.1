# 🧬 Classificação Tumoral por Expressão Gênica (RNA-Seq)

Este repositório contém uma solução completa de Machine Learning para a classificação e diagnóstico de tipos tumorais a partir de dados de sequenciamento de RNA (RNA-Seq). O projeto engloba desde o pré-processamento e análise exploratória de dados até a construção, seleção de *features* e disponibilização de uma ferramenta de inferência via linha de comando (CLI).

---

## 📌 Visão Geral do Projeto

O objetivo principal é identificar padrões de expressão gênica que diferenciam amostras de tecidos/tumores. A pipeline reduz a alta dimensionalidade dos dados genéticos (selecionando os genes mais relevantes) e utiliza um modelo de **Random Forest** para realizar diagnósticos individuais com alto nível de precisão e confiança.

---

## 📁 Estrutura do Repositório

```text
.
├── dados/                  # Datasets brutos, processados e amostras de teste (.csv)
├── modelo/                 # Artefatos salvos do modelo (.joblib)
├── notebooks/              # Notebooks da análise e modelagem
│   ├── 01_limpeza.ipynb
│   ├── 02_analise_exploratoria.ipynb
│   └── 03_modelagem.ipynb
├── .gitignore              # Regras de exclusão do Git
├── predict.py              # Script CLI para diagnóstico via terminal
└── README.md               # Documentação do projeto
```

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Linguagem:** Python 3.13+
* **Manipulação de Dados:** `pandas`, `numpy`
* **Machine Learning & Pré-processamento:** `scikit-learn` (`RandomForestClassifier`, `StandardScaler`, `LabelEncoder`)
* **Persistência de Modelos:** `joblib`
* **Interface CLI:** `argparse`

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos e Instalação

Certifique-se de ter o Python instalado. Recomenda-se a instalação das dependências utilizadas no projeto:

```bash
pip install pandas numpy scikit-learn joblib
```

---

### 2. Executando a Inferência via Terminal (CLI)

O script `predict.py` permite realizar o diagnóstico de um paciente/amostra individual passando o caminho de um arquivo CSV diretamente pela linha de comando.

#### Sintaxe Básica:

```bash
python predict.py -c "caminho/para/o/arquivo.csv"
```

#### Exemplos de Uso:

* **Passando um arquivo de teste dentro do projeto:**
  ```bash
  python predict.py -c dados/teste.csv
  ```

* **Passando um arquivo localizado em outra pasta (ex: Downloads):**
  ```bash
  python predict.py -c "C:\Users\Usuario\Downloads\paciente1.csv"
  ```

---

### 💻 Exemplo de Saída no Terminal

Ao executar o script, a ferramenta carrega dinamicamente os artefatos treinados (`modelo/`), aplica as transformações necessárias e exibe o resultado formatado:

```text
============================================================
      DIAGNÓSTICO GENÉTICO INDIVIDUAL (RNA-Seq)
============================================================

---------------------------------------------
          RESULTADO DO DIAGNÓSTICO
---------------------------------------------
  Amostra / Paciente   : dados/teste.csv
  Diagnóstico Previsto : BRCA
  Nível de Confiança   : 98.50%
---------------------------------------------
```

---

## 🔬 Pipeline de Modelagem (`notebooks/`)

1. **`01_limpeza.ipynb`**: Tratamento inicial, identificação de valores nulos e estruturação do dataset.
2. **`02_analise_exploratoria.ipynb`**: Análise estatística e distribuição da expressão dos genes.
3. **`03_modelagem.ipynb`**: Treinamento do modelo Random Forest, seleção das 50 *features* mais importantes, codificação de rótulos e exportação dos artefatos para a pasta `modelo/`.

---

## 📜 Licença

Este projeto foi desenvolvido para fins educacionais e de pesquisa em Ciência de Dados e Inteligência Artificial.
