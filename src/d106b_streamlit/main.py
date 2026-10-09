import streamlit as st
import pandas as pd

import os
from dotenv import load_dotenv    #  pip install python-dotenv



st.header("Use of ENV Keys")

## ========== 1) use of .env info =============== 

# 1. Load the environment variables from the .env file
load_dotenv()

# 2. Access the variables using os.getenv()
# api_key = os.getenv("API_KEY")
tel = os.getenv("my_tel_num")

api_key = st.secrets["API_KEY"]

if api_key:
    st.write("API key is loaded.")
else: 
    st.write("API key is NOT loaded.")  



# You can also provide a default fallback value if the key doesn't exist
debug_mode = os.getenv("DEBUG", "False")  # not added to the ,env file (on purpose)

st.write("\n======== For output info: see server logs ===============\n")
# Previewing the loaded data
print(f"API Key Loaded: {api_key is not None}")
print(f"API key : {api_key}")
print(f"tel num: {tel}")
print(f"Debug Mode: {debug_mode}\n")

# ============== 2) draw a map =============
data = pd.DataFrame({
    "lat": [28.6139, 19.0760],
    "lon": [77.2090, 72.8777]
})

st.map(data)

