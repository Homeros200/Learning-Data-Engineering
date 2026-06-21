def write_log(message):
    with open(r"c:\Main\Python\app.txt", "a") as file:
        file.write(message + "\n")

#Validation Function
def is_valid_email(email):
    return "@" in email and "." in email

#Transformation Function
def clean_and_split_email(email):
    # Task : clean an email and split it into username and domain
    email = email.strip().lower()
    username, domain= email.split("@")
    return {
        "username": username,
        "domain": domain
    }
#Orchestrator Function
def process_user_email(email):
    write_log("App Started")

    #we must check if it is valid
    if not is_valid_email(email):
        write_log(f"Invalid Email received: {email}")
    #if it is not valid, we log the problem
    else:
        clean_email = clean_and_split_email(email)
        write_log(f"Processed Email:{clean_email}")
    write_log("App Stopped")
    
#And we log what happened

#We receive an email from a user 
email = input("Please enter Your Email:")
process_user_email(email)


