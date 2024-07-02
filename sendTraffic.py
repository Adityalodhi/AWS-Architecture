import requests

# URL of the load balancer
load_balancer_url = 'http://your-load-balancer-url.com'

# Function to send multiple requests
def send_multiple_requests(requests_count):
    for _ in range(requests_count):
        response = requests.get(load_balancer_url)
        print(f"Status Code: {response.status_code}")


if __name__ == "__main__":
    # Number of requests to send
    requests_count = 100
    # Send the requests
    send_multiple_requests(requests_count)
