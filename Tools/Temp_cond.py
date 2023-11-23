import pandas as pd
import os

def process_file(file_path, year):
    """ Procesa un archivo individual y retorna los promedios anuales por región con el año correspondiente. """
    data = pd.read_excel(file_path, skiprows=1)

    # Conservar solo la columna de región y la del promedio anual
    data = data[['ENTIDAD', 'ANUAL']]
    data.columns = ['Region', year]
    data = data.sort_values(by='Region')  # Ordenar por región

    return data.set_index('Region')

def main():
    base_directory = "Data/Other/Temperature"  # Directorio base actualizado
    all_years_data = []

    for file_name in os.listdir(base_directory):
        if file_name.endswith('.xlsx'):
            year = str(file_name)[:4]  # Asumiendo que el nombre del archivo es el año
            file_path = os.path.join(base_directory, file_name)
            year_data = process_file(file_path, year)
            all_years_data.append(year_data)

    # Combinar todos los datos en un solo DataFrame
    final_data = pd.concat(all_years_data, axis=1)

    # Guardar los datos combinados
    final_data.to_excel("Data/Other/Temperature/temp_cond.xlsx")

if __name__ == "__main__":
    main()


