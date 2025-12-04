# Análisis lealtad aerolínea

Este proyecto tiene como objetivo analizar el comportamiento y las características de los clientes de un programa de fidelización de una aerolínea. A través del estudio de datos (actividad de vuelos y datos demográficos), se busca comprender mejor a los clientes para implementar mejoras y orientar los esfuerzos estratégicos de manera más precisa.

## 📌 Índice

- Descripción del Proyecto
- Datos Utilizados
- Objetivos del Análisis
- Requisitos y Tecnologías
- Estructura del Repositorio
- Instrucciones de Uso
- Tareas del Proyecto
- Visualizaciones Solicitadas
- Autoría
- Funcionamiento 

## 📝 Descripción del Proyecto

Este repositorio forma parte del Módulo 3 del curso de Data Analyst. El objetivo principal es realizar un análisis exploratorio, limpieza y visualización de datos provenientes de un programa de lealtad de una aerolínea.

Incluye la carga, unión, limpieza y análisis de dos bases de datos:

Actividad de vuelos y puntos acumulados/redimidos.

Información demográfica y de fidelidad de los clientes.

## 📂 Datos Utilizados

El dataset está compuesto por dos archivos CSV:

1️⃣ Customer Flight Analysis.csv
Contiene registros mensuales de actividad aérea de los clientes

2️⃣ Customer Loyalty History.csv
Incluye datos demográficos y de membresía.



## 🎯 Objetivos del Análisis

- Conocer mejor a los clientes de la aerolínea para orientar estratégicamente los esfuerzos del programa de fidelización.
- Identificar patrones en la actividad de vuelos y uso de puntos.
- Explorar diferencias entre perfiles demográficos, niveles educativos, salarios y tipos de tarjeta.
- Detectar oportunidades de mejora en el programa de lealtad.

## 🛠️ Requisitos y Tecnologías

**Librerías utilizadas**
- pandas
- numpy
- seaborn
- matplotlib

**Entorno**
- VS Code
- Jupyter Notebook
- Git / GitHub

## 📁 Estructura del Repositorio

(🚨🚨🚨🚨 ADAPTAR AL TERMINAR EL PROYECTO 🚨🚨🚨🚨)

/
├── data/
│   ├── Customer Flight Analysis.csv
│   ├── Customer Loyalty History.csv
│
├── notebooks/
│   ├── 01_exploracion.ipynb
│   ├── 02_limpieza.ipynb
│   ├── 03_visualizaciones.ipynb
│
├── src/
│   ├── cleaning.py
│   ├── utils.py
│
├── README.md
└── .gitignore

## ▶️ Instrucciones de Uso


Ejecutar los notebooks:

jupyter notebook


Explorar los scripts de la carpeta /src
(limpieza, funciones auxiliares, procesamiento, etc.)

## 📊 Tareas del Proyecto
**Fase 1: Exploración y Limpieza**
- Análisis inicial: nulos, tipos de datos, estadísticas, duplicados.
- Unión eficiente de los datasets por Loyalty Number.
- Limpieza: conversión de tipos, imputación o eliminación de nulos, validación de consistencia.

**Fase 2: Visualización**
Responder mediante visualizaciones a:
- Distribución de vuelos reservados por mes.
- Relación entre distancia volada y puntos acumulados.
- Distribución de clientes por provincia/estado.
- Comparación de salario promedio por nivel educativo.
- Proporción de tipos de tarjeta de fidelidad.
- Distribución de clientes según estado civil y género.

## 👤 Autoría

Proyecto realizado como parte del Módulo 3 del curso Data Analyst por **Elena Pavón Fernández**


## Funcionamiento.

El proyecto comienza con el ipynb de 01_exploracion. 
Arranca importando las librerías que van a ser necesarias para el EDA.  
- Fase uno: explorar los csv para conocerlos y ver qué columna o columnas pueden necesitar limpieza. 

![alt text](image-1.png)
Imagen 1: Visualización de uno de los CSV
- Para explorarlo vamos a usar métodos como: .head(), .size(), .shape(), .unique()... 
- Durante el proceso observo que tenemos una categoría dentro de la columna Education sin ningún dato y decido imputarlos calculando la media entre las medianas de las categorias superior e inferior de la misma.
- Los salarios están muy dispersos. 
Boxplot Salary antes de la corrección:
![alt text](image.png)

- **La fase de visualización es bastante interesante y esclarecedora**
![alt text](image-2.png)
Gráfico que muestra la relación absolutamente proporcional entre distancia volada y puntos acumulados

![alt text](image-3.png)
Gráfico que muestra la cantidad de clientes según género y estado civil

![alt text](image-4.png)
Gráfica que muestra la evolución de reserva de vuelos durante el año, mostrando la diferencia entre dos años. 

