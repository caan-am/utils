import pandas as pd
import os

def calculate_monthly_returns(file_path):
    # Leer CSV
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values('Date', inplace=True)
    
    # Calcular rentabilidad mensual
    df['Return'] = df['Value'].pct_change() * 100
    
    # Seleccionar columnas necesarias
    df = df[['Date', 'Return']].dropna()
    return df

def main():
    input_folder = 'input'
    output_folder = 'output'
    output_file = os.path.join(output_folder, 'monthly_returns.xlsx')
    
    # Asegurarse de que la carpeta de salida existe
    os.makedirs(output_folder, exist_ok=True)
    
    # Obtener lista de archivos CSV
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
    
    # Crear un archivo Excel con múltiples hojas
    with pd.ExcelWriter(output_file) as writer:
        for file in csv_files:
            file_path = os.path.join(input_folder, file)
            returns = calculate_monthly_returns(file_path)
            sheet_name = os.path.splitext(file)[0][:31]  # Excel limita los nombres de hoja a 31 caracteres
            returns.to_excel(writer, sheet_name=sheet_name, index=False)
    
    print(f'Resultados guardados en: {output_file}')

if __name__ == '__main__':
    main()