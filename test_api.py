import requests

# Open the test CSV file
with open('test_data.csv', 'rb') as f:
    files = {'file': f}
    
    # Send it to your API
    response = requests.post('http://localhost:8080/analyze', files=files)
    
    # Print the result
    print(response.json())