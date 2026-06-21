gamers = []

def add_gamer(gamer, gamers_list):
    if "name" in gamer and "availability" in gamer:
        gamers_list.append(gamer)

kimberly = {"name" : "kimberly", "availability" : ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly,gamers)

add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

def build_daily_frequency_table():
    return {"Monday" : 0, "Tuesday" : 0, "Wednesday" : 0, "Thursday" : 0, "Friday" : 0, "Saturday" :0, "Sunday" : 0}

count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for a in gamers_list:
        for b in a["availability"]:
           available_frequency[b] += 1
         


calculate_availability(gamers, count_availability)



def find_best_night(availability_table):
    highest = 0
    best_day = ""
    result = ""
    for i in availability_table:
        if availability_table[i] > highest:
            highest = availability_table[i]
            best_day = i
            result = best_day
    return result



game_night = find_best_night(count_availability)


def available_on_night(gamers_list, day):
    gamers = []
    for i in gamers_list:
        if day in i['availability']:
            gamers.append(i["name"])
    return gamers
         



attending_game_night = available_on_night(gamers, game_night)



form_email = "Hello {name}, your {game} game night is scheduled for {day_of_week}."

def send_email(gamers_who_can_attend, day, game):
    for i in gamers_who_can_attend:
        print(form_email.format(name = i, game = game, day_of_week = day ))





send_email(attending_game_night, game_night,"Abruptly Goblins!" )




unable_to_attend_best_night = []

for i in gamers:
    if game_night not in i['availability']:
        unable_to_attend_best_night.append(i)













second_night_availability = build_daily_frequency_table()


calculate_availability(unable_to_attend_best_night,second_night_availability)



find_best_night(second_night_availability)



second_night = find_best_night(second_night_availability)

available_second_game_night = available_on_night(unable_to_attend_best_night, second_night)



send_email(available_second_game_night, second_night, "Abruptly Goblins!")



