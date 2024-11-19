# Vehicle Listings Web Application

This project demonstrates how to containerize a simple Flask web application that displays vehicle listings stored in a PostgreSQL database. Using Docker, we can easily set up and deploy the entire application stack with two containers: one for the Flask API and one for the PostgreSQL database.

### Project Overview

- **Flask Web Application**: The application serves a simple webpage that lists car details (make, model, year, color, price) retrieved from a PostgreSQL database.
- **PostgreSQL Database**: Stores vehicle data, including car details.
- **Docker**: The application and database are containerized to ensure easy deployment and consistency across environments.

### Steps to Set Up the Project

1. **Create Two Containers**:
   - **Flask Application Container**: Hosts the Flask app that interfaces with the database.
   - **PostgreSQL Database Container**: Hosts the PostgreSQL database containing car listings.

2. **Database Initialization**:
   - Create an `init-db/init.sql` script to:
     - Set up a `vehicle` database.
     - Create a `cars` table with the following schema:
     - 
       id SERIAL PRIMARY KEY,
       make VARCHAR(50),
       model VARCHAR(50),
       year INT,
       color VARCHAR(20),
       price DECIMAL(10, 2)


   - Insert some dummy data into the table to populate the database.

3. **Dockerfile**:
   - Create a `Dockerfile` for the Flask API container to install dependencies and run the Flask application.

4. **Connect Flask to PostgreSQL**:
   - Configure the Flask application to connect to the PostgreSQL container and fetch data from the `cars` table.

### Running the Application

1. **Build and Start the Containers**:
   - Use Docker commands to build and run the application and database containers.

2. **Access the Application**:
   - After the containers are running, open your browser and go to `http://localhost:5000` to view the vehicle listings.

### Expected Outcome

If the project is set up correctly, visiting `localhost:5000` will display a simple webpage with a list of cars retrieved from the PostgreSQL database. The app will automatically query the `cars` table and show the vehicle information.


### Notes

- Make sure to adjust your Flask application's database connection settings to match the containerized PostgreSQL database's hostname and port.
- Ensure the `init.sql` script is executed when the PostgreSQL container starts to initialize the database and populate it with data.

This project is a simple introduction to containerization with Docker, and it demonstrates how to set up a web application and a database service in isolated environments.
