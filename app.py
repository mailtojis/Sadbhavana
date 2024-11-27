import streamlit as st
import qrcode
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from io import BytesIO
import random
import re

# Load email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "jisthottam@gmail.com"
EMAIL_PASSWORD = "weac teal rdhv hpxk"

# Embed custom CSS
st.markdown(
    """
    <style>
        .css-1pbnwmo {
            display: none;
        }
        .stApp {
            background-color: #E6F7FF;
            padding-top: 20px;
        }
        .event-image {
            width: 100%;
            max-height: 400px;
            object-fit: cover;
        }
        .registration-form {
            background: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }
        .form-title {
            color: #004C99;
            font-size: 26px;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display event image and title
st.markdown('<h2 class="form-title">Register Below to get your Free Entry Pass</h2>', unsafe_allow_html=True)
st.image("./Image/eventPhoto.jpeg", use_column_width=True, output_format="JPEG")

# Registration form
with st.form("registration_form"):
    name = st.text_input("Full Name", max_chars=50)
    mobile = st.text_input("Mobile Number", max_chars=10)
    email = st.text_input("Email")
    emirates = st.selectbox("Select Emirate", ["", "Abu Dhabi", "Dubai", "Sharjah", "Ajman", "Ras Al Khaimah", "Fujairah", "Umm Al Quwain"])

    col1_inner, col2_inner = st.columns(2)
    with col1_inner:
        adults = st.number_input("Number of Adults", min_value=0, max_value=10, value=0, step=1)
    with col2_inner:
        kids = st.number_input("Number of Kids", min_value=0, max_value=10, value=0, step=1)

    submit_button = st.form_submit_button("Register", use_container_width=True)

    # Validation and email handling
    if submit_button:
        def is_valid_email(email):
            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            return re.match(email_regex, email)

        def is_valid_mobile(mobile):
            return len(mobile) == 10 and mobile.isdigit()

        if not name or not mobile or not email or emirates == "":
            st.error("Please fill in all fields.")
        elif not is_valid_email(email):
            st.error("Please enter a valid email address.")
        elif not is_valid_mobile(mobile):
            st.error("Mobile number should be exactly 10 digits.")
        else:
            registration_number = f"REG-{random.randint(1000, 9999)}"
            qr_data = f"Registration Number: {registration_number}\nName: {name}\nMobile: {mobile}\nEmirate: {emirates}\nAdults: {adults}\nKids: {kids}"
            qr = qrcode.make(qr_data)
            buffered = BytesIO()
            qr.save(buffered, format="PNG")
            qr_image = buffered.getvalue()

            try:
                msg = MIMEMultipart()
                msg["From"] = EMAIL_ADDRESS
                msg["To"] = email
                msg["Subject"] = "Registration Confirmation"
                body = (
                    f"<h2>Registration Confirmation</h2>"
                    f"<p>Thank you, {name}, for registering.</p>"
                    f"<p>Your Registration Number is: <strong>{registration_number}</strong></p>"
                )
                msg.attach(MIMEText(body, "html"))
                image = MIMEImage(qr_image)
                image.add_header("Content-ID", "<qrcode>")
                msg.attach(image)

                with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                    server.starttls()
                    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    server.send_message(msg)

                st.success("Registration successful! A confirmation email has been sent.")
            except Exception as e:
                st.error(f"Failed to send email: {e}")
