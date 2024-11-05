import streamlit as st
import qrcode
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from io import BytesIO
import random
import os

# Load email configuration from environment variables
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "jisthottam@gmail.com"
EMAIL_PASSWORD = "weac teal rdhv hpxk"

# Check if email credentials are set
if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    st.error("Email credentials are not set. Please set EMAIL_ADDRESS and EMAIL_PASSWORD as environment variables.")
else:
    # Title for the registration page
    st.title("Registration Page")

    # Form for user registration
    with st.form("registration_form"):
        # Mandatory fields
        name = st.text_input("Name", max_chars=50)
        mobile = st.text_input("Mobile Number", max_chars=10)
        email = st.text_input("Email")
        emirates = st.selectbox("Select Emirate", 
                                ["", "Abu Dhabi", "Dubai", "Sharjah", "Ajman", "Ras Al Khaimah", "Fujairah", "Umm Al Quwain"])
        
        # Submit button
        submit_button = st.form_submit_button("Register")
        
        if submit_button:
            if not name or not mobile or not email or emirates == "":
                st.error("Please fill in all fields.")
            else:
                # Generate a unique registration number
                registration_number = f"REG-{random.randint(1000, 9999)}"
                
                # Generate QR Code with registration details
                qr_data = f"Registration Number: {registration_number}\nName: {name}\nMobile: {mobile}\nEmirate: {emirates}"
                qr = qrcode.make(qr_data)
                buffered = BytesIO()
                qr.save(buffered, format="PNG")
                qr_image = buffered.getvalue()

                # Send email with registration details and QR code
                try:
                    # Setup the email content
                    msg = MIMEMultipart()
                    msg['From'] = EMAIL_ADDRESS
                    msg['To'] = email
                    msg['Subject'] = "Registration Confirmation"
                    
                    # Email body
                    body = f"""<h2>Registration Confirmation</h2>
                               <p>Thank you, {name}, for registering.</p>
                               <p>Your Registration Number is: <strong>{registration_number}</strong></p>"""
                    msg.attach(MIMEText(body, 'html'))

                    # Attach QR Code image
                    image = MIMEImage(qr_image)
                    image.add_header('Content-ID', '<qrcode>')
                    msg.attach(image)

                    # Connect to the SMTP server and send email
                    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                        server.starttls()  # Enable TLS encryption
                        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                        server.send_message(msg)
                    
                    st.success("Registration successful! A confirmation email has been sent.")
                
                except Exception as e:
                    st.error(f"Failed to send email: {e}")
