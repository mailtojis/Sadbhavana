import streamlit as st
import qrcode
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from io import BytesIO
import base64
import random
import os

# Load email configuration from environment variables
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "jisthottam@gmail.com"
EMAIL_PASSWORD = "weac teal rdhv hpxk"


# Function to convert image file to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Convert the banner image to base64
image_base64 = get_base64_image("image/S24.png")

# Embed the image in HTML
st.markdown(
    f"""
    <style>
        .side-by-side {{
            display: flex;
            align-items: center;
        }}
        .side-by-side img {{
            max-width: 50%;
            height: 20%;
        }}
        .registration-form {{
            width: 70%;
            padding: 10px;
        }}
    </style>
    <div class="side-by-side">
        <div><img src="data:image/png;base64,{image_base64}" alt="Banner"></div>
        <div class="registration-form">
    """,
    unsafe_allow_html=True
)

# Form for user registration
st.title("Registration Page")
if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    st.error("Email credentials are not set.")
else:
    with st.form("registration_form"):
        name = st.text_input("Name", max_chars=50)
        mobile = st.text_input("Mobile Number", max_chars=10)
        email = st.text_input("Email")
        emirates = st.selectbox("Select Emirate", ["", "Abu Dhabi", "Dubai", "Sharjah", "Ajman", "Ras Al Khaimah", "Fujairah", "Umm Al Quwain"])
        submit_button = st.form_submit_button("Register")
        
        if submit_button:
            if not name or not mobile or not email or emirates == "":
                st.error("Please fill in all fields.")
            else:
                registration_number = f"REG-{random.randint(1000, 9999)}"
                qr_data = f"Registration Number: {registration_number}\nName: {name}\nMobile: {mobile}\nEmirate: {emirates}"
                qr = qrcode.make(qr_data)
                buffered = BytesIO()
                qr.save(buffered, format="PNG")
                qr_image = buffered.getvalue()
                
                try:
                    msg = MIMEMultipart()
                    msg['From'] = EMAIL_ADDRESS
                    msg['To'] = email
                    msg['Subject'] = "Registration Confirmation"
                    body = f"<h2>Registration Confirmation</h2><p>Thank you, {name}, for registering.</p><p>Your Registration Number is: <strong>{registration_number}</strong></p>"
                    msg.attach(MIMEText(body, 'html'))
                    image = MIMEImage(qr_image)
                    image.add_header('Content-ID', '<qrcode>')
                    msg.attach(image)
                    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                        server.starttls()
                        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                        server.send_message(msg)
                    st.success("Registration successful! A confirmation email has been sent.")
                except Exception as e:
                    st.error(f"Failed to send email: {e}")

# Close the HTML div for the form
st.markdown("</div></div>", unsafe_allow_html=True)
