def write_log(message):
    with open(r"c:\Main\Python\app.txt", "a") as file:
        file.write(message + "\n")



write_log("App Started")
write_log("user logged in ")
write_log("App Stopped")