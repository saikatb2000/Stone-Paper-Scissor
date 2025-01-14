import streamlit as st
import random

st.title("Rock Paper Scissors Game")
null = "❌"
rock = "🪨"
paper = "📄"
scissor = "✂️"
game_images = [null, rock, paper, scissor]

user_choice = st.number_input("Enter a choice (nothing = 0, rock = 1, paper = 2, scissors = 3):", min_value=0, max_value=3, step=1, format="%d")

st.write("You chose:")
st.write(game_images[user_choice])

computer_choice = random.randint(0, 3)
st.write("Computer chose:")
st.write(game_images[computer_choice])

if user_choice == 1 and computer_choice == 3:
    st.write("**You win!**")
elif computer_choice == 1 and user_choice == 3:
    st.write("**You lose!**")
elif computer_choice > user_choice:
    st.write("**You lose!**")
elif computer_choice < user_choice:
    st.write("**You win!**")
elif computer_choice == 0 and user_choice == 0:
    st.write("**PLEASE ENTER A CHOICE!**")
else:
    st.write("**It's a tie!**")
