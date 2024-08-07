MRP Project
This repository contains a Material Requirements Planning (MRP) system built using FastAPI and PostgreSQL. The MRP system helps manage manufacturing processes by determining the materials and components needed to produce a product, ensuring materials are available for production and products are available for delivery to customers.

Setup Instructions
Prerequisites
Python 3.6+: Ensure Python is installed on your machine.
PostgreSQL: Make sure PostgreSQL is installed and running.

Clone the repository:
sh
Copy code
git clone https://github.com/jagannadh22/MRP-Project---Term-5-ESD-SUTD.git
cd MRP-Project---Term-5-ESD-SUTD

Set Up the Virtual Environment
Create and activate a virtual environment:

sh
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the dependencies:

sh
Copy code
pip install -r requirements.txt

Set Up the PostgreSQL Database
Start PostgreSQL:

Ensure PostgreSQL is installed and running.
Create a new database:

Open the PostgreSQL command line interface (CLI) or use a database management tool like pgAdmin.
Create a new database:
sql
Copy code
CREATE DATABASE your_database_name;
Restore the database schema and data:

Using the PostgreSQL CLI, execute the schema and data SQL files:
sh
Copy code
psql -U your_username -d your_database_name -f path/to/sql/schema.sql
psql -U your_username -d your_database_name -f path/to/sql/data.sql

Configure Environment Variables
Set the DATABASE_URL environment variable:
Configure the DATABASE_URL environment variable to point to your local PostgreSQL database. You can set this variable in your operating system or within your virtual environment activation script:

sh
Copy code
export DATABASE_URL="postgresql://your_username:your_password@localhost:5432/your_database_name"  # On Windows: set DATABASE_URL=postgresql://your_username:your_password@localhost:5432/your_database_name

Modify Configuration Files

Update Database Connection Settings:
Ensure the database connection settings in database.py match your local PostgreSQL configuration:
python
Copy code
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://your_username:your_password@localhost:5432/your_database_name')

Run the Application
Start the FastAPI application:

Run the application using Uvicorn:

sh
Copy code
uvicorn main:app --reload
Access the API documentation:

Open your web browser and navigate to http://127.0.0.1:8000/docs to view and interact with the Swagger UI, which provides a graphical interface to test and interact with the API endpoints.

Usage

API Endpoints:
The project provides CRUD operations for part records, bills of materials, orders, inventory, routing, and workcenters.
You can run the MRP calculation via the /mrp/ endpoint.

Adjusting for Local Environment

Database Configuration:

Modify the database URL in your environment variables to match your local PostgreSQL setup.

Python Dependencies:

Ensure all required Python packages are installed by running pip install -r requirements.txt.
Port and Host Configuration:

If needed, adjust the Uvicorn command to run the application on a different port or host:
sh
Copy code
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Running Tests
Testing Endpoints:
Use tools like Swagger UI, curl, or Postman to manually test the API endpoints.
Optionally, write and run automated tests using pytest to ensure that all endpoints work as expected.

Troubleshooting
Common Issues:
Ensure PostgreSQL is running and accessible.
Verify that the DATABASE_URL environment variable is correctly set.
Check for any missing Python dependencies and install them using pip install -r requirements.txt.

Summary
This guide provides a step-by-step process to set up the MRP system on your local environment. By following these instructions, you can configure the PostgreSQL database, adjust the project settings for your local setup, and run the FastAPI application to manage manufacturing processes effectively.

If you have any issues or questions, please open an issue in this repository or contact the repository owner.
