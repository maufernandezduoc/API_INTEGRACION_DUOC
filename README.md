## Instalación
*pre requesito: Docker https://www.docker.com/*
1. Dirígete a la carpeta raíz del proyecto /entrega

2. Ejetuta el comando: ```docker compose up```

3. (Opcional en caso de tener puertos utilizados) Configuración de puerto HTTP/TCP:

4. Edita el archivo docker-compose.yml
5. En API tbk la línea número 19 se encuentra el puerto por defecto es el *8888*, si lo requieres puedes cambiar por alguno disponible en tu equipo.
6. En API tienda la línea número 10 se encuentra el puerto por defecto es el *5000*, si lo requieres puedes cambiar por alguno disponible en tu equipo.

7. Si ya habias ejecutado este comando ```docker compose up``` , ejecutar este comando ```docker compose build```

## API tbk 
- URL Local http://localhost:8888/docs


## Metodo */execute_sale_fake*
Usado para hacer pruebas, todas las peticiones darán una transacción exitosa, ejemplo:
```
{
  "status": true,
  "id_transaction": 1684726454
}
```
Los datos o montos ingresados no son validados y no afectan a la tabla de tarjetas.



## Metodo */execute_sale*
Usado para produccion, las transacciones exitosas daran:
```
{
  "status": true,
  "id_transaction": 1684726454
}
```
Los datos o montos ingresados son validados y afectan a la tabla de tarjetas.


****

## Metodo */view_all_card*

Usado para entregar la lista de tarjetas con sus saldos 


# Errores controlados

El formato del *fecha_v* (ej: 05/23) incorrecto. 
```
{
    'status': False, 
    'msg': 'fecha_v con formato incorrecto'
}
```

El valor de *nro_tarjeta* no fue encorntrado en la tabla de tarjetas
```
{
    'status': False, 
    'msg': 'Tarjeta no encontrada'
}
```
Algun valor de tarjeta ingresada no coincide con la que esta almacenada en la base de datos (*nro_tarjeta*, *fecha_v*, *cvv*) 
```
{
    'status': False, 
    'msg': 'Los valores de la tarjeta no coinciden'
}
```

El monto a cobrar es mayor al que tiene de saldo la tarjeta ingresada
```
{
    'status': False, 
    'msg': 'Saldo insuficiente'
}
```

Error al prosesar el cobro, la operacion fue interrumpida por algun procedo interno del api
```
{
    'status': False, 
    'msg': 'Error en el cobro'
}
```



## API tienda
- URL Local http://localhost:5000

## Metodo *Addcliente*  POST http://127.0.0.1:5000/clientes
Usado para agregar clientes, todas las peticiones seran exitosa, ejemplo:
```
{
    "rut: 11111111-1,
     n_tarjeta: 1270795238838918

}
```
Los datos ingresados no son validados y no afectan a la tabla de Productos.

## Método *Obtener_clientes*

Usado para entregar la lista completa de clientes

El valor de *id_cliente* no fue encontrado en la tabla de cliente

```
{
    'status': False, 
    'msg': producto no encontrado'
}
```



## Método *Eliminar_cliente*

Usado para eliminar todos los datos de un cliente de la tabla carritos

El valor de *id_cliente* fue eliminado en la tabla de cliente

```
{
    'status': False, 
    'msg': cliente eliminado '
}
```


# Errores controlados


El valor de *rut* no fue encontrado en la tabla de clientes
```
{
    'status': False, 
    'msg': cliente no encontrado'
}
```


Algún valor del cliente ingresado no coincide con la que esta almacenada en la base de datos (*rut*, *tarjeta*) 
```
{
    'status': False, 
    'msg': 'Los valores del cliente no coinciden'
}
```

## Metodo *Addproductos* POST  http://127.0.0.1:5000/productos
Usado para agregar productos, todas las peticiones seran exitosa, ejemplo:
```
{
    "id_producto": 6, 
	"nombre": "Cuerdas", 
	"valor_venta": 15000,
	"stock": 10

}
```
Los datos ingresados no son validados y no afectan a la tabla de Productos.

