from cgi import test
from cgitb import reset
from urllib import response
from main import app
import unittest


class FlaskApplicationTesting(unittest.TestCase):

    def test_server_is_live(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)


    def test_endpoint_1(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/domain-data-minor")
        self.assertEqual(response.status_code, 200)

    def test_endpoint_2(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/domain-threat-analysis")
        self.assertEqual(response.status_code, 200)

    
    def test_endpoint_3(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/domain-time-series", query_string={'start': "2022-01-20", "end": "2022-04-20"})
        self.assertEqual(response.status_code, 200)
    
        
    def test_endpoint_4(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/configuration")
        self.assertEqual(response.status_code, 200)

    def test_endpoint_5(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/domain/{}".format("aoins.com"))
        self.assertEqual(response.status_code, 200)
 
    def test_endpoint_6(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/configuration/{}".format("Ulster University"))
        self.assertEqual(response.status_code, 200)

    def test_endpoint_6(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/configuration/{}".format("Ulster University"))
        self.assertEqual(response.status_code, 200)

    def test_endpoint_7(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/configuration/{}".format("INCORRECT INFORMATION"))
        self.assertEqual(response.status_code, 404)

        
if __name__ == "__main__":
    unittest.main()