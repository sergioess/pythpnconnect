from models.clasificacion import Clasificacion

# listClasificaciones = Clasificacion(1)

# print(Clasificacion.cantidadClasificaciones)

# print(Clasificacion.listClasificacion())
# print(Clasificacion.cantidadClasificaciones)


# CREAR REGISTRO
# clasiSalsas = Clasificacion("Salsas")
# clasiSalsas.create_clasificacion()

# CONSULTAR POR NOMBRE
# clasiSalsas = Clasificacion('Salsas')
# clasiSalsas.get_nombre()
# print(
#     f"La Clasificacion tiene id {clasiSalsas.id} y nombre {clasiSalsas.nombre}")


# ELIMINAR REGISTRO
clasiSalsas = Clasificacion('Salsas')
clasiSalsas.delete()
