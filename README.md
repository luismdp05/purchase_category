# Módulo Purchase Category para Odoo 17

## Descripción
El módulo Purchase Category extiende las funcionalidades de compras en Odoo 17, permitiendo una mejor organización y gestión de las categorías en el proceso de compras.

## Obtener el código

```bash
# Clonar el repositorio
git clone https://github.com/luismdp05/purchase_category.git

# Cambiar al directorio del módulo
cd purchase_category

# Si estás trabajando en una rama específica
git checkout develop
```

## Desarrollo

### Requisitos previos
- Python 3.10 o superior
- Odoo 17.0
- Git

### Configuración del entorno de desarrollo
1. Crear un entorno virtual:
```bash
python -m venv venv
.\venv\Scripts\Activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Enlazar el módulo:
```bash
# Desde el directorio de addons de Odoo
New-Item -ItemType SymbolicLink -Path "custom_addons\purchase_category" -Target "ruta\al\modulo\purchase_category"
```

## Características principales

- Categorización avanzada de órdenes de compra
- Filtros y agrupaciones por categorías

## Instalación

1. Copie el módulo `purchase_category` en la carpeta `custom_addons`
2. Actualice la lista de aplicaciones en Odoo
3. Busque e instale el módulo "Purchase Category"

## Configuración

Después de la instalación:

1. Vaya a Compras > Configuración
2. Active las opciones de categorización que necesite
3. Configure las categorías de compra predeterminadas

## Uso

Para utilizar el módulo:

1. Al crear una nueva orden de compra, seleccione la categoría correspondiente
2. Utilice los filtros de categoría en la vista de lista de compras
3. Acceda a los reportes específicos por categoría desde el menú de Informes

## Requisitos

- Odoo 17.0
- Módulo base de compras (purchase) instalado

## Soporte

Para reportar problemas o solicitar nuevas funcionalidades, contacte al equipo de desarrollo.

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si deseas contribuir al proyecto:

1. Asegúrate de leer las guías de contribución de Odoo
2. Crea un fork del repositorio
3. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
4. Realiza tus cambios y haz commit
   - Usa mensajes de commit descriptivos
   - Sigue las convenciones de código de Odoo
5. Empuja tus cambios a tu fork (`git push origin feature/nueva-caracteristica`)
6. Abre un Pull Request con una descripción clara de los cambios

### 📖 Guías de Contribución

- Sigue los estándares de código de Odoo
- Documenta cualquier nueva funcionalidad
- Añade pruebas para las nuevas características
- Actualiza la documentación si es necesario
