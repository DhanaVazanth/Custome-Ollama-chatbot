import streamlit as st
import subprocess
import os
import requests
import json
from function import *



def main():
    st.title("AI Avatar Creator")

    Avatar_name , system_prompt , temparature , create_button = get_user_input()

    if create_button:
        init_db()
        save_avatar(Avatar_name , system_prompt , temparature)

        with st.spinner("Creating Avatar..."):
            model_file_path = create_model_file(Avatar_name , system_prompt , temparature)

            if model_file_path:
                create_ai_model(Avatar_name, model_file_path)

                run_ai_model(Avatar_name)

                st.toast(f"✨ Your :green[{Avatar_name}] has been created and running successfully")


    url = "http://localhost:11434/api/generate"

    prompt = st.chat_input("Enter your prompt")

    if prompt and Avatar_name:
        data = {"model": Avatar_name, "prompt": prompt, "avatar_name": Avatar_name}

        stream_api_response(url, data)

if __name__ == "__main__":
    main()