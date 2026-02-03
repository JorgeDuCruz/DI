
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

  pode ter varios paragrafos

Outro Termo
  Podemos escribir outros termos

| Podemos definir bloque de texto
| Para iso usamos o caracter

.. _bloques-de-codigo:

Bloque de código
++++++++++++++++

Para codigo::

 bloque de codigo
 bloque 1
 bloque2

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

.. error::

  Trabucaches!

.. important::

  Ares tiene tecnicazas

.. warning::

  No vas a poder viciar, Jaja

.. note::

  Mañana tienes examen y no sabes nada

Outra forma de definir bloques de código a anterior, mirao en :ref:`bloques-de-codigo`.

.. code-block::
   :caption: un exemplo

     Esta liña precisa catro espazos

.. image:: _static/equis16x216.jpg

Este texto ten notas [#f1]_ para despois aclaralas no remate [#f2]_ do documento

Outro paragrafo en medio

.. rubric:: Notas o pe:

.. [#f1] Son aclaracions sobre o que se esta a describir
.. [#f2] Sueleb poñerse o fin do texto.
