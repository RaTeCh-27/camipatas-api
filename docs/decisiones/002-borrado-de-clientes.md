# 002 – Borrado de clientes: soft delete

## Contexto
El problema que aparece es que cuando un cliente deja el servicio lo primero que se piensa es borrarlo de la base de datos pero esto conlleva a que no solo se borre a el sino al perro y se pierde la informacion pasada del mismo no permitiendonos que vuelva a el servicio en caso de que quiera volver.

## Decisión
Elegi que no se borra nada: el cliente queda con activo = False. A los perros también les puse activo ya que por periodos no tienen el servicio activo permite este cambio sin la necesidad de borrar los cambios

## Alternativas que consideré
Se considero usar el metodo Cascade pero en caso de borrar todo y querer hacer un recuento general de los ingresos se perdera el historial perdiendo el total de ganancias

## Consecuencias
Conservás todo el historial y podés reactivar a un cliente si vuelve pero al listar clientes y perros hay que filtrar los que tienen activo = True, para no mostrar los dados de baja.