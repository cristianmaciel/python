import mysql.connector
from os import *

# Conectando ao MySQL (sem especificar o banco de dados)
meubd = mysql.connector.connect(
    host='localhost',
    user='user',
    password='123456'
)
system('clear')
# Criando um novo banco de dados
cursor = meubd.cursor()
cursor.execute("CREATE DATABASE BACKUP")
