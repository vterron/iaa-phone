IAA-CSIC Phone Book
===================

This Python script, ``iaa-phone``, serves as the *white pages* of the `Institute of Astrophysics of Andalusia <http://www.iaa.es>`_ (CSIC, Spain). It is a command-line application that queries the website in order to find the telephone number given a name or surname. Associate researchers are also included in the search, unlike visiting ones, which are not currently listed in the general alphabetical list.

The reverse telephone directory (*grey pages*) is also available, as searches may also be done by the phone number or e-mail address.

All searches are case- and accent-insensitive.

Examples
--------

.. code:: bash

  $ phone ter
  Cafetería IAA                    |      | 565 |
  Terrón Salas, Víctor Francisco   | UDIT | 605 | vterron
  Cafetería UDIT                   |      | 571 |
  [...]

Include multiple terms to restrict the search results:

.. code:: bash

  $ phone vic ter
  Terrón Salas, Víctor Francisco | UDIT | 605 | vterron

People can also be looked up by phone number:

.. code:: bash

  $ phone 605
  Terrón Salas, Víctor Francisco | UDIT | 605 | vterron
