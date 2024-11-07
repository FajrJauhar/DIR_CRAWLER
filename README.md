# DIR_CRAWLER
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>C2 Server and Directory Crawler</title>
</head>
<body>

    <header>
        <h1>C2 Server and Directory Crawler</h1>
        <p>A project consisting of a Python-based C2 server and a directory crawler written in C, designed to exfiltrate directory structure and file logs.</p>
    </header>

    <section>
        <h2>Project Overview</h2>
        <p>This project includes two main components:</p>
        <ul>
            <li>
                <strong>C2 Server (Python)</strong>: A Flask-based server that listens for requests on specified endpoints to handle logs and directory structure data.
            </li>
            <li>
                <strong>Directory Crawler (C)</strong>: A C program that scans the Desktop directory (or any specified directory) for files and subdirectories, sending the data to the C2 server for logging and processing.
            </li>
        </ul>
    </section>

    <section>
        <h2>Features</h2>
        <ul>
            <li>Directory scanning starts from the Desktop directory.</li>
            <li>Directory structure and file logs are sent to the server for storage.</li>
            <li>Logs are saved in a `.txt` file for later review.</li>
            <li>Python Flask server handles incoming POST requests for logs and structure data.</li>
            <li>Server and client are designed to run on local networks.</li>
        </ul>
    </section>

    <section>
        <h2>Setup Instructions</h2>
        <p>To get started with this project, follow the instructions below:</p>
        <ol>
            <li>Clone the repository to your local machine using the following command:
                <pre>git clone https://github.com/FajrJauhar/C2-server-and-directory-crawler.git</pre>
            </li>
            <li>Ensure Python 3 and the required dependencies (Flask, Requests) are installed:
                <pre>pip install Flask requests</pre>
            </li>
            <li>Run the Python C2 server:
                <pre>python C2.py</pre>
            </li>
            <li>Compile and run the C directory crawler program to start scanning and sending data:
                <pre>gcc dir_crawler.c -o dir_crawler</pre>
                <pre>./dir_crawler</pre>
            </li>
        </ol>
    </section>

    <section>
        <h2>Endpoints</h2>
        <h3>/structure (POST)</h3>
        <p>Receives directory structure data in JSON format from the directory crawler.</p>
        <pre>
{
    "type": "directory", 
    "path": "/path/to/directory"
}
        </pre>
        <h3>/logs (POST)</h3>
        <p>Receives file log data in form data from the crawler (e.g., filename).</p>
    </section>

    <section>
        <h2>Files</h2>
        <ul>
            <li><strong>C2.py</strong> - Python Flask server handling incoming data and saving it to files.</li>
            <li><strong>dir_crawler.c</strong> - C program that scans the Desktop directory and sends structure/file data to the C2 server.</li>
        </ul>
    </section>

    <section>
        <h2>License</h2>
        <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
    </section>

</body>
</html>
