"""
data_science_environment_project.py
Código para limpeza, análise e visualização de dados ambientais
Autor: Gerado por ChatGPT (assistente)
Instruções: Coloque os arquivos CSV na mesma pasta e rode: python data_science_environment_project.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# -------------------- Configurações --------------------
DATA_FILES = {
    "energy": "consumo_energetico.csv",
    "air": "qualidade_ar.csv",
    "waste": "residuos.csv",
    "resources": "uso_recursos.csv"
}

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------- Funções utilitárias --------------------
def load_csv_safe(path):
    try:
        df = pd.read_csv(path)
        print(f"[OK] Carregado: {path} -> {df.shape[0]} linhas, {df.shape[1]} colunas")
        return df
    except FileNotFoundError:
        print(f"[AVISO] Arquivo não encontrado: {path}. Criando DataFrame vazio.")
        return pd.DataFrame()

def summarize_df(df, name):
    print(f"--- Resumo: {name} ---")
    print(df.info())
    print(df.describe(include='all').transpose().head(20))

def basic_cleaning(df):
    # Exemplo de limpeza: renomear colunas, converter datas, tratar missing
    df = df.copy()
    # normalizar nomes de colunas
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    # detectar colunas de data
    for c in df.columns:
        if 'date' in c or 'data' in c or 'dia' in c:
            try:
                df[c] = pd.to_datetime(df[c], dayfirst=True, errors='coerce')
            except Exception:
                pass
    # substituir strings vazias por NaN
    df = df.replace(r'^\s*$', np.nan, regex=True)
    return df

def detect_anomalies_iqr(series):
    # Detectar outliers via IQR
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return series[(series < lower) | (series > upper)]

# -------------------- Pipeline --------------------
def main():
    # Carregar datasets
    dfs = {k: load_csv_safe(v) for k,v in DATA_FILES.items()}
    
    # Limpeza básica
    for k in list(dfs.keys()):
        dfs[k] = basic_cleaning(dfs[k])
        summarize_df(dfs[k], k)
    
    # Exemplo de análises (ajuste conforme os nomes reais das colunas)
    # 1) Consumo energético: média por mês / pico horário
    if not dfs['energy'].empty:
        df = dfs['energy']
        # tentar inferir coluna de consumo e data
        possible_consumption_cols = [c for c in df.columns if 'consum' in c or 'energy' in c or 'kwh' in c]
        date_cols = [c for c in df.columns if 'date' in c or 'data' in c or 'dia' in c or 'timestamp' in c]
        if date_cols and possible_consumption_cols:
            dcol = date_cols[0]; ecol = possible_consumption_cols[0]
            df[dcol] = pd.to_datetime(df[dcol], errors='coerce', dayfirst=True)
            df['month'] = df[dcol].dt.to_period('M')
            monthly = df.groupby('month')[ecol].mean().dropna()
            monthly.plot(kind='bar', figsize=(10,5), title='Consumo médio por mês')
            plt.tight_layout()
            plt.savefig(os.path.join(OUTPUT_DIR, 'consumo_medio_mes.png'))
            plt.close()
    
    # 2) Qualidade do ar: verificar PM2.5, PM10, NO2
    if not dfs['air'].empty:
        df = dfs['air']
        pollutant_cols = [c for c in df.columns if any(p in c for p in ['pm25','pm2.5','pm10','no2','o3','co'])]
        if pollutant_cols:
            df[pollutant_cols].plot(subplots=True, layout=(len(pollutant_cols),1), figsize=(8, 2*len(pollutant_cols)), legend=False)
            plt.suptitle('Séries temporais de poluentes')
            plt.tight_layout(rect=[0,0,1,0.97])
            plt.savefig(os.path.join(OUTPUT_DIR, 'poluentes_timeseries.png'))
            plt.close()
            # detectar anomalias via IQR para cada poluente
            anomalies = {}
            for col in pollutant_cols:
                if pd.api.types.is_numeric_dtype(df[col]):
                    anom = detect_anomalies_iqr(df[col].dropna())
                    anomalies[col] = anom
                    print(f"[ANOMALIAS] {col}: {len(anom)} valores atípicos detectados")
    
    # 3) Resíduos: geração por bairro / categoria
    if not dfs['waste'].empty:
        df = dfs['waste']
        for col in ['bairro','categoria','tipo']:
            if col in df.columns:
                top = df.groupby(col)['quantidade'].sum().sort_values(ascending=False).head(10)
                top.plot(kind='bar', figsize=(10,5), title=f'Geração de resíduos por {col} (top 10)')
                plt.tight_layout()
                plt.savefig(os.path.join(OUTPUT_DIR, f'residuo_top10_{col}.png'))
                plt.close()
                break
    
    # 4) Uso de recursos: água, energia, áreas verdes
    if not dfs['resources'].empty:
        df = dfs['resources']
        # exemplo: radar de uso relativo (normalizar colunas numéricas)
        num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if num_cols:
            summary = df[num_cols].describe().loc[['mean']].transpose()
            summary.columns = ['mean']
            summary = (summary - summary.min()) / (summary.max() - summary.min())
            ax = summary['mean'].plot(kind='bar', figsize=(10,5), title='Uso relativo médio de recursos')
            plt.tight_layout()
            plt.savefig(os.path.join(OUTPUT_DIR, 'uso_recursos_relativo.png'))
            plt.close()
    
    print("Pipeline concluído. Verifique a pasta 'outputs' para imagens e resultados.")

if __name__ == '__main__':
    main()
