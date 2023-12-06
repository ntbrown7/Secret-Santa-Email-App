import tkinter as tk
import random
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, assigned_person):
    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Create the email
    subject = "White Elephant Gift Exchange🎁"
    body = f"You have been assigned to give a gift to: {assigned_person}"
    message = MIMEText(body)
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()

def assign_and_notify():
    # Randomly assign people
    assignments = random.sample(email_list, len(email_list))

    # Send emails
    for i, email in enumerate(email_list):
        assigned_person = assignments[(i + 1) % len(email_list)]
        send_email(sender_email, sender_password, email, assigned_person)

    # Notify on the GUI
    info_label.config(text="Emails sent successfully!")

def add_email():
    email = email_entry.get()
    if email and email not in email_list:
        email_list.append(email)
        email_entry.delete(0, tk.END)
        info_label.config(text=f"Added {email}")
    else:
        info_label.config(text="Invalid or duplicate email")

# Tkinter setup
root = tk.Tk()
root.title("White Elephant Gift Exchange")
root.geometry("400x400")  # Set the window size to 400x400
email_list = []

# Sender's email details
sender_email = "nbvover@gmail.com"  # Replace with your email
sender_password = "mlaa tjkm bezw sghr"      # Replace with your password

info_label = tk.Label(root, text="Enter participant emails")
info_label.pack()

email_entry = tk.Entry(root)
email_entry.pack()

add_button = tk.Button(root, text="Add Email", command=add_email)
add_button.pack()

assign_button = tk.Button(root, text="Assign and Notify", command=assign_and_notify)
assign_button.pack()

root.mainloop()
