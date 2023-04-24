# API-First-Video

## Instalación para dev
Utilicen una versión de Python 3.10 o menor.
Crear primero BD en postgresql First-Video, las tablas se crearan solas cuando se ejecute el programa.
### 1. Instalar las dependencias de Python:
**Recomiendo utilizar un ambiente virtual**

```pip install -r requirements.txt```

<br>

### 2. Desde la carpeta src ejecutar la API:
```uvicorn main:app --reload```

### Si no funciona utilizar el siguiente comando:
```python -m uvicorn:app --reload```

<br>

### 3. ¡A trabajar!