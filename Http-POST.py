import requests

url = input('Enter the URL for the POST request: ')
num_requests = int(input('Enter the number of requests to send: '))
data_size = 10000  # Example data size of 10,000 bytes

data = 'x' * data_size  # Create a string of 'x's with the specified data size

for i in range(num_requests):
    print(f'Request {i+1}: Sending POST request to: {url}')
    response = requests.post(url, data={'data': data})
    if response.status_code == 201:  # 201 Created
        response_data = response.json()
        print(f'Response {i+1}:', response_data)
    else:
        print(f'Failed to make request {i+1}:', response.status_code, response.text)
