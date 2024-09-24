import psycopg2
import json

conn = psycopg2.connect(
    host="localhost",  
    port="7889",  
    database="mvc-han",  
    user="postgres",  
    password="burhan7730"  
)


cur = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS ip_data (
    id SERIAL PRIMARY KEY,
    ip_prefix VARCHAR(50),
    region VARCHAR(50),
    service VARCHAR(50),
    network_border_group VARCHAR(50)
);
"""
cur.execute(create_table_query)

conn.commit()


with open('index.json', 'r', encoding='utf-8') as file:
    data_list = json.load(file)

insert_query = """
INSERT INTO ip_data (ip_prefix, region, service, network_border_group)
VALUES (%s, %s, %s, %s)
"""

for data in data_list:
    cur.execute(insert_query, (
        data['ip_prefix'],
        data['region'],
        data['service'],
        data['network_border_group']
    ))

conn.commit()

cur.close()
conn.close()

print("ข้อมูลจากไฟล์ index.json ถูกบันทึกลงในฐานข้อมูลเรียบร้อยแล้ว")
