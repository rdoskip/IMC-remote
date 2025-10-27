#!/usr/bin/env python3
"""
Cliente TCP para solicitar cálculo de IMC remoto.
Pide datos al usuario y muestra la respuesta del servidor.
Uso: python3 client.py <IP_SERVIDOR> [PUERTO]
"""
import socket
import json
import struct
import sys

def send_message(conn, obj):
    data = json.dumps(obj).encode('utf-8')
    header = struct.pack('!I', len(data))
    conn.sendall(header + data)

def recvall(conn, n):
    buf = b''
    while len(buf) < n:
        chunk = conn.recv(n - len(buf))
        if not chunk:
            return None
        buf += chunk
    return buf

def recv_message(conn):
    header = recvall(conn, 4)
    if not header:
        return None
    length = struct.unpack('!I', header)[0]
    data = recvall(conn, length)
    if not data:
        return None
    return json.loads(data.decode('utf-8'))

def pedir_datos():
    print("Ingrese los datos para calcular el IMC (use altura en metros y peso en kg).")
    sexo = input("Sexo (M/F/O): ").strip()
    edad = int(input("Edad (años): ").strip())
    altura = float(input("Altura (m), ej 1.75: ").strip())
    peso = float(input("Peso (kg): ").strip())
    return {"sexo": sexo, "edad": edad, "altura": altura, "peso": peso}

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 client.py <IP_SERVIDOR> [PUERTO]")
        sys.exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) >= 3 else 5000

    datos = pedir_datos()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Conectando a {host}:{port} ...")
        s.connect((host, port))
        send_message(s, datos)
        resp = recv_message(s)
        if resp is None:
            print("No se recibió respuesta del servidor.")
            return
        if resp.get("status") == "ok":
            print("Resultado del servidor:")
            print(f"  IMC: {resp.get('imc')}")
            print(f"  Categoría: {resp.get('categoria')}")
            print(f"  Mensaje: {resp.get('mensaje')}")
            print("\nExplicación:\n" + resp.get("explicacion"))
        else:
            print("Error desde servidor:", resp.get("errors"))

if __name__ == "__main__":
    main()