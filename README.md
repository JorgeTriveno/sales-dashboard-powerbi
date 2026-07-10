# Proyecto NovaFin: Dashboard de Rendimiento Comercial

Este repositorio contiene un proyecto de Business Intelligence a nivel empresarial desarrollado con **Power BI**, **Python** y un modelo de datos relacional de **más de 15,000 registros** enfocado en el sector financiero peruano.

# Componentes del Proyecto
* **`data/sales_data.xlsx`**: Base de datos generada sintéticamente mediante Python con lógica de conversión y metas de negocio reales.
* **`generar_datos.py`**: Script de Python desarrollado con Pandas para automatizar la creación del dataset a gran escala.
* **`Dashboard_NovaFin.pbix`**: Archivo de Power BI estructurado bajo un **Modelo Estrella** (Tablas Dimensión y Hechos) y cálculo de KPIs mediante medidas **DAX**.

# KPIs Implementados
* **Monto Total Vendido**: Colocaciones totales formateadas en Soles (S/).
* **Total Colocaciones**: Transacciones exitosas por asesor.
* **% Conversión**: Efectividad comercial calculada a través de `DIVIDE([Total Colocaciones], [Total Contactos], 0)`.
* **% Cumplimiento Meta**: Evaluación del desempeño individual vs meta asignada corporativa.
