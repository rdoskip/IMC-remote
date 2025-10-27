# Proyecto IMC Remote (TCP en Python)

Este proyecto fue desarrollado como práctica para aplicar el uso del **protocolo TCP** mediante **sockets** en Python. El objetivo es crear una aplicación cliente-servidor que calcule el **Índice de Masa Corporal (IMC)** de forma remota. El cliente envía los datos (sexo, edad, altura y peso) al servidor, y este devuelve el resultado del IMC junto con su clasificación.

## Requerimientos

- Dos máquinas con **Ubuntu** (pueden ser máquinas virtuales en VirtualBox).
- **Python 3.10 o superior**.
- Conexión en la **misma red local** (usar modo adaptador puente en VirtualBox).
- **Wireshark** (opcional, para analizar los paquetes TCP).

## Pasos de instalación y ejecución

1. Actualizar los paquetes:  
   `sudo apt update && sudo apt upgrade -y`
2. Verificar versión de Python:  
   `python3 --version`
3. (Opcional) Instalar Wireshark:  
   `sudo apt install wireshark`  
   Permitir captura para usuarios no root si se solicita.
4. Verificar conexión entre las máquinas:
   - En el servidor: `ip a` (anotar la IP, por ejemplo, `192.168.1.19`).
   - En el cliente: `ping 192.168.1.19`
5. Clonar el proyecto:  
   `git clone https://github.com/rdoskip/IMC-remote.git`  
   `cd IMC-remote`
6. En el **servidor**, ejecutar:  
   `python3 server/server.py`
7. En el **cliente**, ejecutar:  
   `python3 client/client.py <ip_del_servidor>`  
   Ejemplo: `python3 client/client.py 192.168.1.19`
8. Ingresar los datos solicitados: sexo, edad, altura (m) y peso (kg).
9. El sistema mostrará el IMC calculado, la categoría y una breve explicación.

## Fórmula del IMC

IMC = peso (kg) / (altura (m))²

## Comunicación entre cliente y servidor

- **Cliente → Servidor:** envía `{sexo, edad, altura, peso}` en formato JSON.
- **Servidor → Cliente:** responde `{imc, categoria, explicacion}` también en formato JSON.

**Autor:** Ronald Santiago Niño Tineo y Juan David Mirando Pelaez
**Materia:** Redes
**Año:** 2025
