#!/usr/bin/python3
from elasticsearch import Elasticsearch
import requests
import json
import mysql.connector


# Inicializo cliente ELK
elk_client = Elasticsearch(hosts=["localhost:9200"])

# print (client)
if elk_client.indices.exists(index="autos") is True:
    # print ("El indice ya existe");
    elk_client.indices.delete(index="autos")
    elk_client.indices.create(index="autos")
    result = 1
else:
    elk_client.indices.create(index="autos")
    # print ("Indice creado");

mydb = mysql.connector.connect(
  host="localhost",
  user="idatos",
  password="idatos",
  database="IDATOS"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM vehiculo")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  car_brand = x[3]
  car_model = x[4]
  car_doors = x[11]
  car_year = x[7]
  car_kilometers = x[10]
  car_fuel_type = x[8]
  car_price = x[1]
  car_price_currency = x[2]
  car_condition = x[0]
  publication_link = x[13]
  publication_title = x[14]
  publication_thumbnail = x[12]
  publication_document = {
      "brand": car_brand,
      "model": car_model,
      "doors": car_doors,
      "year" : car_year,
      "kilometers": car_kilometers,
      "fuel_type": car_fuel_type,
      "price": car_price,
      "currency": car_price_currency,
      "condition": car_condition,
      "publication_link": publication_link,
      "publication_title": publication_title,
      "thumbnail": publication_thumbnail,
  }
  json_document = json.dumps(publication_document)
  log_json_document = json.dumps(publication_document, indent=4)
  elk_client.index(index="autos", body=json_document)
