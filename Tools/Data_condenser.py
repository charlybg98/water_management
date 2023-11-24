import pandas as pd
import os

data_path = "./../Data"
file_names = os.listdir(data_path)

combined_df = pd.DataFrame()

for file in file_names:
    df = pd.read_excel(os.path.join(data_path, file))

    if "Clave" in df.columns:
        df.drop("Clave", axis=1, inplace=True)

    df_melted = df.melt(id_vars=["Nombre"], var_name="Year", value_name=file[:-5])
    df_melted.set_index(["Nombre", "Year"], inplace=True)

    if combined_df.empty:
        combined_df = df_melted
    else:
        combined_df = combined_df.join(df_melted, how="outer")

combined_df.reset_index(inplace=True)
combined_df["RHA_Year"] = combined_df["Nombre"] + "_" + combined_df["Year"].astype(str)
combined_df = combined_df.set_index("RHA_Year").drop(columns=["Nombre", "Year"])
combined_df.dropna(inplace=True)
combined_df.to_csv(os.path.join(data_path, "data.csv"))
