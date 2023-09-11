## Prerequisites
Before you can use this project, you'll need to have the following software installed on your system:
- Python (version 3.10 or higher)
- Docker

## Installation 

Use the package manager to install requests.

```bash
pip install requests
```

## Project Structure
The project consists of the following components:

api.py: This Python script is responsible for fetching and displaying a list of Pokémon from Generation 3 using the PokeAPI.

Dockerfile: This Dockerfile contains instructions for building a Docker image that encapsulates the Python script and its dependencies for easy deployment.

## Usage
## Running the Python Script 
1. Open a terminal.
2. Navigate to the directory containing the api.py file.
3. Run the following command to execute the script:

```bash
python api.py
```
4. The script will make an API request to retrieve the list of Pokémon from Generation 3 and display the results in the terminal.

## Installing the library
We create a requirements.txt file by creating a virtual environment. After activating a virtual environment, we have to run the command as follows:

```bash
pip freeze > requirements.txt
```
## Running the Script Inside a Docker Container
1. Ensure that you have Docker installed and running on your system.
2. Open a terminal.
3. Navigate to the directory containing the Dockerfile and api.py files.
4. Build a Docker image using the following command (replace pokemon-gen3-finder with your desired image name):
```bash
docker build -t pokemon-gen3-finder .
```
5. Once the image is built successfully, you can run a Docker container with the following command:
```bash
docker run pokemon-gen3-finder
```
6. The Docker container will execute the Python script, retrieve the list of Pokémon from Generation 3, and display the results in the container's terminal.

## Contributing
If you would like to contribute to this project, feel free to submit pull requests or open issues on the GitHub repository.

## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).