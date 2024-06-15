# Biblus
[![CI: Biblus](https://github.com/yegres280/biblus/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/yegres280/biblus/actions/workflows/main.yml)

The service for finding and dowloading books using **Onion Network**.


## Technology Stack
![nginx](https://img.shields.io/badge/nginx-green.svg?&style=for-the-badge&logo=nginx&logoColor=white)
![docker](https://img.shields.io/badge/docker-%232496ED.svg?&style=for-the-badge&logo=docker&logoColor=white)
![Github Actions](https://img.shields.io/badge/-Github%20Actions-black?style=for-the-badge&logo=githubactions)
![python](https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=yellow)
![pydantic](https://img.shields.io/badge/-Pydantic-%23CC0000?style=for-the-badge&logo=pydantic)
![pytest](https://img.shields.io/badge/-Pytest-b0c4de?style=for-the-badge&logo=pytest)
![fastapi](https://img.shields.io/badge/fastapi%20-%2313988a.svg?&style=for-the-badge&logo=fastapi&logoColor=white)
![redis](https://img.shields.io/badge/redis%20-%23CC0000.svg?&style=for-the-badge&logo=redis&logoColor=white)
![ElasticSearch](https://img.shields.io/badge/-ElasticSearch-005571?style=for-the-badge&logo=elasticsearch)
![TOR](https://img.shields.io/badge/-Tor-7D4698?style=for-the-badge&logo=torbrowser)



## Table of Contents
- [Biblus](#biblus)
  - [Technology Stack](#technology-stack)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [Docker Compose installation:](#docker-compose-installation)
    - [Local installation](#local-installation)
  - [Usage](#usage)
  - [DEMO](#demo)
  - [License](#license)


## Features
1. API built with **FastAPI**
2. Strong typization with **pydantic** and standart python library
3. Intergrational tests with **pytest**
4. **CI/CD:** Linting, Docker Compose, Tests in **Github Actions**
5. **Elasticsearch** stores data about books in JSON format. The storage is easily replacable
6. A user can find books using **Full Text Search** and get download links for a certain book
7. The user can download a book directly from the app if there is a **Tor** link for a book in a storage so app can download a file and give it to a user
8. The service is easily deployed using **Docker Compose**
9.  Caching with **Redis** (replacable) and [FastAPI-Cache](https://github.com/long2ice/fastapi-cache)
10. **Nginx** as web-server

## Installation

### Docker Compose installation:
1. Clone the repository:
```bash
 git clone https://github.com/yegres280/biblus.git
```
2. Build Docker Compose:
```bash
 docker compose up -d
```

### Local installation
1. Clone the repository:
```bash
 git clone https://github.com/yegres280/biblus.git
```
2. Install dependencies:
```bash
 cd biblus/src/ && python -m venv .venv && cd .. && pip install -r requirements/local.txt
```

## Usage
1. Launch
``` bash
 cd src && python main.py
```

## DEMO



## License
This project is licensed under the [Open Software License 3.0](LICENSE)
