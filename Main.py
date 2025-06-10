import streamlit as st

# Set page config
st.set_page_config(page_title="Love Percentage Calculator", layout="centered")

# Set page background color
page_bg = """
<style>
body {
    background: linear-gradient(to right, #fbd3e9, #bbd4ff);
}
.stApp {
    background: linear-gradient(to right, #fbd3e9, #bbd4ff);
    font-family: 'Arial', sans-serif;
}
.result-box {
    background-color: #ffe0ec;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    margin-top: 20px;
    box-shadow: 2px 2px 8px #ccc;
}
.result-title {
    color: #d63384;
    font-size: 28px;
    font-weight: bold;
}
.percentage {
    font-size: 36px;
    font-weight: bold;
    color: #b4005f;
    margin: 10px 0;
}
.message {
    font-size: 18px;
    color: #003366;
}
input, textarea {
    font-size: 18px;
}
.stButton > button {
    background-color: #f26b9a;
    color: white;
    font-size: 18px;
    padding: 10px 25px;
    border-radius: 10px;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# App title
st.markdown("## ❤️ Love Percentage Calculator")

# Input fields
name1 = st.text_input("Enter your name:")
name2 = st.text_input("Enter loved one's name:")
relation = st.text_input("Enter your relation (Father/Mother/Friend/sibling/couple/other/etc.):")

if st.button("Calculate ❤️") and name1 and name2 and relation: 
    # Preprocess input
    name1_clean = name1.lower().replace(" ", "")
    name2_clean = name2.lower().replace(" ", "")

    # Calculate matching and non-matching letters
    common_letters = set(name1_clean) & set(name2_clean)
    matching = sum(min(name1_clean.count(ch), name2_clean.count(ch)) for ch in common_letters)
    total_letters = len(name1_clean) + len(name2_clean)
    remaining = total_letters - 2 * matching
    
    # Handle percentage calculation
if remaining >= 10:
        # If remaining is 10 or more, take first digit and add to matching*2, then use second digit
        remaining_str = str(remaining)
        first_digit = int(remaining_str[0])
        second_digit = int(remaining_str[1]) 
        percentage = int(str(matching * 2 + first_digit) + str(second_digit)
else:
        # If remaining is less than 10, use original logic
        percentage = int(str(matching * 2) + str(remaining)) if matching * 2 + remaining > 0 else 0
    
    # Ensure percentage doesn't exceed 100%
if percentage > 100:
        percentage = 100

    # Dynamic title
title =f"love between you and your {relation.capitalize()}💖:"

    # Dynamic messag
if relation.lower() == "father":
        message = "A father's love is forever! You're deeply bonded we cannot count the unconditional love of father 🪄🤗."
elif relation.lower() == "mother":
        message = "Mother loves her child infinite, This bond is pure and strong. No one can calculate it in numbers✨💖"
elif relation.lower() == "friend":
        message = "Friendship is a gift🎁. This shows how close you are but if the number is less you can change it by putting some efforts 😊!"
elif relation.lower() in ["couple"]:
        message = "This bond is strong 🧡! Keep loving and supporting each other🙃 relations need care, respect, love and understanding keep growing in the track of this pure bond 😇🩷."
elif relation.lower() in ["siblings"]:
        message = "Siblings are fun partners of each other they just need to spend time, laugh together, play together and make things silly 😂 only this can make the siblings bond stronger 🤗."
else:
            message = "Even small love counts! Keep caring and stay connected 🫶relations only needs love, understanding, respect, care and support💪 keep nurturing your bond together 🥰." 

    # Output box
st.markdown(f"""
    <div class='result-box'>
        <div class='result-title'>{title}</div>
        <div class='percentage'>{percentage}%</div>
        <div class='message'>{message}</div>
    </div>
    """, unsafe_allow_html=True)
