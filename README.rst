=====================
oceandb-mogodb-driver
=====================


.. image:: https://img.shields.io/pypi/v/oceandb-mongodb-driver.svg
        :target: https://pypi.python.org/pypi/oceandb-mongodb-driver

.. image:: https://img.shields.io/travis/oceanprotocol/oceandb-mongodb-driver.svg
        :target: https://travis-ci.com/oceanprotocol/oceandb-mongodb-driver

.. image:: https://readthedocs.org/projects/oceandb-plugin-system/badge/?version=latest
        :target: https://oceandb-plugin-system.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/oceanprotocol/oceandb-mongodb-driver/shield.svg
     :target: https://pyup.io/repos/github/oceanprotocol/oceandb-mongodb-driver/
     :alt: Updates



MongoDB driver to connect implementing OceanDB.

* Free software: Apache Software License 2.0
* Documentation: https://oceandb-plugin-system.readthedocs.io.


How to use it
-------------

First of all we have to specify where is allocated our config.
To do that we have to pass the following argument:

.. code-block:: python

    --config=/path/of/my/config
..

If you do not provide a configuration path, by default the config is expected in the config folder.

In the configuration we are going to specify the following parameters to

.. code-block:: python

    [oceandb]

    enabled=true
    #location of plugin class
    module=mongo
    module.path=plugins/
    #plugin connection
    db.hostname=localhost
    db.port=27017
    db.username=
    db.password=
    db.name=test
    db.collection=protokeeper
..

Once you have defined this the only thing that you have to do it is use it:

.. code-block:: python

    oceandb = OceanDb(conf)
    oceandb.write({"id": 1, "value": "test"})

..
