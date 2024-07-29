verdaccio plugin for `Tutor <https://docs.tutor.edly.io>`__
###############################################################################

verdaccio plugin for Tutor


Installation
************

.. code-block:: bash

    pip install git+https://github.com/raccoongang/tutor-contrib-verdaccio

Usage
*****

The plugin must be enabled before starting to build any images.

.. code-block:: bash

    tutor plugins enable verdaccio
    tutor local start -d verdaccio
    tutor images build mfe
    tutor images build openedx

License
*******

This software is licensed under the terms of the AGPLv3.
