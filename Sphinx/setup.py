from distutils.core import setup

from setuptools import find_packages

setup(name = "Aplicación de exemplo de distribución",
      version="0.1",
      description="Exemplo de uso de distutils",
      long_description="""Descripción longa do proxecto, con explicación en
                          varias liñas formando parte da documentación
                          do paquete distribuible.""",
      author= "Jorge",
      author_email="jdurancruz@danielcastelao.org",
      license="GLP",
      scripts=["lanzador.sh"],
      py_modules=["apoio"],
      packages= find_packages(),  #packages=["cod","documentacion"],
      package_data= {
          "documentacion":["html/*.html","html/searchindex.js","html/_static/*.js","html/_static/*.css",
                           "html/_images/equis16x216.jpg"]
      }
      )
