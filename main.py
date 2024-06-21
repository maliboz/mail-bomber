import smtplib
from email.mime.text import MIMEText

# Email information
sender_email = "your_email@gmail.com"
sender_password = "your_app_specific_password"
recipient_email = "target_email@gmail.com"
subject = "Test Email"  # Ensure the subject is meaningful to avoid spam filters
body = "This is a test email."

# SMTP server and port
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Create the email message
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recipient_email

# Connect to the SMTP server and send emails
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    
    for i in range(100):  # Send 100 emails
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"{i+1}. email sent successfully")
    
    server.quit()
    print("All emails sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")
