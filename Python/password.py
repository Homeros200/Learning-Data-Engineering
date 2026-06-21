

email = "George.gomer@gmail.com"
password = input("აქ შეიყვანეთ თქვენი პაროლი:")
valid =  True
if password == "" :
    print("პაროლის ველი ვერ იქნება ცარიელი:")
    valid = False 
if len(password) < 8 :
    print("უნდა შეადგენდეს მინიმუმ 8 სიმბოლოს.")
    valid = False 
if  password.isupper() or password.isdigit() :
    print("უნდა შეიცავდეს მინიმუმ 1 დაბალ ასობგერას.")
    valid = False 
if password.islower() or password.isdigit()  :  
    print("უნდა შეიცავდეს მინიმუმ 1 მაღალ ასობგერას.") 
    valid = False 
if email == password:
    print("არ უნდა იყოს იგივე ნაირი როგორიცაა იმაილი")
    valid = False 

if " " in password :
    print("არ უნდა შეიცავდეს პრაბლეს.")
    valid = False 
if not password[0].isalnum() or not password[-1].isalnum() :
    print("უნდა იწყებოდეს ასობგერით ან ციფრით.")
    valid = False 
if valid :
    print("პაროლი მიღებულია.")


#Password = 12345678aA