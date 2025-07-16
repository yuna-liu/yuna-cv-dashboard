from neo4j import GraphDatabase
import streamlit as st

# Load credentials
NEO4J_URI = st.secrets["neo4j"]["NEO4J_URI"]
NEO4J_USER = st.secrets["neo4j"]["NEO4J_USER"]
NEO4J_PASSWORD = st.secrets["neo4j"]["NEO4J_PASSWORD"]

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))


def insert_cv_data(tx):
    tx.run("""
    // Create Person node
    MERGE (y:Yuna {name: 'Yuna'})

    // Projects/Companies
    MERGE (salesTeam:Project {name: 'VCC Sales Team'})
    MERGE (volvoCell:Company {name: 'VCC Cell Team'})
    MERGE (bank:Company {name: 'Collector Bank'})
    MERGE (capgemini:Company {name: 'Capgemini'})

    // Employment relationships
    MERGE (y)-[:WORKS_AT]->(volvoCell)
    MERGE (y)-[:WORKS_AT]->(bank)
    MERGE (y)-[:WORKS_AT]->(capgemini)

    // Consulting relationship
    MERGE (capgemini)-[:CONSULT_AT]->(salesTeam)

    // Roles at VCC Sales Team
    MERGE (deDataEng:Role {name: 'DE'})
    MERGE (genAI:Role {name: 'GenAI Dev'})
    MERGE (salesTeam)-[:HAS_ROLE]->(deDataEng)
    MERGE (salesTeam)-[:HAS_ROLE]->(genAI)

    // Common Skill Nodes
    MERGE (snowflake:Skill {name: 'Snowflake'})
    MERGE (azure:Skill {name: 'Azure'})
    MERGE (matillion:Skill {name: 'Matillion'})
    MERGE (sql:Skill {name: 'SQL'})
    MERGE (powerBI:Skill {name: 'Power BI'})
    MERGE (airflow:Skill {name: 'Airflow'})
    MERGE (kubernetes:Skill {name: 'Kubernetes'})
    MERGE (dataArchitecture:Skill {name: 'Data Architecture'})
    MERGE (aiChatbot:Skill {name: 'AI Chatbot'})
    MERGE (streamlit:Skill {name: 'Streamlit'})
    MERGE (databricks:Skill {name: 'Databricks'})
    MERGE (powerAutomate:Skill {name: 'Power Automate'})
    MERGE (tableau:Skill {name: 'Tableau'})
    MERGE (python:Skill {name: 'Python'})
    MERGE (pyspark:Skill {name: 'PySpark'})
    MERGE (pandas:Skill {name: 'Pandas'})
    MERGE (matplotlib:Skill {name: 'Matplotlib'})
    MERGE (xgboost:Skill {name: 'XGBoost'})
    MERGE (scikitlearn:Skill {name: 'Scikit-learn'})
    MERGE (tensorflow:Skill {name: 'TensorFlow'})
    MERGE (pytorch:Skill {name: 'PyTorch'})

    // Skills for DE role
    MERGE (deDataEng)-[:USES_SKILL]->(snowflake)
    MERGE (deDataEng)-[:USES_SKILL]->(azure)
    MERGE (deDataEng)-[:USES_SKILL]->(matillion)
    MERGE (deDataEng)-[:USES_SKILL]->(sql)
    MERGE (deDataEng)-[:USES_SKILL]->(powerBI)
    MERGE (deDataEng)-[:USES_SKILL]->(airflow)
    MERGE (deDataEng)-[:USES_SKILL]->(kubernetes)
    MERGE (deDataEng)-[:USES_SKILL]->(dataArchitecture)

    // Skills for GenAI Dev role
    MERGE (genAI)-[:USES_SKILL]->(aiChatbot)
    MERGE (genAI)-[:USES_SKILL]->(streamlit)
    MERGE (genAI)-[:USES_SKILL]->(snowflake)
    MERGE (genAI)-[:USES_SKILL]->(databricks)

    // Roles at VCC Cell Team
    MERGE (volvoCellDE:Role {name: 'DE Intern'})
    MERGE (volvoCellDA:Role {name: 'DA Intern'})
    MERGE (volvoCellDS:Role {name: 'DS Intern'})
    MERGE (volvoCell)-[:HAS_ROLE]->(volvoCellDE)
    MERGE (volvoCell)-[:HAS_ROLE]->(volvoCellDA)
    MERGE (volvoCell)-[:HAS_ROLE]->(volvoCellDS)

    // Skills for VCC Cell roles
    MERGE (volvoCellDE)-[:USES_SKILL]->(azure)
    MERGE (volvoCellDE)-[:USES_SKILL]->(powerAutomate)

    MERGE (volvoCellDA)-[:USES_SKILL]->(powerBI)
    MERGE (volvoCellDA)-[:USES_SKILL]->(tableau)

    MERGE (volvoCellDS)-[:USES_SKILL]->(python)
    MERGE (volvoCellDS)-[:USES_SKILL]->(xgboost)
    MERGE (volvoCellDS)-[:USES_SKILL]->(scikitlearn)
    MERGE (volvoCellDS)-[:USES_SKILL]->(tensorflow)
    MERGE (volvoCellDS)-[:USES_SKILL]->(pytorch)

    // Role at Collector Bank
    MERGE (bankDS:Role {name: 'DS Intern'})
    MERGE (bank)-[:HAS_ROLE]->(bankDS)

    // Skills for Collector Bank role
    MERGE (bankDS)-[:USES_SKILL]->(databricks)
    MERGE (bankDS)-[:USES_SKILL]->(pyspark)
    MERGE (bankDS)-[:USES_SKILL]->(python)
    MERGE (bankDS)-[:USES_SKILL]->(pandas)
    MERGE (bankDS)-[:USES_SKILL]->(matplotlib)
    MERGE (bankDS)-[:USES_SKILL]->(xgboost)
    MERGE (bankDS)-[:USES_SKILL]->(scikitlearn)
    MERGE (bankDS)-[:USES_SKILL]->(tensorflow)
    MERGE (bankDS)-[:USES_SKILL]->(pytorch)
    """)



with driver.session() as session:
    session.write_transaction(insert_cv_data)
    print("✅ CV data inserted into Neo4j!")

driver.close()


