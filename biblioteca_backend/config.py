import os

class Config:
    """
    Clase de configuración para la aplicación.

    Atributos:
        SQLALCHEMY_DATABASE_URI (str): URI de la base de datos que se utilizará.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Si se deben rastrear o no modificaciones en los objetos de la base de datos.
    """
    
    # URI de conexión a la base de datos MySQL
    SQLALCHEMY_DATABASE_URI = (
        'mysql://uyatqkdz9bqlwawj:'  # Usuario de la base de datos
        'Zboq569HsIwhVBPD8wuw@'       # Contraseña de la base de datos
        'bnvdmhsfgblvagbb6b2p-mysql.services.clever-cloud.com:'  # Host de la base de datos
        '3306/'                        # Puerto de la base de datos
        'bnvdmhsfgblvagbb6b2p'         # Nombre de la base de datos
    )
    
    # Configuración para desactivar el seguimiento de modificaciones
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactivar el seguimiento de modificaciones para evitar overhead

