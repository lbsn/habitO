from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import date
import json

# Habit model
class Habit(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=128)
	description = models.TextField()
	created = models.DateField(default=date.today)
	days = models.TextField(max_length=128, default={})
	achv_default = {'1':0,'2':0,'3':0, '4':0}
	achievements = models.TextField(max_length=128, default=json.dumps(achv_default))
	slug = models.SlugField()	
	
	# Sets as unique the combination title + user 
	# (a user cannot create two habits with the same title)
	class Meta:
		unique_together = ('user', 'title')
		
	# Returns days as a dictionary.
	# A dictionary cannot be directly stored in the database, 
	# so the value of days field must be parsed to a json object in order to be used
	def getDays(self):
		return json.loads(self.days)
	
	# Gets the index of today's value in the days field dict
	def getTodayIndex(self):
		days = json.loads(self.days)
		start_date = self.created
		now_date = date.today()
		diff_days = (now_date - start_date)
		index = diff_days.days + 1 
		# Maximum number of days is 49
		if index > 49:
			index = 49
		return index
		
	# Checks days starting from creation date until now
	# and sets empty days to 0
	def checkDays(self):
		days = self.getDays()
		today_index = self.getTodayIndex()
		for d in range(1, today_index + 1):
			if str(d) not in days:
				days[str(d)] = 0
		self.days = json.dumps(days)
		self.save()
	
	# Checks if habit is completed (last index in days should be 49)
	def checkCompleted(self):
		last_index = self.getTodayIndex()
		if last_index == 49:
			return True
		return False
		
	# Returns achievements as a dictionary
	def getAchievements(self):
		return json.loads(self.achievements)
	
	# Checks achievements and updates the field
	def checkAchievements(self):
		achv = self.getAchievements()
		days = self.getDays()
		goals = {
			5:1,
			10:2,
			15:3
			}
		count = 0
		# Checks goals by counting sequences of values = 1
		for i in range(1, len(days) + 1):
			if days[str(i)] == 1:
				count = count + 1
				if count in goals:
					achv[str(goals[count])] = 1
			else:
				count = 0
		# Checks completed
		if self.checkCompleted():
			achv['4'] = 1
		self.achievements = json.dumps(achv)
		self.save()
		
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Habit, self).save(*args, **kwargs)
		
	def __str__(self):
		return self.title
	
	def __unicode__(self):
		return self.title

