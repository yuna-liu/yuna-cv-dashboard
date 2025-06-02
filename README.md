# my-cv-dashboard

Here is my cv dashboard streamlit playground

Updates on 2025-06-02

Summary Checklist for Knowledge Graph using neoj4:
Step	Status
Created Aura Free instance	🔲
Found your Bolt URI	🔲
Set your password	🔲
Inserted data with Cypher	🔲
Added connection info to Streamlit code	🔲


Details:
Step 1: Log in and create your Neo4j Aura Free instance
Go to: https://neo4j.com/cloud/aura/

Sign up or log in with your Neo4j account

Click Create Database and choose Aura Free tier

Give it a name (e.g., yuna-cv-graph) and create it

Step 2 and 3: Find your connection details (URI, username, password)
After your database is ready (this can take a couple of minutes):

Click on your database instance in the Aura dashboard

You will see Connection details:

Info	Where to find it
Bolt URL or Neo4j URI	Something like neo4j+s://<random>.databases.neo4j.io
Username	Usually neo4j (default)
Password	The password you set when creating the database

Step 4:Insert Your CV Data into Neo4j
You only need to run this once to populate the database. You can do it via python script (recommended for automation) to populate your CV graph.
You can save it as something like insert_data.py and run:

bash

python insert_data.py

