# Cliente TCP - Cálculo de IMC

Este script implementa el **cliente TCP** del proyecto IMC Remote.  
Permite al usuario ingresar sus datos personales y enviarlos a un servidor remoto para calcular su **Índice de Masa Corporal (IMC)**.

## Funcionamiento

1. Solicita al usuario los siguientes datos:
   - Sexo
   - Edad
   - Altura (en metros)
   - Peso (en kilogramos)
2. Envía los datos en formato JSON al servidor.
3. Espera la respuesta con el resultado del IMC, la categoría y una breve explicación.
4. Muestra la información en pantalla.

## Ejecución

1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar:  
   `python3 client/client.py <ip_del_servidor>`  
   Ejemplo:  
   `python3 client/client.py 192.168.1.19`
3. Ingresar los datos cuando el programa los solicite.

## Notas

- El cliente y el servidor deben estar en la **misma red local**.
- Puede usarse **modo adaptador puente** en VirtualBox para facilitar la comunicación.
- Si el servidor está en Linux, se recomienda verificar la IP con `ip a`.

**Archivo:** `client/client.py`
