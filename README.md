# Pagos Simulados

Proyecto académico desarrollado por **Carlos Humberto Esquivel Sanchez** para simular pagos en línea.

## 📘 Descripción
Este sistema permite registrar usuarios, simular transferencias de dinero entre ellos y validar que el remitente tenga saldo suficiente. Incluye un diagrama UML de clases y pruebas unitarias.

## 📂 Estructura
pagos-simulados/
│
├── README.md
├── docs/              # Documentación y UML
│   └── diagrama-clases.png
├── src/               # Código fuente
│   ├── main.py
│   └── pagos.py
├── tests/             # Pruebas unitarias
│   └── test_pagos.py
└── requirements.txt

## 📊 UML
El diagrama de clases se encuentra en `docs/diagrama-clases.png`.

## 🚀 Instalación
```bash
git clone https://github.com/Carlos2731/Pagos-Simulados-.git
cd Pagos-Simulados-
pip install -r requirements.txt

## ▶️ Uso del programa

Ejecuta el archivo principal para simular una transferencia:

```bash
python src/main.py

=== Estado inicial ===
Carlos - Saldo: $1000.00
Brayan - Saldo: $500.00
✅ Transferencia exitosa: Carlos → Brayan ($200.00)

=== Estado final ===
Carlos - Saldo: $800.00
Brayan - Saldo: $700.00


##Pruebas Unitarias
pytest tests/

Autor
Carlos Humberto Esquivel Sanchez  
Licenciatura en Desarrollo de Software - UABC
