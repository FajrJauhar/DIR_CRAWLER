# DIR_CRAWLER
# C2 Server and Directory Crawler

A project consisting of a Python-based C2 server and a directory crawler written in C, designed to exfiltrate directory structure and file logs.

## Project Overview

This project includes two main components:

- **C2 Server (Python)**: A Flask-based server that listens for requests on specified endpoints to handle logs and directory structure data.
- **Directory Crawler (C)**: A C program that scans the Desktop directory (or any specified directory) for files and subdirectories, sending the data to the C2 server for logging and processing.

## Features

- Directory scanning starts from the Desktop directory.
- Directory structure and file logs are sent to the server for storage.
- Logs are saved in a `.txt` file for later review.
- Python Flask server handles incoming POST requests for logs and structure data.
- Server and client are designed to run on local networks.

## Setup Instructions

To get started with this project, follow the instructions below:

1. Clone the repository to your local machine using the following command:
    ```bash
    git clone https://github.com/FajrJauhar/C2-server-and-directory-crawler.git
    ```

2. Ensure Python 3 and the required dependencies (Flask, Requests) are installed:
    ```bash
    pip install Flask requests
    ```

3. Run the Python C2 server:
    ```bash
    python C2.py
    ```

4. Compile and run the C directory crawler program to start scanning and sending data:
    ```bash
    gcc dir_crawler.c -o dir_crawler
    ./dir_crawler
    ```

## Endpoints

### `/structure` (POST)
Receives directory structure data in JSON format from the directory crawler.
```json
{
    "type": "directory", 
    "path": "/path/to/directory"
}

