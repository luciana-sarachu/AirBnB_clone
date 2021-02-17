#!/usr/bin/python3


from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place
import unittest

"""Test Console"""


class TestConsole(unittest.TestCase):

    """test if all required classes are created correctly"""

    def test_classes(self):

        """Test if all required classes are present"""

        user_example = User()
        city_example = City()
        amenity_example = Amenity()
        state_example = State()
        review_example = Review()
        place_example = Place()
        self.assertEqual(user_example.__class__.__name__, "User")
        self.assertEqual(city_example.__class__.__name__, "City")
        self.assertEqual(amenity_example.__class__.__name__, "Amenity")
        self.assertEqual(state_example.__class__.__name__, "State")
        self.assertEqual(review_example.__class__.__name__, "Review")
        self.assertEqual(place_example.__class__.__name__, "Place")

    def test_father(self):

        """ test if all required classes inherit correcly from BaseModel"""

        user_example = User()
        city_example = City()
        amenity_example = Amenity()
        state_example = State()
        review_example = Review()
        place_example = Place()
        self.assertTrue(issubclass(user_example.__class__, BaseModel))
        self.assertTrue(issubclass(city_example.__class__, BaseModel))
        self.assertTrue(issubclass(amenity_example.__class__, BaseModel))
        self.assertTrue(issubclass(state_example.__class__, BaseModel))
        self.assertTrue(issubclass(review_example.__class__, BaseModel))
        self.assertTrue(issubclass(place_example.__class__, BaseModel))