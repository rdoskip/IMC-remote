#!/usr/bin/env python3
"""
Servidor TCP para calcular IMC (BMI).
Escucha conexiones permanentes y atiende cada cliente en un hilo.
Recibe JSON con: sexo, edad, altura (m), peso (kg).
Responde JSON con: imc, categoria, texto_explicativo.
"""
import socket
import threading
import json
import struct

HOST = "0.0.0.0"   # escuchar en todas las interfaces
PORT = 5000

# --- utilidades para enviar/recibir mensajes con prefijo de longitud ---
def send_message(conn, obj):
    data = json.dumps(obj).encode('utf-8')
    header = struct.pack('!I', len(data))  # 4 bytes big-endian
    conn.sendall(header + data)

def recv_message(conn):
    header = recvall(conn, 4)
    if not header:
        return None
    length = struct.unpack('!I', header)[0]
    data = recvall(conn, length)
    if not data:
        return None
    return json.loads(data.decode('utf-8'))

def recvall(conn, n):
    buf = b''
    while len(buf) < n:
        chunk = conn.recv(n - len(buf))
        if not chunk:
            return None
        buf += chunk
    return buf

# --- cálculo IMC y clasificación ---
def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError("Altura debe ser > 0")
    imc = peso / (altura * altura)
    return round(imc, 2)

def categoria_imc(imc):
    # Clasificación general (WHO / Tua Saúde similar)
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25.0:
        return "Normal"
    elif imc < 30.0:
        return "Sobrepeso"
    elif imc < 35.0:
        return "Obesidad I"
    elif imc < 40.0:
        return "Obesidad II"
    else:
        return "Obesidad III"

def info_imc_texto():
    return (
        "IMC (Índice de Masa Corporal) = peso(kg) / (altura(m))^2.\n"
        "Clasificación aproximada:\n"
        " - Bajo peso: < 18.5\n"
        " - Normal: 18.5 - 24.9\n"
        " - Sobrepeso: 25 - 29.9\n"
        " - Obesidad I: 30 - 34.9\n"
        " - Obesidad II: 35 - 39.9\n"
        " - Obesidad III: >= 40\n"
    )

# --- manejo de cliente ---
def handle_client(conn, addr):
    try:
        req = recv_message(conn)
        if req is None:
            print(f"[{addr}] conexión cerrada sin datos.")
            return
        # Esperar campos: sexo, edad, altura, peso
        sexo = req.get("sexo")
        edad = req.get("edad")
        altura = float(req.get("altura"))
        peso = float(req.get("peso"))

        # Validaciones simples
        errors = []
        if sexo is None:
            errors.append("Falta 'sexo'")
        if edad is None or int(edad) <= 0:
            errors.append("Edad inválida")
        if altura <= 0:
            errors.append("Altura inválida")
        if peso <= 0:
            errors.append("Peso inválido")

        if errors:
            response = {"status": "error", "errors": errors}
            send_message(conn, response)
            return

        imc = calcular_imc(peso, altura)
        cat = categoria_imc(imc)
        respuesta_texto = f"IMC calculado: {imc}. Categoría: {cat}."

        response = {
            "status": "ok",
            "imc": imc,
            "categoria": cat,
            "explicacion": info_imc_texto(),
            "mensaje": respuesta_texto
        }
        send_message(conn, response)
        print(f"[{addr}] resuelto IMC={imc}, categoria={cat}")
    except Exception as e:
        send_message(conn, {"status": "error", "errors": [str(e)]})
        print(f"[{addr}] error: {e}")
    finally:
        conn.close()

def main():
    print(f"Servidor IMC escuchando en puerto {PORT}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        while True:
            conn, addr = s.accept()
            print(f"Conexión entrante desde {addr}")
            t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            t.start()

if __name__ == "__main__":
    main()
