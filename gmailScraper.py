import imaplib
import email
import getpass
from email.header import decode_header

#Credentials
username = input("Your gmail --> ")
password = getpass.getpass("Your password --> ")

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")
print(imap.login(username, password)) # authenticate


def fetchEmails(numToFetch):
    #numToFetch = number of top emails to fetch
    
    status, messages = imap.select("INBOX")
    messages = int(messages[0]) # total number of emails

    for i in range(messages, messages - numToFetch, -1): #Loop through the first 3
        res, msg = imap.fetch(str(i), "(RFC822)") # fetch the email message by ID
        
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                
                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding) # if it's a bytes, decode to str
                
                # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding) # if it's a bytes, decode to str
                
                print("Subject:", subject)
                print("From:", From)
                
    # close the connection and logout
    imap.close()
    imap.logout()