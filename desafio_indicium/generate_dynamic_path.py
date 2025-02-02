import os
import sys
from datetime import datetime

def create_dynamic_path(base_path, table_name, execution_date=None):
    """
    Cria um caminho dinâmico com base na data e no nome da tabela.
    Se a data não for fornecida, usa a data atual.
    Cria os diretórios necessários caso não existam.
    """
    dynamic_path = os.path.join(base_path, table_name, execution_date)    
    os.makedirs(dynamic_path, exist_ok=True)
    
    return dynamic_path

def main():
    """
    python generate_dynamic_path.py <csv/postgres> <table_name> <date(optional)>
    date: YYYY-MM-DD
    """
    execution_date = os.getenv("EXECUTION_DATE")
    table_name = sys.argv[2] 
    if sys.argv[1] == "csv":
        base_path = "../code-challenge/data/csv"
    else:
        base_path = "../code-challenge/data/postgres"
    dynamic_path = create_dynamic_path(base_path, table_name, execution_date)
    print(f"export DYNAMIC_PATH='{dynamic_path}'")

if __name__ == "__main__":
    main()