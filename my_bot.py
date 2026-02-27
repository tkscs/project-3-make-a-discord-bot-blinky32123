from secret import my_username
import random as r
import datetime
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
def should_i_respond(user_message, user_name):
  if user_name=="muky":
    return False
  if "robot" in user_message:
    return True
  if "random number" in user_message:
    return True
  if "wake up" in user_message:
    #print("i have awakened")
    return True
  if "animal" in user_message:
    #list=["bird","dog","cat", "dolphin","lion","naked molerat", "shark"]
    #r.choice(list, k=1)
    #print(f"my favorite animal is {list}")
    return True
  if "random" in user_message:
    #list2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","q","s","t","u","v","w","y","x","z"]
    #randomization=r.choice(list2, k=20)
    #extralist=[1,2]
    #halfhalf=r.choice(extralist, k=1)
    #if halfhalf==1:
    #  upperrandom=randomization.upper()
    #  print(upperrandom)
    #if halfhalf==2:
    #  lowerrandom=randomization.lower()
    #  print(lowerrandom)
    return True
  if "country" in user_message:
    return True
  if "time" in user_message:
    return True
  # if "number game" in user_message:
    
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
    animal_list=r.choice(list, k=1)
    return f'''my favorite animal is {animal_list}
    '''
    
  if "random" in user_message:
    list2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","q","s","t","u","v","w","y","x","z"]
    randomization = r.choice(list2, k=20)
    randomization=randomization + randomization
    half=r.randint(1,2)
    if half==1:
      upperrandom=randomization.upper()
      return f'''{upperrandom}
      '''
    if half==2:
      lowerrandom=randomization.lower()
      return f'''{lowerrandom}
      '''
  if "random number" in user_message:
    return f'''{r.randint(0,101)}
    '''
  if "country" in user_message:
    countries=["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czechia", "DRC", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", 
               "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Mali", "Malta", "Mauritania", "Mauritius", "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "San Marino", "Saudi Arabia", "Senegal", "Serbia", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Tunisia", "Turkey", "Turkmenistan", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe",]
    countrys=r.choice(countries, k=1)
    return f'''{countrys}
    '''
  if "time" in user_message:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f'''{current_time}       
    ''' 
  # if "number game" in user_message:
    
  else:
    return False




# listt=["1","2","3","4","5","6","7","8","9","10"]
# x=r.choice(listt, k=1)
#  #guess wip
# x=7 #(1-10)
# min_y = 1
# max_y = 10
# print( min_y, " ", max_y)
# y=r.randint(min_y,max_y)
# print(y)
# guess = 1

# while (y != x) : 
#     z=input(f"my number is:")
#     if z=="higher":
#         min_y = y
#     elif z=="lower":
#         max_y = y

#     print( min_y, " ", max_y)
#     y=r.randint(min_y,max_y)
#     print(y)
#     guess = guess + 1

# if (y == x):
#     print("I won in", guess, "guesses")  