
# receptor.py - QR Receiver for Red Team File Transfer
import cv2
import base64
import json
import gzip
from pyzbar.pyzbar import decode
from io import BytesIO

cap = cv2.VideoCapture(0)
chunks = {}
received = set()
expected_total = None
filename = None

print("[*] Iniciando captura de fragmentos QR (modo consola)...")

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    decoded_objs = decode(frame)
    for obj in decoded_objs:
        try:
            payload = json.loads(obj.data.decode())
            if 'acknowledged' in payload and 'total' in payload:
                expected_total = payload['total']
                filename = payload.get('filename', 'archivo.gz')
                print(f"[✓] Calibración: {filename} ({expected_total} fragmentos)")
                continue
            if 'i' in payload and 'data' in payload:
                i = int(payload['i'])
                if i not in received:
                    received.add(i)
                    chunks[i] = payload['data']
                    print(f"[+] Fragmento {i + 1}/{expected_total} recibido")
        except Exception as e:
            pass

    if expected_total and len(received) == expected_total:
        break

print("[✓] Todos los fragmentos recibidos. Reconstruyendo...")
joined = ''.join([chunks[i] for i in range(expected_total)])
binary = base64.b64decode(joined)
try:
    final = gzip.decompress(binary)
    out_name = filename.replace('.gz', '')
except:
    final = binary
    out_name = filename

with open(out_name, 'wb') as f:
    f.write(final)

print(f"[✓] Archivo reconstruido: {out_name} ({len(final)} bytes)")
cap.release()
