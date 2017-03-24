# Script to populate the database
# Will create some users if not existing and habits associated to the users

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
						'habito.settings')

import django
import json
django.setup()
from habito_app.models import Habit
from django.contrib.auth.models import User
from datetime import date

# Creates some users
def create_users():
	users = [
		{"username": "admin", 
		"password": "pass1234",
		"super": True
		},
		{"username": "jack", 
		"password": "pass1234",
		"super": False
		},
		{"username": "lisa", 
		"password": "pass1234",
		"super": False
		}
	]
	
	for u in users:
		add_user(u["username"], u["password"], u["super"])


# Creates some habits
def populate():
	
	habits = [
		{"title":"Take a nap",
		"description":"Some description here",
		"days":{"1":1,"2":1,"3":0,"4":1,"5":1,"6":0,"7":1,"8":1,"9":0},
		"username": "jack",
		"created": date(2017,2,24)
		},
		{"title":"Drink ginger tea every day",
		"description":"Some description here",
		"days":{"1":1,"2":1,"3":1,"4":1,"5":1,"6":1,"7":1,"8":1,"9":0, "10":1, "11":1, "12":1},
		"username": "lisa",
		"created": date(2017,3,1)
		},
		{"title":"Write code every day",
		"description":"Some description here",
		"days":{"1":1,"2":1,"3":1,"4":1,"5":1,"6":0,"7":1,"8":1,"9":0},
		"username": "lisa",
		"created": date(2017,2,28)
		}, 
		{"title":"Make a list before going shopping",
		"description":"Some description here",
		"days":{"1":1,"2":1,"3":0,"4":1},
		"username": "lisa",
		"created": date(2017,2,28)
		},
		{"title":"Stop checking your phone at dinner",
		"description":"Some description here",
		"days":{"1":1,"2":1,"3":0,"4":1,"5":1,"6":1,"7":1,
		"8":1,"9":0,"10":1,"11":1,"12":1,"13":1,"14":1,
		"15":0,"16":1,"17":1,"18":1,"19":1,"20":1,"21":0,
		"22":1,"23":1,"24":1,"24":1,"25":1,"26":0,"27":1,"28":1,
		"29":1,"30":1,"31":1,"32":0,"33":1,"34":1,"35":1,
		"36":1,"37":1,"38":0,"39":1,"40":1,"41":1,"42":1, 
		"43":1,"44":0,"45":1,"46":1,"47":1,"48":1,"49":1},
		"username": "lisa",
		"created": date(2017,2,15)
		},
		{"title":"Stop smoking",
		"description":"Some description here",
		"days":{"1":1,"2":1,"3":1,"4":1,"5":1,"6":1,"7":1,
		"8":1,"9":0,"10":1,"11":1,"12":1,"13":1,"14":1,
		"15":0,"16":1,"17":1,"18":1,"19":1},
		"username": "jack",
		"created": date(2017,3,3)
		}
		]
	
	for h in habits:
		add_habit(h)

		
# HELPER FUNCTIONS
# Adds a single user
def add_user(username, password, super):
	# Check if user already exists
	if not User.objects.filter(username=username).exists():
		user = User.objects.create_user(username, password = password)
		if super == True:
			user.is_superuser = True
		user.is_staff=True
		user.save()

# Adds a single habit	
def add_habit(habit_data):
	u = User.objects.get(username=habit_data["username"])
	h = Habit.objects.get_or_create(title=habit_data["title"], user=u)[0]
	h.description = habit_data["description"]
	h.days = json.dumps(habit_data["days"])
	h.created = habit_data["created"]
	h.save()
	return h


# Start eecution
if __name__ == '__main__':
	print("Starting Habit_O population script...")
	create_users()
	populate()