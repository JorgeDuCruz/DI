
===============================
Introducción a restructure text
===============================

------------------------------------------
Breve introducción a escritura de docs rst
------------------------------------------

Título
======


Subtítulo
---------

Título de sección
~~~~~~~~~~~~~~~~~

Outro máis
++++++++++

Outro máis
**********

Texto plano sen ningunha marca considérase un párrafo

En calquera texto necesitamos **remarcar** o contido. Para chamar atención dentro dun texto utilizase a *cursiva*, que remarca a palabra dentro de un texto. Tamen usase as ``comillas`` para mostrar exemplos de código

Como escribir \* e \'.
;;;;;;;;;;;;;;;;;;;;;;

Para o uso de \ * hai que usar as barras de escape \\. Lo mismo para las comillas

* Esta é unha lista desordenada
* Ten dous elementos. Este elemento pode
  ocupar dúas liñas.

  * sublista

1. Primeiro elemento dunha lista ordenada
2. Segundo elemento

  #. sublista

#. Esto tamén é ordenado

#. Vaise numerando solo

Termo
  Definición do termo, que ten que estar sangrado

  pode ter varios parrafo

Outro Termo
  Podemos escribir outros termos

| Podemos definir bloque de texto
| Para iso usamos o caracter


Para codigo no sé

Taboas
******

+------------------------+-----------------+----------+---------------+
|Cabeceira liña columna 1| Cab2            |Cab3      | Cab4          |
|Cabeceira opcional      |                 |          |               |
+========================+=================+==========+===============+
|elemento 1,1            |col2             |col3      |col4           |
+------------------------+-----------------+----------+---------------+


===================== ============== ====================
Outra táboa            Columna2        Columna 3
===================== ============== ====================
Elemento 1            ele 2           ele 3
Elemento 1            ele 2           ele 3
Elemento 1            ele 2           ele 3
Elemento 1            ele 2           ele 3
===================== ============== ====================

Enlaces
*******

este texto pode ter un enlace a `Sphinx`_.

.. _Sphinx: https://www.sphinx-doc.org

Se poden definir `enlaces <https://google.com/>`_ inline

.. attention::

  O texto que queremos incluir no bloque!

.. caution::

  Coidado !!

.. danger::

  Uui, miedito!