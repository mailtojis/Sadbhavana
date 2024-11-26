import streamlit as st

# Embed custom CSS to hide the footer and red Streamlit icon
st.markdown(
    """
    <style>
        /* Hide the Streamlit footer (red icon) */
        .css-1pbnwmo {
            display: none;
        }
        
        /* Set background color and padding for the entire app */
        .stApp {
            background-color: #E6F7FF;  /* Light blue background */
            padding-top: 20px;  /* Add some space from the top */
        }

        /* Image styling for the event image */
        .event-image {
            width: 100%;
            max-height: 400px;
            object-fit: cover;
        }

        /* Custom styling for the registration form */
        .registration-form {
            background: rgba(255, 255, 255, 0.9); /* Semi-transparent white background */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;  /* Space between image and form */
        }

        /* Style for the form fields and text */
        .form-title {
            color: #004C99;  /* Blue color for title */
            font-size: 26px;
            font-weight: bold;
        }

        .form-label {
            font-weight: bold;
            color: #004C99;  /* Matching color for labels */
        }

        .form-submit {
            background-color: #004C99;
            color: white;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the event image at the top

st.markdown('<h2 class="form-title">  Register Below to get your Free Entry Pass</h2>', unsafe_allow_html=True)
st.image("./Image/eventPhoto.jpeg", use_column_width=True, output_format="JPEG")

# Registration form section
with st.form("registration_form"): 
    
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

    submit_button = st.form_submit_button("Register", use_container_width=True)
    
    if submit_button:
        if not name or not mobile or not email or emirates == "":
            st.error("Please fill in all fields.")
        elif len(mobile) != 10 or not mobile.isdigit():
            st.error("Mobile number should be exactly 10 digits.")
        else:
            st.success("Registration successful!")
    
    st.markdown('</div>', unsafe_allow_html=True)
