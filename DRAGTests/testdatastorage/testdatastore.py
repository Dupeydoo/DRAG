import os.path

import numpy as np
import pandas as pd
from django.test import TestCase

from DRAG.datacontext import context
from DRAGNN.storage import datastore
from DRAGTests.mock.mockpopulation import MockPopulation

"""
Datastore test module.

    Author:
        James
    
    Version:
        1.0.0
"""


class TestDataStore(TestCase):
    """
    A testing class for the datastore module in DRAGNN.

    Attributes:
        population (:obj:`list` of :obj:`Track`): Population to store in a test
        data file.

        user_id (:obj:`str`): The unique string identifier for a user.
        context (:obj:`dict`): Dictionary of algorithm parameters.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        datastore.current_path = datastore.test_path
        self.population = MockPopulation().population
        self.user_id = "test_user"
        self.context = context
        datastore.store_data(self.population, self.user_id)

    def test_store_data(self):
        """
        Tests the store_data method in setUp was successful.
        """
        path = datastore.test_path + "test_userdata.h5"
        exists = os.path.isfile(path)

        # Select the data.
        store = pd.HDFStore(path)
        content = list(store.select("track"))
        fitnesses = list(store.select("fitness"))

        self.assertTrue(content,
                        "The population content was not added to the store!")
        self.assertTrue(fitnesses,
                        "The population fitnesses were not added to the store!")
        self.assertTrue(exists, "The data file was not stored!")

    def test_read_data_store(self):
        """
        Tests the read_data method.
        """
        track_np, fitness_np = datastore.read_data(8, self.user_id)

        # Ensure that numpy arrays are created.
        track_instance = True if isinstance(track_np, np.ndarray) else False
        fitness_instance = True if isinstance(fitness_np, np.ndarray) else False

        self.assertTrue(track_instance,
                        "The returned instance should be a numpy array!")
        self.assertTrue(fitness_instance,
                        "The returned instance should be a numpy array!")

    def test_get_data_store(self):
        """
        Tests that the data store can be retrieved externally.
        """
        store = datastore.get_data_store(self.user_id)
        instance = True if isinstance(store, pd.HDFStore) else False
        self.assertTrue(instance, "The returned instance should be a HDFStore!")

    def test_delete_data_store(self):
        """
        Tests that a particular data store can be deleted.
        """
        datastore.delete_data_store(self.user_id)
        path = datastore.test_path + "test_userdata.h5"
        exists = os.path.exists(path)
        self.assertFalse(exists, "The file should have been cleared!")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.population, self.user_id, self.context
