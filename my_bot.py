from secret import my_username
import random as r
import datetime

#to standardize message user_message.lower()==
#global is a function that does something?
#top function is if "" in message return true
#second function is the actual stuff if return true and print(x) -->return(x)
"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
term = 0
def should_i_respond(user_message, user_name):
  if user_name=="muky":
    return False
  # if "number" in user_message and user_name=="muky":
  #   return True
  if "robot" in user_message:
    return True
  if "number" in user_message:
    return True
  if "wake up" in user_message:
    return True
  if "animal" in user_message:
    return True
  if "random" in user_message:
    return True
  if "country" in user_message:
    return True
  if "time" in user_message:
    return True
  if "roll" in user_message: 
     return True
  if "flip" in user_message:
    return True
  if "color" in user_message:
    return True 
  if "again" in user_message:
    return True 
  if "functions" in user_message:
    return True
  else:
    return False
"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  global term
  # return f"""Hi 
  #{user_message.replace("robot", user_name)}"""

  if "robot" in user_message:
    return f"""Hi 
    {user_message.replace("robot", user_name)}"""
  if "wake up" in user_message:
    return f'''i have awakened
    '''
  if "animal" in user_message:
    list=["bird","dog","cat", "dolphin","lion","naked molerat", "shark"]
    animal_list=r.choice(list)
    return f'''my favorite animal is a {animal_list}
    '''
  if "random" in user_message:
    list2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","q","s","t","u","v","w","y","x","z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    randomization = r.choices(list2, k=20) 
    randomized=r.choice(list2)
    randomization.append(randomized)
    half=r.randint(1,2)
    if half==1:
      upperrandom=[item.upper() for item in randomization]
      uppercase = "".join(upperrandom)
      return f'''{uppercase}
      '''
    if half==2:
      lowerrandom=[item.lower() for item in randomization]
      lowercase = "".join(lowerrandom)
      return f'''{lowercase}
      '''
  if "number" in user_message:
    x=r.randint(0,101)
    if user_name=="muky":
      return f'''{r.randint(0,10)}
      '''
    else:
      return f'''{x}
    '''
  if "country" in user_message:
    countries=["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czechia", "DRC", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", 
    "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Mali", "Malta", "Mauritania", "Mauritius", "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "San Marino", "Saudi Arabia", "Senegal", "Serbia", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Tunisia", "Turkey", "Turkmenistan", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe",]
    countrys=r.choice(countries)
    return f'''{countrys}
    '''
  if "time" in user_message:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f'''{current_time}       
    ''' 
  if "roll" in user_message:
    listt=[1,2,3,4,5,6]
    term=r.choice(listt)
    return f'''you rolled a {term}
    '''
  elif "again":
    listt=[1,2,3,4,5,6]
    term2=r.choice(listt)
    term3=term2+term
    return f'''you rolled a {term2} adding up to {term3}
    '''
  if "flip" in user_message:
    coin=["Heads","Tails"]
    p=r.choice(coin)
    return f'''{p}
    '''
  if "color" in user_message:
    colors=["yellow","blue","red","green","purple","pink","black","white","orange","teal"]
    favorite_color=r.choice(colors)
    if user_name=="muky":
      favorite_color=="blue"
    return f'''my favorite color is {favorite_color}
    '''
  if "functions" in user_message:
    return f'''color, flip, roll--> again, time, country, number, random, animal, wake up, robot"
    '''
  else:
    return False