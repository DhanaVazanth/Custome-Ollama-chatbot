import streamlit as st
import json
import requests
import subprocess
import os
import sqlite3


# Function to initialize the database
def init_db():
    conn = sqlite3.connect("avatars.db")
    cursor = conn.cursor()
   
    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS avatars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            avatar_name TEXT UNIQUE,
            system_prompt TEXT,
            temperature REAL
        )
    """)
   
    conn.commit()
    conn.close()


# Function to save avatar to the database
def save_avatar(avatar_name, system_prompt, temperature):
    conn = sqlite3.connect("avatars.db")
    cursor = conn.cursor()


    try:
        cursor.execute("INSERT INTO avatars (avatar_name, system_prompt, temperature) VALUES (?, ?, ?)",
                       (avatar_name, system_prompt, temperature))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Avatar '{avatar_name}' already exists in the database.")


    conn.close()


# Function to retrieve all avatars
def get_all_avatars():
    conn = sqlite3.connect("avatars.db")
    cursor = conn.cursor()
    cursor.execute("SELECT avatar_name FROM avatars")
    avatars = [row[0] for row in cursor.fetchall()]
    conn.close()
    return avatars




def stream_api_response(url, data):
    """
    Streams the response from an API endpoint and displays it in Streamlit.
    """
    response = requests.post(url, json=data, stream=True)


    if response.status_code == 200:
        placeholder = st.empty()
        full_response = ""


        for line in response.iter_lines(decode_unicode=True):
            if line:
                try:
                    chunk = json.loads(line)
                    response_part = chunk.get("response", "")
                    full_response += response_part
                    placeholder.markdown(full_response)


                except json.JSONDecodeError:
                    st.error("Failed to decode response as JSON.")
        placeholder.markdown(full_response)  # Ensure the last bit is shown.
    else:
        st.error(f"API request failed with status code: {response.status_code}")


def get_user_input():
    """Collect user input from the Streamlit sidebar."""
    with st.sidebar:
        Avatar_name = st.text_input("Enter Avatar Name:").replace(" ","")


        system_prompt = st.text_area(f"Enter your :green[{Avatar_name}]'s Role Play:") if Avatar_name else ""
        temperature = st.slider("Select Temperature:", 0.0, 1.0, step=0.1)
       
        create_button = st.button("Create..🦾")


        return Avatar_name, system_prompt, temperature, create_button


def create_model_file(Avatar_name, system_prompt, temperature):
    """Generate and save the model file."""
    if not Avatar_name or not system_prompt:
        st.error("Please enter both Avatar Name and Role Play description!")
        return None


    model_file_path = os.path.join(os.getcwd(), "modelfile2")


    model_file_content = f"""
FROM llama3.1:latest


PARAMETER temperature {temperature}


SYSTEM \"\"\"Your name is {Avatar_name} and {system_prompt}\"\"\"
"""


    try:
        with open(model_file_path, "w") as f:
            f.write(model_file_content)
        return model_file_path
    except Exception as e:
        st.error(f"Error while saving model file: {e}")
        return None


def create_ai_model(Avatar_name, model_file_path):
    """Run the command to create the AI model using Ollama."""
    if not model_file_path:
        return


    create_string = f"ollama create {Avatar_name} -f \"{model_file_path}\""


    try:
        subprocess.run(create_string, check=True, shell=True)
        st.toast(f"Your :green[{Avatar_name}] AI has been created successfully!", icon='🪄')
    except FileNotFoundError:
        st.toast("oLlama command not found. Make sure Ollama is installed and added to PATH.")
    except subprocess.CalledProcessError as e:
        st.toast(f"Error in executing command: {e}")


def run_ai_model(Avatar_name):
    """Run the AI model using Ollama."""
    if not Avatar_name:
        st.error("Please provide an Avatar Name before running the model!")
        return


    run_command = f"ollama run {Avatar_name}"


    try:
        subprocess.Popen(run_command, shell=True)  # Run model in background
    except FileNotFoundError:
        st.error("oLlama command not found. Make sure Ollama is installed and added to PATH.")
    except subprocess.CalledProcessError as e:
        st.error(f"Error in running model: {e}")