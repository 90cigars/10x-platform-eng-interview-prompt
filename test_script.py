import requests

# Define the base URL of your service API
base_url = "http://localhost:5001"

# Define test cases
test_cases = [
    {"url": "/query?limit=5", "expected_status_code": 200},
    {"url": "/query?date=2012-06-04", "expected_status_code": 200},
    {"url": "/query?weather=rain", "expected_status_code": 200},
    {"url": "/query?weather=rain&limit=5", "expected_status_code": 200},
]

# Run test cases
for test_case in test_cases:
    url = base_url + test_case["url"]
    response = requests.get(url)
    
    if response.status_code == test_case["expected_status_code"]:
        print(f"PASS: {url}")
    else:
        print(f"FAIL: {url} (Expected: {test_case['expected_status_code']}, Actual: {response.status_code})")
