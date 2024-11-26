import streamlit as st

# Embed custom CSS for the card layout
st.markdown(
    """
    <style>
        .card {
            background: #ffffff;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }
        .card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .card-content {
            padding: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
 

# Create a card with the event image and content
st.markdown('<div class="card">', unsafe_allow_html=True)

# Event Image
st.image("./Image/eventPhoto.jpeg", width=700,use_column_width=False)

# Card Content (Registration Form)
with st.form("registration_form"):
    st.markdown('<div class="card-content">', unsafe_allow_html=True)
    st.title("Registration Page")

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
