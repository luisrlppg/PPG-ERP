import pandas as pd
import uuid

def generar_archivos(input_file, output_file1, output_file2):
    # Diccionario de reemplazo de categorías
    categoria_mapping = {
        "ALAMBRE": "Materia Prima / Alambre",
        "BOTELLA": "Botella",
        "CEPILLOS": "Cepillo",
        "CERDA": "Materia Prima / Cerda",
        "EMPAQUE": "Empaque",
        "ESCURRIDORES": "Escurridor",
        "GALLETA": "Galleta",
        "INSERTO CON ROSCA 13mm": "Inserto de sobre tapa",
        "MANGOS": "Mango",
        "MATERIAL VIRGEN": "Materia Prima",
        "OPRESOR": "Opresor",
        "PIGMENTOS": "Materia Prima / Pigmentos",
        "PINCELES": "Pincel",
        "PRODUCTO COMPLETO": "Producto Final",
        "TAPAS": "Tapa"
    }
    
    # Diccionario de reemplazo de ubicaciones
    ubicacion_mapping = {
        "1 Embarque": "Embarque",
        "Almacen de Pigmentos": "Pigmentos",
        "B11 CUARENTENA": "B11_Cuarentena",
        "CUARENTENA": "Cuarentena",
        "PARA REVISAR": "Revision",
        "PISO DE ALMACEN": "Piso_De_Almacen"
    }
    
    # Cargar el archivo CSV original
    df = pd.read_csv(input_file, dtype=str)
    
    # Eliminar la última fila si corresponde a un total en lugar de un artículo
    df = df.iloc[:-1]
    
    # Generar el primer archivo con product_id y product_type
    df1 = df[['Artículo', 'Categoría', 'Valor de costo', 'Descripción']].copy()
    df1.insert(0, 'product_id', [str(uuid.uuid4()) for _ in range(len(df1))])  # Generar IDs únicos
    df1.insert(2, 'Product Type', 'Storable Product')
    
    # Reemplazar las categorías según el diccionario
    df1['Categoría'] = df1['Categoría'].replace(categoria_mapping)
    
    # Eliminar duplicados basándose en la columna 'Artículo'
    df1 = df1.drop_duplicates(subset=['Artículo'])
    
    # Guardar el primer archivo como CSV
    df1.to_csv(output_file1, index=False)
    
    # Generar el segundo archivo con las columnas requeridas
    df2 = df[['Artículo', 'Ubicación', 'Cantidad']].copy()
    
    # Reemplazar las ubicaciones según el diccionario y reemplazar espacios por '0'
    df2['Ubicación'] = df2['Ubicación'].replace(ubicacion_mapping).str.replace(" ", "0")
    
    # Agregar sufijo a las ubicaciones
    df2['Ubicación'] = "alm/Stock/" + df2['Ubicación']
    
    # Quitar espacios en la columna Cantidad
    df2['Cantidad'] = df2['Cantidad'].str.replace(" ", "")
    
    # Guardar el segundo archivo como CSV
    df2.to_csv(output_file2, index=False)
    
    print(f'Archivos generados:\n  - {output_file1}\n  - {output_file2}')

original = './../../docs/last_inv.csv'
productos = './../../docs/productos.csv'
ubicaciones = './../../docs/ubicaciones.csv'

# Uso del script
generar_archivos(original, productos, ubicaciones)
