import pandas as pd


def padronizarMF(sexo):
    if sexo[0].lower() == "m":

        return "M"
    return "F"


file_path = "Base_despadronizada.csv"

df = pd.read_csv(file_path, dtype=str)

numerical_columns = ["nota_matematica", "nota_portugues", "frequencia"]

for col in numerical_columns:
    df[col] = df[col].str.replace(",", ".").astype(float)


df["sexo"] = [padronizarMF(x) for x in df["sexo"]]

df["Media"] = (df["nota_matematica"] + df["nota_portugues"] + df["frequencia"] / 10) / 3

df["aprovado"] = df["Media"].apply(lambda x: "Sim" if x >= 7 else "Nao")

df.to_csv("padronizado.csv", decimal=',', float_format='%.2f' , index=False)

print(df)
