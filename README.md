# Vulnerable Flask API

This project demonstrates common vulnerabilities affecting backend APIs: 
 - SQL Injection
 - Weak Cryptography

## The API
The `POST /user/login` endpoint accepts form-urlencoded params `username` and `password`.

The database is initialized with two users, `alice`, and `bob`.

The `GET /` endpoint will return a basic web page, and on the server it will print out the database contents.

A `POST /user` endpoint also exists to create new users.

## Setup

### Create/Activate virtual environment

If no virtual environment exists, run the following to create a virtual environment named `myvenv` (or whatever you want).
```sh
python -m venv myvenv
```

Activate (macOS, Linux):
```shell
. ./myvenv/bin/activate
```

Activate (Windows):
```powershell
. ./myvenv/bin/activate.ps1
```
Deactivate by entering the `deactivate` command.

### Install dependencies
With the virtual environment active, run
```shell
pip install -r requirements.txt
```

## Vulnerabilities
### SQL Injection vuln

Verify by sending the payload:
```shell
curl -X POST --data-urlencode "username=bob' AND 1=1; --" --data-urlencode "password= " http://127.0.0.1:5000/user/login
```

### Weak Cryptographic Algorithm
SHA1 is used 

