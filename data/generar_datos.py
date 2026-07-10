import pandas as pd
import random
from datetime import datetime, timedelta

print("🚀 Generando tu dataset de 15,000 filas... Por favor espera un momento.")

# Configuración de Listas base (Mercado Peruano)
asesores = [
    "Juan Quispe", "María Flores", "Carlos Mendoza", "Ana Rodriguez", "Luis Huamán",
    "Diana Villanueva", "Jorge Castaneira", "Rosa Palomino", "Pedro Sanchez", "Gisela Ramos",
    "Miguel Benites", "Lucía Espinoza", "Kevin Gonzales", "Sofía Castro", "Christian Farfán",
    "Fiorella Chunga", "Raúl Ortiz", "Milagros Cárdenas", "Manuel Chávez", "Elena Vivanco",
    "Diego Guerrero", "Vanessa Lázaro", "Renzo Miranda", "Camila Tello", "Ángel Rojas",
    "Fabiola Aguilar", "Arturo Pinedo", "Claudia Solís", "Javier Torres", "Natalia Vera"
]

ciudades = ["Lima", "Arequipa", "Trujillo", "Chiclayo", "Piura", "Iquitos", "Cusco", 
            "Huancayo", "Tacna", "Chimbote", "Pucallpa", "Cajamarca", "Ica", "Juliaca", "Huánuco"]

canales = ["Presencial", "WhatsApp", "Telemarketing", "Web"]

productos_config = {
    "Crédito Personal": {"min": 5000, "max": 30000},
    "Crédito Vehicular": {"min": 25000, "max": 75000},
    "Tarjeta de Crédito Gold": {"min": 1500, "max": 5000},
    "Tarjeta de Crédito Black": {"min": 6000, "max": 20000},
    "Préstamo Mivivienda": {"min": 120000, "max": 300000},
    "Crédito Mype": {"min": 10000, "max": 50000},
    "Compra de Deuda": {"min": 5000, "max": 40000},
    "Seguro de Vida": {"min": 500, "max": 2000}
}

productos = list(productos_config.keys())


metas_asesor = {asesor: random.randint(40000, 90000) for asesor in asesores}


data = []
fecha_inicio = datetime(2025, 1, 1)

for i in range(1, 15001):
    id_venta = f"VEN-{i:05d}"
    fecha_aleatoria = fecha_inicio + timedelta(days=random.randint(0, 364))
    asesor = random.choice(asesores)
    ciudad = random.choice(ciudades)
    producto = random.choice(productos)
    canal = random.choice(canales)
    
    
    clientes_contactados = random.randint(5, 40)
    
    ventas = random.randint(0, min(clientes_contactados, random.randint(1, 5))) 
    
    
    if ventas > 0:
        monto_unitario = random.randint(productos_config[producto]["min"], productos_config[producto]["max"])
        monto_vendido = monto_unitario * ventas
    else:
        monto_vendido = 0
        
    meta_mensual = metas_asesor[asesor]
    
    data.append([
        fecha_aleatoria.strftime("%Y-%m-%d"), id_venta, asesor, ciudad, 
        producto, clientes_contactados, ventas, monto_vendido, meta_mensual, canal
    ])


columnas = ["Fecha", "ID Venta", "Asesor", "Ciudad", "Producto", 
            "Clientes Contactados", "Ventas", "Monto Vendido", "Meta Mensual", "Canal de Venta"]

df = pd.DataFrame(data, columns=columnas)


df.to_excel("sales_data.xlsx", index=False, engine="openpyxl")

print("Archivo 'sales_data.xlsx' generado con éxito con 15,000 filas.")
print("Ahora muévelo a tu carpeta 'data/' y súbelo a GitHub desde GitHub Desktop.")