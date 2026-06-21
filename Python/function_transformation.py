def clean_and_split_email(email):
    cl_email = email.strip().lower()
    #sara@gmail.com
    username, domain = cl_email.split("@")
    return {"username":username,
            "domain:":domain}
    
print(clean_and_split_email("    saRa@gMAil.com   "))

