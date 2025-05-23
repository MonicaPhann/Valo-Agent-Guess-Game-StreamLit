import random
import streamlit as st
import pandas as pd

# Title
st.title('Valorant Agent Guess Game')

# Load CSV Data
data = pd.read_csv("/Users/monic/Documents/GitHub/Valo-Agent-Guess-Game-StreamLit/champs.csv")

st.subheader("Guess the Valorant Agent!")
st.write("You have 2 hints to guess the agent. Type your guess in the input box below.")
st.write("You have 3 attempts to guess the agent correctly.")
st.write("Good luck!")
st.divider()

# Convert columns to lists
nameList = data["Name"].tolist()
roleList = data["Role"].tolist()
countryList = data["Origin"].tolist()

# Initialize session state
if "started" not in st.session_state:
    st.session_state.started = False
if "attempt" not in st.session_state:
    st.session_state.attempt = 0
if "randInt" not in st.session_state:
    st.session_state.randInt = 0
if "agent" not in st.session_state:
    st.session_state.agent = ""

# Hint system
def hint(tries):
    if tries == 0:
        st.info(f"Hint!!!! Role is: {roleList[st.session_state.randInt]}")
    elif tries == 1:
        st.info(f"Hint!!!! From: {countryList[st.session_state.randInt]}")

# Start game button
button_text = "🎮 Start Game!" if not st.session_state.started else "🔄 Restart Game"

if st.button(button_text):
    st.session_state.randInt = random.randrange(len(nameList))
    st.session_state.agent = nameList[st.session_state.randInt]
    st.session_state.started = True
    st.session_state.attempt = 0
    st.success("Game started! Use the input below to guess.")

# Game Logic
if st.session_state.started:
    user = st.chat_input("Guess the Agent:")

    if user:
        name = str(user).strip().lower().capitalize()
        agent = st.session_state.agent

        if name == agent:
            st.success(f"🎉 Correct! The agent was: {agent}")
            st.session_state.started = False  # End the game
        elif name in nameList:
            st.warning("❌ Wrong! Try again.")
            hint(st.session_state.attempt)
            st.session_state.attempt += 1
        else:
            st.error("⚠️ That’s not a valid agent name. Try again.")

        if st.session_state.attempt > 2:
            st.error(f"❌ You've used all your hints! The agent was: {agent}")
            st.session_state.started = False  # End the game
