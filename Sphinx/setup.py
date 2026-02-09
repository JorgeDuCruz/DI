from distutils.core import setup

setup(name = "Aplicación de exemplo de distribución",
      version="0.1",
      description="Exemplo de uso de distutils",
      long_description="""Descripción longa do proxecto, con explicación en
                          varias liñas formando parte da documentación
                          do paquete distribuible.""",
      author= "Jorge",
      author_email="jdurancruz@danielcastelao.org",
      license="GLP",
      scripts=["main.py"])
