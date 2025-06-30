# Documented Vulnerabilities in Damn-Vulnerable-Test-App

## Backend
- **Hardcoded AWS, Slack, Google API keys** in `backend/config.py`
- **SQL Injection** in `/login` and `/search` endpoints in `backend/app.py`
- **Command Injection** in `/ping` endpoint in `backend/app.py`
- **SSRF** in `/fetch` endpoint in `backend/app.py`
- **Use of hardcoded credentials in code** (`backend/utils.py`, `backend/app.py`)
- **Dependency Confusion**: `internal-company-utils` in `backend/requirements.txt`
- **Insecure dependencies**: Outdated Flask, requests, mysql-connector in `backend/requirements.txt`
- **Insecure Deserialization**: `/deserialize` endpoint in `backend/app.py`
- **Path Traversal**: `/readfile` endpoint in `backend/app.py`
- **Insecure Direct Object Reference (IDOR)**: `/user` endpoint in `backend/app.py`
- **Sensitive Data Exposure**: `/env` endpoint in `backend/app.py`
- **Weak Hashing**: `/hash` endpoint in `backend/app.py`
- **Open Redirect**: `/redirect` endpoint in `backend/app.py`
- **Unrestricted File Upload**: `/upload` endpoint in `backend/app.py`
- **XXE**: `/xml` endpoint in `backend/app.py`
- **More Dependency Confusion**: `internal-company-crypto`, `internal-company-xml` in backend/frontend dependencies
- **Insecure Deserialization**: Use of `pickle.loads` in backend

## Frontend
- **Hardcoded API keys** in `frontend/src/api.js`
- **XSS**: User input rendered with `dangerouslySetInnerHTML` in `frontend/src/App.js`
- **Dependency Confusion**: `internal-company-ui` in `frontend/package.json`
- **Insecure dependencies**: Outdated React, ReactDOM, axios in `frontend/package.json`
- **Insecure Local Storage Usage**: Storing tokens in `localStorage` in `frontend/src/App.js`
- **Open Redirect**: Redirecting based on query string in `frontend/src/App.js`
- **CSRF**: Form submits to backend without CSRF token in `frontend/src/App.js`
- **Insecure Randomness**: Use of `Math.random()` for tokens in `frontend/src/App.js`
- **Sensitive Data in Source Maps**: Fake secret in code comment in `frontend/src/App.js`
- **More Dependency Confusion**: `internal-company-crypto`, `internal-company-xml` in `frontend/package.json`
- **Insecure dependencies**: Outdated jQuery in `frontend/package.json`

---

This application is intentionally vulnerable for SAST/SCA scanner testing. Do NOT deploy in production. 