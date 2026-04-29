import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from typing import Dict, Optional


class MedicalDataProcessor:
    """ classe responsável por carregar, processar, analisar e exportar
    dados médicos provenientes de arquivos JSON."""

    def __init__(self, file_path: str, enable_plots: bool = False):
        self.file_path = file_path
        self.enable_plots = enable_plots
        self.raw_data = None
        self.df = None

    @staticmethod
    def parse_date(date_obj: Optional[Dict]) -> Optional[datetime]:
        """converte datas no formato mongodb para datetime"""
        try:
            if date_obj and "$date" in date_obj:
                return pd.to_datetime(date_obj["$date"])
        except Exception:
            return None
        return None

    @staticmethod
    def anonymize(value: str) -> str:
        """anonimiza dados sensíveis (ex: cpf)"""
        if not value:
            return None
        return f"***{value[-3:]}"

    def load_json(self):
        """carrega e valida o json"""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.raw_data = json.load(f)

            if not isinstance(self.raw_data, list):
                raise ValueError("json deve ser uma lista de pacientes.")

        except Exception as e:
            raise RuntimeError(f"erro ao carregar json: {e}")

    def normalize_data(self):
        """transforma json em dataframe estruturado"""
        """lamba minha caceta de brinde foda-se o código é meu caralho"""
        records = []

        for patient in self.raw_data:
            try:
                base_info = {
                    "cpf": self.anonymize(patient.get("cpf")),
                    "sexo": patient.get("sexo"),
                    "cidade": patient.get("cidade"),
                    "estado": patient.get("estado"),
                    "data_nascimento": self.parse_date(patient.get("dataNascimento"))
                }

                for reg in patient.get("registros", []):
                    info = reg.get("informacoes", {})

                    record = {
                        **base_info,
                        "tipo": reg.get("tipo"),
                        "servico": reg.get("servico"),
                        "data_entrada": self.parse_date(reg.get("dataEntrada")),
                        "data_saida": self.parse_date(reg.get("dataSaida")),
                        "data_cadastro": self.parse_date(reg.get("dataCadastro")),
                        "especialidade": info.get("especialidade") or info.get("especializacao"),
                        "diagnostico": info.get("diagnostico"),
                        "medicamento": (
                            info.get("medicamento", {}).get("nome")
                            if isinstance(info.get("medicamento"), dict)
                            else None
                        ),
                        "cid": (
                            info.get("cid")[0]["descricao"]
                            if info.get("cid") else None
                        )
                    }

                    records.append(record)
        
            except Exception as e: 
                print(f"erro ao processar paciente: {e}")

        self.df = pd.DataFrame(records)

    def clean_data(self):
        """limpeza e padronização"""
        if self.df is None:
            raise ValueError("dados não carregados.")

        self.df.drop_duplicates(inplace=True)

        for col in ["sexo", "cidade", "estado", "tipo"]:
            if col in self.df.columns:
                self.df[col] = self.df[col].astype(str).str.upper().str.strip()

        for col in ["data_entrada", "data_saida", "data_cadastro", "data_nascimento"]:
            self.df[col] = pd.to_datetime(self.df[col], errors="coerce").dt.tz_localize(None)

        self.df["idade"] = (
            (pd.Timestamp.now(tz=None) - self.df["data_nascimento"]).dt.days // 365
        )

        self.df.fillna({
            "diagnostico": "NÃO INFORMADO",
            "medicamento": "NÃO INFORMADO",
            "cid": "NÃO INFORMADO"
        }, inplace=True)

    def generate_statistics(self):
        """gera estatísticas básicas"""
        """que banco de dados grande do caralho vai se fuder é 17:54 e eu só consegui executar
        a porra do código DUAS vezes pra testar pq demora MIL ANOS pra carregar essa merda"""
        print("\n=== estatísticas ===")

        print("\nidade média:")
        print(self.df["idade"].mean())

        print("\ndistribuição por sexo:")
        print(self.df["sexo"].value_counts())

        print("\ntipos de registro:")
        print(self.df["tipo"].value_counts())

        print("\ndiagnósticos mais comuns:")
        print(self.df["cid"].value_counts().head(10))

    def plot_data(self):
        """cria gráficos simples"""
        if not self.enable_plots:
            return

        sns.set()

        plt.figure()
        self.df["sexo"].value_counts().plot(kind="bar")
        plt.title("distribuição por sexo")
        plt.show()

        plt.figure()
        self.df["cid"].value_counts().head(5).plot(kind="bar")
        plt.title("top diagnósticos")
        plt.show()

    def export_data(self, output_path: str):
        """exporta dados tratados"""
        try:
            self.df.to_csv(f"{output_path}.csv", index=False)
            self.df.to_excel(f"{output_path}.xlsx", index=False)
            print("exportação concluída.")
        except Exception as e:
            print(f"erro ao exportar: {e}")

    def filter_by_diagnosis(self, diagnosis: str):
        """filtra por diagnóstico"""
        return self.df[self.df["cid"].str.contains(diagnosis, case=False, na=False)]


if __name__ == "__main__":
    processor = MedicalDataProcessor(
        r"C:\Users\joaof\OneDrive\Desktop\el pitchula\santa_casa.registros_medicos.json",
        enable_plots=False  # muda pra True se quiser ver gráficos
    )

    processor.load_json()
    processor.normalize_data()
    processor.clean_data()

    processor.generate_statistics()
    processor.plot_data()

    processor.export_data("saida_tratada")

    resultado = processor.filter_by_diagnosis("HIPOTENSAO")
    print("\npacientes com hipotensão:")
    print(resultado.head())