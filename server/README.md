# Servidor TCP - Cálculo de IMC

Este script implementa el **servidor TCP** del proyecto IMC Remote.  
Su función es recibir los datos enviados por el cliente (sexo, edad, altura y peso), calcular el **Índice de Masa Corporal (IMC)**, determinar su categoría y enviar la respuesta nuevamente al cliente.

## Funcionamiento

1. El servidor crea un socket TCP y queda a la espera de conexiones.
2. Al recibir una solicitud, decodifica los datos enviados en formato JSON.
3. Calcula el IMC mediante la fórmula:  
   `IMC = peso / (altura ** 2)`
4. Clasifica el IMC (bajo peso, normal, sobrepeso u obesidad).
5. Envía la respuesta al cliente en formato JSON.
6. Cierra la conexión y queda listo para recibir otra.

## Ejecución

1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar:  
   `python3 server/server.py`
3. Ver la IP del servidor con:  
   `ip a`
4. Esperar la conexión del cliente.

## Notas

- Asegúrese de que el firewall o la configuración de red permita el puerto utilizado (por defecto 5000).
- Puede ejecutar `Wireshark` en el servidor para observar los paquetes TCP.

**Archivo:** `server/server.py`