## Método *Obtener_productos*

Usado para entregar la lista completa de productos 

## Método *eliminarproducto*

Usado para eliminar un productos 


# Errores controlados


El valor de *id_producto* no fue encontrado en la tabla de productos
```
{
    'status': False, 
    'msg': producto no encontrado'
}
```
El formato del *stock* (ej: 0) incorrecto. 
```
{
    'status': False, 
    'msg': 'no existe stock del producto'
}
```

Algún valor del producto ingresado no coincide con la que esta almacenada en la base de datos (*id_producto *, *nombre*) 
```
{
    'status': False, 
    'msg': 'Los valores del producto no coinciden'
}

```

## Metodo *Addcarritos* POST http://127.0.0.1:5000/carritos
Usado para agregar carritos, todas las peticiones seran exitosa, ejemplo:
```
{
    "id_carrito": 1, 
	"rut": "11111111-1", 
	"total": 0
}
```
Los datos ingresados no son validados y no afectan a la tabla de Productos.

E

## Método *Obtener carritos*

Usado para entregar la lista completa de carritos

## Método *Obtener_carrito*

Usado para entregar los datos de un carrito

# Errores controlados


El valor de *id_carrito* no fue encontrado en la tabla de carritos
```
{
    'status': False, 
    'msg': carrito no encontrado'
}
```
El formato del *total* (ej: < 0) incorrecto. 
```
{
    'status': False, 
    'msg': el total no puede ser menor que 0'
}
```
Algún valor del carrito ingresado no coincide con la que esta almacenada en la base de datos (*id_carrito*, *rut*) 
```
{
    'status': False, 
    'msg': 'Los valores del carrito no coinciden'
}
```

## Método *Eliminar_carrito*

Usado para eliminar todos los datos de un carrito de la tabla carritos


# Errores controlados


El valor de *id_carrito* no fue encontrado en la tabla de carritos
```
{
    'status': False, 
    'msg': carrito no fue eliminado'
}
```
Algún valor del carrito ingresado no coincide con la que esta almacenada en la base de datos (*id_carrito*, *rut*) 
```
{
    'status': False, 
    'msg': 'Los valores del carrito no coinciden'
}
```
## Método *productocarrito* http://127.0.0.1:5000/ POST

Usado para ver los productos que posee un carrito


# Errores controlados


El valor de *id_carrito* no fue encontrado en la tabla de carritos
```
{
    'status': False, 
    'msg': carrito no fue encontrado
}
```

## Método *Agregarproductocarrito*

Usado para agregar los productos a un carrito


# Errores controlados


El valor de *id_producto* no fue encontrado en la tabla de productos
```
{
    'status': False, 
    'msg': producto no fue encontrado
}
```

## Metodo *Addcompras* POST http://127.0.0.1:5000/compra
Usado para agregar compras, todas las peticiones seran exitosa, ejemplo:
```
{
    "n_tarjeta": 1270795238838918,
    "fecha_v": "12/26",
    "cvv": 942,
    "id_carrito": 1

}
```
Los datos ingresados no son validados y no afectan a la tabla de Productos.

## Método *Obtener_compras*

Usado para entregar la lista completa de compras



## Método *Obtener_compra*

Usado para entregar los datos de una compra

El valor de *idcompra* no fue encontrado en la tabla de compras
```
{
    'status': true, 
    'msg': compra no encontrada'
}
```

# Errores controlados


El valor de *id* no fue encontrado en la tabla de compras
```
{
    'status': False, 
    'msg': compra no encontrada'
}
```
El formato del *total* (ej: < 0) incorrecto. 
```
{
    'status': False, 
    'msg': el total no puede ser menor que 0'
}
```
Algún valor del carrito ingresado no coincide con la que esta almacenada en la base de datos (*id*,   *transacción*) 
```
{
    'status': False, 
    'msg': 'Los valores del compras no coinciden'
}
```
