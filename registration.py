import streamlit as st

# Embed custom CSS to style the page and form
st.markdown(
    """
    <style>
        /* Set background color for the entire page */
        .stApp {
            background-color: #F6F4E8;  /* Light blue background color */
        }

        /* Style for the card */
        .card {
            background: #ffffff;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            margin-top: 50px; /* Add margin to separate card from top */
            padding: 20px; /* Optional, to create some space around the card */
        }

        /* Event image in the card */
        .card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }

        /* Content inside the card */
        .card-content {
            padding: 20px;
        }

        /* Custom style for form labels to make them bold and change color */
        .stTextInput label,
        .stNumberInput label,
        .stSelectbox label {
            font-weight: bold;
            color: #006064;  /* Dark blue color for the labels */
        }

        /* Style for the form inputs */
        .stTextInput, .stNumberInput, .stSelectbox {
            margin-top: 10px;
            border: 1px solid #006064;  /* Dark blue border color */
            padding: 5px;
            border-radius: 5px;
        }

        /* Submit button */
        .stButton button {
            background-color: #00838f;  /* Dark cyan background for the button */
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 5px;
        }

        /* Optional: Style for error or success messages */
        .stError, .stSuccess {
            font-weight: bold;
            color: #d32f2f;  /* Red color for error messages */
        }

        /* Custom Title Style */
        .custom-title {
            font-size: 24px;
            font-weight: bold;
            color: #00796b;  /* Change to your desired color */
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Custom Title with smaller size and different color
st.markdown('<h3 class="custom-title">Register Below to Get Your Free Entry Pass</h3>', unsafe_allow_html=True)
 

# Event Image
st.image("./Image/eventPhoto.jpeg", width=700, use_column_width=False)

# Card Content (Registration Form)
with st.form("registration_form"):
    st.markdown('<div class="card-content">', unsafe_allow_html=True)
    
    # Form fields
    name = st.text_input("Full Name", max_chars=50)
    mobile = st.text_input("Mobile Number", max_chars=10)
    email = st.text_input("Email")
    emirates = st.selectbox("Select Emirate", ["", "Abu Dhabi", "Dubai", "Sharjah", "Ajman", "Ras Al Khaimah", "Fujairah", "Umm Al Quwain"])

    # Number of adults and kids fields in a single row
    col1_inner, col2_inner = st.columns(2)
    with col1_inner:
        adults = st.number_input("Number of Adults", min_value=0, max_value=10, value=0, step=1)
    with col2_inner:
        kids = st.number_input("Number of Kids", min_value=0, max_value=10, value=0, step=1)

    submit_button = st.form_submit_button("Register")
    
    if submit_button:
        if not name or not mobile or not email or emirates == "":
            st.error("Please fill in all fields.")
        elif not is_valid_email(email):
            st.error("Please enter a valid email address.")
        elif not is_valid_mobile(mobile):
            st.error("Mobile number should be exactly 10 digits.")
        else:
            st.success("Registration successful!")
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
