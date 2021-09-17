import psycopg2


def create_connection():
    conn = psycopg2.connect(
        host='ec2-3-231-69-204.compute-1.amazonaws.com', port=5432, database='d3hr8qndm4p50h', user='oxwttxarfidlxi', password='89e47cacfc5926776ab52a7e485b08a91bf9632736ca0843d80b6356b506f3f2')

    # cur = conn.cursor()

    return conn

# cur.execute('SELECT * FROM clasificaciones')

# print(cur.fetchall())

# cur.close()


# conn2 = psycopg2.connect(
#     host='ec2-54-156-60-12.compute-1.amazonaws.com', port=5432, database='d7h26gu4vod24h', user='viutzficoufmpa', password='c0d7d5f9df168feff12131f3352922560adbb1250a644651b2cc28442e06de2b')

# cur2 = conn2.cursor()
# cur2.execute('SELECT * FROM rol')

# print(cur2.fetchall())

# cur2.close()
