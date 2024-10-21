# Build the Docker image
docker build -t flask-app .

# Run the container
docker run -p 5000:5000 flask-app


Now, you can access the app by visiting http://localhost:5000 in your browser, and it should display "Hello, World!".


# Enter the container interactively
docker run -it flask-app /bin/bash

# Run the tests using Pytest
pytest
