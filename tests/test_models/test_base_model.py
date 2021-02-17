#!/usr/bin/python3

"""Unittest for base model module."""

from models.base_model import BaseModel
from datetime import datetime
import uuid
import unittest


class TestBaseModel(unittest.TestCase):
    """ test the base model class"""

    def test_base_model_id_format(self):
        """test if UUID is a string"""
        id_nbr = BaseModel()
        self.assertIsInstance(id_nbr.id, str)

    def test_base_model_created_at_format(self):
        """test if created_at is datetime format"""
        date = BaseModel()
        self.assertIsInstance(date.created_at, datetime)

    def test_base_model_updated_at_format(self):
        """test if date and time updated are in datetime format"""
        date = BaseModel()
        self.assertIsInstance(date.updated_at, datetime)

    def test_init(self):
        """Test instantiation"""
        instance = BaseModel()
        self.assertIs(type(instance), BaseModel)
        instance.name = "accomodation"
        attributes_types = {"id": str, "created_at": datetime,
                            "updated_at": datetime, "name": str}
        self.assertEqual(instance.name, "accomodation")
        self.assertIs(type(attributes_types), dict)

    def test_str(self):
        """test if the str method has the correct output"""
        instance = BaseModel()
        string = "[BaseModel] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(string, str(instance))

    def test_updated_at_after_save(self):
        """test if updated_at has the current datetime after save"""
        date = BaseModel()
        date_before_save = date.updated_at
        date.save()
        self.assertTrue(date.updated_at > date_before_save)

    def test_to_dict_noAditonalAttr(self):
        """check to_dict Attributes"""
        my_model = BaseModel()
        BaseModel.name = "holberton"
        attributes = {}
        for key, value in my_model.to_dict().items():
            if (key not in ('__class__', 'id', 'created_at', 'updated_at')):
                attributes[key] = value
        self.assertFalse(attributes)
