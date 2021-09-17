import psycopg2


class Clasificacion:

    clasificaciones = []  # Atributo de la clase categorias
    id = 0
    cantidadClasificaciones = 0

    def __init__(self, cantidadClasificaciones):
        self.cantidadClasificaciones = cantidadClasificaciones

    def listClasificacion(self):

        conn = psycopg2.connect(
            host='ec2-3-231-69-204.compute-1.amazonaws.com', port=5432, database='d3hr8qndm4p50h', user='oxwttxarfidlxi', password='89e47cacfc5926776ab52a7e485b08a91bf9632736ca0843d80b6356b506f3f2')

        cur = conn.cursor()
        cur.execute('SELECT * FROM clasificaciones')

        self.clasificaciones = cur.fetchall()
        self.cantidadClasificaciones = len(self.clasificaciones)

        cur.close()

        return self.clasificaciones
