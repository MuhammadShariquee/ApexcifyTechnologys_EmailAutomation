import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your email and app password
sender_email = "shariqmini292@gmail.com"
sender_password = "tzqs msle htgk zsuq"

# List of recipients
recipients = [
    "alikhan01@gmail.com",
    "ayeshamalik92@gmail.com",
    "bilalsheikh07@gmail.com",
    "fatimasiddiqui85@gmail.com",
    "hassanqureshi33@gmail.com",
    "sanamirza14@gmail.com",
    "zeeshanabbasi09@gmail.com",
    "nidajatoi56@gmail.com",
    "owaisbaloch88@gmail.com",
    "kiranmemon22@gmail.com",
    "irfanpathan77@gmail.com",
    "maryamawan03@gmail.com",
    "tariqbutt40@gmail.com",
    "sajidgill18@gmail.com",
    "mahnoorbhatti26@gmail.com",
    "razasangi11@gmail.com",
    "humatunio50@gmail.com",
    "waseemshah08@gmail.com",
    "ridachohan29@gmail.com",
    "usmanhashmi45@gmail.com",
    "kashiflaghari12@gmail.com",
    "aminasoomro20@gmail.com",
    "naveedarain34@gmail.com",
    "sobiarajput06@gmail.com",
    "zainabniazi72@gmail.com",
    "adnanansari99@gmail.com",
    "hinakhokhar58@gmail.com",
    "imrantunio31@gmail.com",
    "mahwisharain47@gmail.com",
    "shariqshaikh292@gmail.com"
]

# Subject and body
subject = "Test Email Automation Project"
body = """
<p>Dear Recipient,</p>

<p>I hope this message finds you well.<br>
This email is part of my internship project on <b>Email Automation using Python</b>.<br>
I am currently testing my program that sends a single message to multiple recipients automatically.</p>

<p><i>Please excuse any inconvenience caused by receiving this test email.</i><br>
No action is required from your side — this is only for demonstration and learning purposes.</p>

<p>Thank you for your understanding and support.</p>

<p>Best regards,<br>
<b>Muhammad Sharique</b><br>
Intern, Python Programming</p>
"""

try:
    # Connect to Gmail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send email to each recipient individually
    for recipient in recipients:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient
        message["Subject"] = subject
        message.attach(MIMEText(body, "html"))

        server.sendmail(sender_email, recipient, message.as_string())
        print(f"✅ Email sent to {recipient}")
    print("🎉 All emails sent successfully!")        


except Exception as e:
    print("❌ Email failed to send!")
    print("Error details:", str(e))

finally:
    server.quit()
