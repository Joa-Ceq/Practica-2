# Práctica 2 Ej 10

En este proyecto se analizan los resultados y se imprimen los mvp y puntajes finales de una serie de rondas de un juego de disparos.
El código fuente y los módulos necesarios se encuentran en el directorio `src`, y los notebooks de análisis, en la carpeta `notebooks`.

# Instalación de Dependencias

Para ejecutar este proyecto, se recomienda crear un entorno virtual y luego instalar las dependencias necesarias.

1- Crear un entorno virtual
```bash
python -m venv venv
```

2- Activar el entorno virtual
- En Windows:
  ```bash
  venv\Scripts\activate
  ```
- En macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

3- Instalar las dependencias
Ejecutar el siguiente comando en la terminal dentro del proyecto:
```bash
pip install -r requirements.txt
```

# Ejecución del Proyecto

Para analizar los datos, ejecutar el script principal:
```bash
python main.py
```

Si se desea trabajar desde un notebook, utilice Jupyter Notebook:
```bash
jupyter notebook
```
Dentro de Jupyter, navegue hasta la carpeta `notebooks` y abra el archivo main.ipynb.

# Estructura del Proyecto
```
Práctica 2/
│── notebooks/
    ├── main.ipynb       # Cóodigo fuente en formato notebook
│── src/                 # Código fuente y funciones
│   ├── calculators.py   # Funciones de cálculo
    ├── process.py       # Funciones principales
│── main.py              # Script principal del ejercicio
│── requirements.txt     # Dependencias del proyecto
│── README.md            # Instrucciones y documentación
```

## Autor
Joaquin Cequeira