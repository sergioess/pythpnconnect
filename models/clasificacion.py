import psycopg2
import conn


class Clasificacion:

    nombre = ''
    id_tienda = 1
    activo = 1

    clasificaciones = []  # Atributo de la clase categorias
    id = 0
    cantidadClasificaciones = 0
    connection = conn.create_connection()

    def __init__(self, cantidadClasificaciones):
        self.cantidadClasificaciones = cantidadClasificaciones

    def __init__(self):
        pass

    def __init__(self, nombre):
        self.nombre = nombre
        pass

    @staticmethod
    def listClasificacion(self):

        # conn = psycopg2.connect(
        #     host='ec2-3-231-69-204.compute-1.amazonaws.com', port=5432, database='d3hr8qndm4p50h', user='oxwttxarfidlxi', password='89e47cacfc5926776ab52a7e485b08a91bf9632736ca0843d80b6356b506f3f2')
        cur = self.connection.cursor()
        self.cur.execute('SELECT * FROM clasificaciones')

        self.cur.execute('SELECT * FROM clasificaciones')
        clasificaciones = self.cur.fetchall()
        cantidadClasificaciones = len(clasificaciones)

        self.cur.close()

        return clasificaciones

    def create_clasificacion(self):
        # print(self.nombre)
        try:
            cur = self.connection.cursor()
            cur.execute(
                "INSERT INTO clasificaciones (nombre, id_tienda, activo) VALUES ('%s', 1, 1)" % (self.nombre))
            # cur.execute(
            #     "INSERT INTO clasificaciones (nombre, id_tienda, activo) VALUES (%s,1,1)", (self.nombre))
            self.connection.commit()
        finally:
            cur.close()
            self.connection.close()

    def delete(self):
        try:
            cur = self.connection.cursor()
            cur.execute(
                'DELETE FROM clasificaciones WHERE nombre=%s', (self.nombre,))
            self.connection.commit()
        finally:
            cur.close()
            self.connection.close()

    def get_nombre(self):
        try:
            cur = self.connection.cursor()
            cur.execute(
                "SELECT * FROM clasificaciones WHERE nombre='%s'" % (self.nombre))

            clasificacion = cur.fetchone()
            self.id = clasificacion[0]
            self.nombre = clasificacion[1]

        finally:
            cur.close()
            self.connection.close()
