# imortando pacotes
import requests
import json
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

# Conexao API
class ConexaoApi:
    def __init__(self,url):
        self.url = url

        global retorno
        parametro = json.dumps({
            "size": 10000
        })
        headers = {
            'Content-Type': 'application/json'
        }
        retorno = requests.request(
            "GET",
            url = self.url,
            data = parametro,
            headers = headers
        )
    # Verifica status
    def StatusApi(self):
        status = retorno
        return (status.status_code)

    # Carrega json
    def Load_Json(self):
        data = json.loads(retorno.text)
        return data

# Conexao banco de dados relacional SQL
class ConexaoDbSql:
    def __init__(self,host,port,database,user,password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

        global conn
        conn = create_engine("mysql+pymysql://"+os.getenv("db_user")+":"+os.getenv("db_pass")+"@"+os.getenv("db_url")+":"+os.getenv("db_port")+"/"+os.getenv("db_database"))

#####################
# Dados conexao API #
#####################
authapi = ConexaoApi(
    os.getenv("api_url")
)

##########################
# Dados conexao DB_Mysql #
##########################
dbsql = ConexaoDbSql(
    os.getenv("db_user"),
    os.getenv("db_pass"),
    os.getenv("db_url"),
    os.getenv("db_port"),
    os.getenv("db_database")
)
