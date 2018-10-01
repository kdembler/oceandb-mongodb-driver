#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oceandb_driver_interface.oceandb import OceanDb

mongo = OceanDb('./tests/oceandb.ini').plugin


def test_plugin_type_is_mongodb():
    assert mongo.type == 'MongoDB'


def test_plugin_write_and_read():
    did = 'did:ocn-asset:0x123456789abcdefghi#path1'
    mongo.write({'value': 'test'}, did)
    assert mongo.read(did)['_id'] == did
    assert mongo.read(did)['value'] == 'test'
    mongo.delete(did)


def test_update():
    mongo.write({'value': 'test'}, 1)
    assert mongo.read(1)['value'] == 'test'
    mongo.update({'value': 'testUpdated'}, 1)
    assert mongo.read(1)['value'] == 'testUpdated'
    mongo.delete(1)


def test_plugin_list():
    mongo.write({'value': 'test1'}, 1)
    mongo.write({'value': 'test2'}, 2)
    mongo.write({'value': 'test3'}, 3)
    assert mongo.list().count() == 3
    assert mongo.list()[0]['value'] == 'test1'
    mongo.delete(1)
    mongo.delete(2)
    mongo.delete(3)


def test_plugin_query():
    mongo.write({'example': 'mongo'}, 1)
    assert mongo.query({'example': 'mongo'})[0]['example'] == 'mongo'
    mongo.delete(1)


def test_plugin_query_text():
    mongo.write({'key': 'A', 'value': 'test first'}, 1)
    mongo.write({'key': 'B', 'value': 'test second'}, 2)
    mongo.write({'key': 'C', 'value': 'test third'}, 3)
    mongo.write({'key': 'D', 'value': 'test fourth'}, 4)
    assert mongo.text_query('test', 'key', -1, 3, 0).count(with_limit_and_skip=True) == 3
    assert mongo.text_query('test', 'key', -1, 3, 0)[0]['key'] == 'D'
    assert mongo.text_query('test', 'key', -1, 3, 0)[1]['key'] == 'C'
    assert mongo.text_query('test', 'key', -1, 2, 1)[0]['key'] == 'B'
    mongo.delete(1)
    mongo.delete(2)
    mongo.delete(3)
    mongo.delete(4)
