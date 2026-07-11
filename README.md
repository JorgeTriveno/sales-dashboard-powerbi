# 📊 NovaFin — Dashboard de Rendimiento Comercial

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

> Proyecto de **Business Intelligence** a nivel empresarial enfocado en el sector financiero peruano. Desarrollado con Power BI, Python y un modelo de datos relacional de más de **15,000 registros**.

---

## 🗂️ Estructura del Proyecto

```
NovaFin/
├── 📁 data/
│   └── sales_data.xlsx        # Dataset generado sintéticamente con Python
├── 📄 generar_datos.py        # Script de automatización con Pandas
└── 📊 Dashboard_NovaFin.pbix  # Dashboard Power BI con Modelo Estrella y DAX
```

---

## 🚀 Componentes Principales

### 🐍 `generar_datos.py`
Script desarrollado en **Python con Pandas** para automatizar la creación del dataset a gran escala, aplicando lógica de conversión y metas de negocio reales del sector financiero peruano.

### 📁 `data/sales_data.xlsx`
Base de datos sintética con más de **15,000 registros**, estructurada para simular el comportamiento comercial real de asesores financieros por ciudad, canal de venta y producto.

### 📊 `Dashboard_NovaFin.pbix`
Dashboard interactivo estructurado bajo un **Modelo Estrella** (tablas Dimensión y Hechos), con KPIs calculados mediante medidas **DAX** y visualizaciones dinámicas filtrables en tiempo real.

---

## 📈 KPIs Implementados

| KPI | Descripción | Fórmula DAX |
|-----|-------------|-------------|
| 💰 **Monto Total Vendido** | Colocaciones totales en Soles (S/.) | `SUM(Hechos[Monto])` |
| 📋 **Total Colocaciones** | Transacciones exitosas por asesor | `COUNT(Hechos[ID_Colocacion])` |
| 🎯 **% Conversión** | Efectividad comercial del asesor | `DIVIDE([Total Colocaciones], [Total Contactos], 0)` |
| 🏆 **% Cumplimiento Meta** | Desempeño individual vs meta corporativa | `DIVIDE([Monto Total Vendido], [Meta Asignada], 0)` |

---

## 🌟 Características del Dashboard

- 🌑 **Diseño dark mode** profesional con identidad visual corporativa
- 🔍 **Filtros interactivos** por Asesor y Canal de Venta
- 🏙️ **Distribución geográfica** de ventas por ciudad (15+ sucursales)
- 🏆 **Ranking de asesores** por monto total vendido
- ⚡ **Actualización en tiempo real** al aplicar filtros

---

## 🛠️ Tecnologías Utilizadas

- **Power BI Desktop** — Visualización y modelado de datos
- **DAX** — Cálculo de medidas y KPIs
- **Python + Pandas** — Generación y automatización del dataset
- **Modelo Estrella** — Arquitectura relacional del modelo de datos
- **Power Query** — Transformación y limpieza de datos

---

## 👨‍💻 Autor

**Jorge Luis Triveño Cabrera**  
Ingeniero de Sistemas | Business Intelligence  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jorgeluistriveno/)

---

> *"Los datos no mienten. Un buen dashboard te lo demuestra."* 🚀
