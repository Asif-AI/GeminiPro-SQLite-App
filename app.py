from dotenv import load_dotenv
load_dotenv()  #load all the variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
#configure API key.
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load google gemini Model and provirde SQL query as a response.
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0], question])
    return response.text

#Function to retrive query from SQL databases
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur=conn.cursor()

    cur.execute(sql)
    rows= cur.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
    return rows

##Define the  prompt.
prompt ="""
You are an expert in converting English questions to SQL query!
The SQL database has the name student and has the following columns - Name, Class, Section and Marks /n/nFor example, n/Example 1 - How many enteries of records are present?,
the SQL command will be something like this SELECT * FROM STUDENT; /nExample 2 - Tell me all the students styding in Data Science Class?,
the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science";
"""

#Streamlit app

st.set_page_config (page_title= "I can retrieve any SQL query")
st.header("Gemini App to retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

#If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response, "student.db")
    st.subheader("The response is")

    for row in response:
        print(row)
        st.header(row)
