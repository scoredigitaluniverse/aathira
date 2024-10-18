from datetime import datetime
current_hour = datetime.now().hour
def greetings(request):
    if 5 <= current_hour < 12:
        greeting = "Good Morning!"
    elif 12 <= current_hour < 17:
        greeting = "Good Afternoon!"
    elif 17 <= current_hour < 21:
        greeting = "Good Evening!"
    else:
        greeting = "Good Night!"
    return {'greeting': greeting,'c_h':current_hour}
