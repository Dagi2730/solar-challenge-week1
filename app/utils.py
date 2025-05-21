import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def load_data():
    # Load cleaned datasets and combine
    df_benin = pd.read_csv('data/benin_clean.csv')
    df_sierra = pd.read_csv('data/sierra_leone_cleaned.csv')
    df_togo = pd.read_csv('data/togo_dapaong_cleaned.csv')

    df_benin['country'] = 'Benin'
    df_sierra['country'] = 'Sierra Leone'
    df_togo['country'] = 'Togo'

    df_all = pd.concat([df_benin, df_sierra, df_togo], ignore_index=True)
    return df_all

def get_summary(df, countries, metrics):
    # Filter data
    df_filtered = df[df['country'].isin(countries)]
    summary = df_filtered.groupby('country')[metrics].agg(['mean', 'median', 'std']).round(2)
    summary.columns = ['_'.join(col) for col in summary.columns]
    summary = summary.reset_index()
    return summary

def create_boxplot(df, countries, metric):
    # Filter data
    df_filtered = df[df['country'].isin(countries)]

    plt.figure(figsize=(8, 5))
    ax = sns.boxplot(x='country', y=metric, data=df_filtered, palette='Set2')
    ax.set_title(f'Boxplot of {metric} by Country')
    ax.set_xlabel('Country')
    ax.set_ylabel(metric)

    # Save plot to bytes
    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    img_bytes = buf.read()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
