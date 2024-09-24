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

query = """
SELECT ip_prefix, region, service, network_border_group
FROM ip_data
WHERE region = %s AND service = %s
"""

cur.execute(query, ('us-west-1', 'S3'))

result = cur.fetchall()

cur.close()
conn.close()

data_list = [
    {
        'ip_prefix': row[0],
        'region': row[1],
        'service': row[2],
        'network_border_group': row[3]
    }
    for row in result
]

with open('filtered_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, indent=4, ensure_ascii=False)

print("ข้อมูลถูกบันทึกในไฟล์ filtered_data.json เรียบร้อยแล้ว")
