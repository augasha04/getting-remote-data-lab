import requests
import json

# Start by creating a GetRequester class. 
# This class should be able to initialize with a string URL.

class GetRequester:

    def __init__(self, url):
        self.url = url

# The GetRequester class should have a get_response_body method,
# that sends a GET request to the URL passed in on initialization.
# This method should return the body of the response.

        response = requests.get(url)
        return response.content
    
    def get_response_body(self):
               
        # response = requests.get(url)
        # return response.content
    
    
# The GetRequester class should have a load_json method should,
# use get_response_body to send a request,
# then return a Python list or dictionary made up of data converted,
# from the response of that request.
    
    def load_json(self):
        response_body = self.get_response_body()
        json_data = json.loads(response_body)
        return json_data
    
    
# You can create an instance of the GetRequester 
# class by passing the URL as a string to the constructor  
  
url = 'https://jsonplaceholder.typicode.com/posts'
requester = GetRequester(url)
response_body = requester.get_response_body()
print(response_body)

json_data = requester.load_json()
print(json_data)