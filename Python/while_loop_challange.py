# Initialize attempt counter
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    answer = input("Do you agree? (yes/no): ").lower()
    if answer == "yes":
        print("Glad we are on the same page")
        break
    else:
        attempts += 1
        if attempts == max_attempts:
            print("3 Strikes, You are Out!")
