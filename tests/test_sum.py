import unittest
from app import app

class TestAPI(unittest.TestCase):

    def setUp(self): #Constructor for Test Case
        self.app = app.test_client() #Using our app for testing

    #We want an endpoint to take in 2 numbers, add them together, 
    # and return the sum with a status of 200
    def test_sum(self):
        payload = {'num1': 3, 'num2': 5} #creating a payload that will be sent in the requst

        response = self.app.post('/sum', json=payload) #creating a POST request to our app at the /sum endpoint
        data = response.json

        self.assertEqual(data['result'], 8) #checking that the response includes a 'result' with a value of 8 (sum of 3 + 5)
        self.assertEqual(response.status_code, 200) #checking for success status code
