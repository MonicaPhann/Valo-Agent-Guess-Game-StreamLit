import random
import streamlit as st
import pandas as pd

st.title('Valorant Agent Guess Game')
data = pd.read_csv("/Users/monic/Documents/GitHub/Valo-Agent-Guess-Game-StreamLit/champs.csv")

#Length of csv file
rowSize = len(data)

#Csv Files
with st.expander("See Agent CSV File"):
    i = 0
    while i < rowSize:
        names = data.loc[i]
        st.write(names)
        i += 1
        
with st.expander("Full CSV File"):
    st.write(data)

st.divider()

#Turning each column into a list
nameList = data["Name"].tolist()
roleList = data["Role"].tolist()
countryList = data["Origin"].tolist()

#names = data.loc[1]
#st.write(names)

#st.write(rowSize)

start = st.button("Press here to Start!")

def hint (tries):
    if tries == 0:
        st.write("Hint!!!! Role is:",roleList[randInt],"\n")
    elif tries == 1:
        st.write("Hint!!!! From:",countryList[randInt],"\n")

randInt = random.randrange(0,len(nameList))
agent = nameList[randInt]

started = False

if start == True:
    started = True
    attempt = 0

    #User input
    user = st.chat_input("Guess the Agent: ",key="Input")

    #User input default to lower and capitalized
    name = str(user).lower().capitalize()


if started:
            
    if name == agent:
        st.write("You have guessed the correct agent! The agent was:", agent)
        started == False

    elif name != agent and name in nameList:
        st.write("Wrong! Try again.")
        hint(attempt)
        attempt = attempt + 1
            
    elif name not in nameList:
        st.write("\nUh oh! This is not an agent name. Try again!")