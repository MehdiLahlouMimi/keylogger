#importement
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



#function
def send_mail(content, adress, password, hoste, porte, Subject): 
	"""
	Simple function to send an email to yourself
	"""
	smtp = smtplib.SMTP(host = hoste, port = porte)          # creating the smtp client object
	smtp.starttls()									         #starting the client
	smtp.login(adress, password)                             #connecting to your email service

	message = MIMEMultipart()                                #creating the message to send
	message["From"] = message["To"] = adress                 
	message["Subject"] = Subject                             #Adding the necessary informations

	message.attach(MIMEText(content, "plain"))               #Attaching the text content to the message

	smtp.send_message(message)                               #And finally sending the message
	del message                                              #To avoid problems