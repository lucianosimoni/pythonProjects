import email, getpass, imaplib
from email.header import decode_header

#Credentials
username = input("Your Gmail here --> ")
password = getpass.getpass("Your password --> ")

numEmails = int(input("How many top emails do you want to scan? --> "))

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")
print(imap.login(username, password)) # authenticate

def ifoodCodigo(numDeEmails):
    subject = fetchEmails(numDeEmails)
    codigo = "" 
    
    for char in subject:
        if char.isnumeric():
            codigo += str(char)
    
    if len(codigo) == 6:
        return(int(codigo)) #Transforms it to integer before returning


status, messages = imap.select("INBOX")
messages = int(messages[0]) #total number of emails

def fetchEmails(numToFetch):
    #numToFetch = number of top emails to fetch

    for i in range(messages, messages-numToFetch, -1): #Loop through the first 2
        res, msg = imap.fetch(str(i), "(RFC822)") # fetch the email message by ID
        
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                
                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding) # if it's a bytes, decode to str
                
                return(subject)
                
    # close the connection and logout
    imap.close()
    imap.logout()