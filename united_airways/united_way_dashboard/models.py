from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Programs(models.Model):
	area = models.CharField(max_length=32)
	funds = models.CharField(max_length=32)
	focus_area = models.CharField(max_length=32)
	strategic_outcomes = models.CharField(max_length=32)
	funding_stream = models.CharField(max_length=128)
	agency_andar = models.IntegerField(default=0)
	agency_name = models.CharField(max_length=128)
	program_andar = models.IntegerField(default=0)
	program_name = models.IntegerField(default=128)
	allocation = models.IntegerField(default=0)
	grant_start_date = models.DateField()
	grant_end_date = models.DateField()
	program_description = models.IntegerField(max_length=256)
	planner = models.CharField(max_length=32)
	early_childhood = models.BinaryField()
	middle_years = models.BinaryField()
	families = models.BinaryField()
	youth = models.BinaryField()
	seniors = models.BinaryField()
	immigrants_refugees = models.BinaryField()
	women = models.BinaryField()
	aboriginal = models.BinaryField()
	other_populations = models.BinaryField()
	art_music_dance = models.BinaryField() 
	caregiver_support = models.BinaryField()
	food_provision = models.BinaryField()
	food_security = models.BinaryField()
	housing_support = models.BinaryField()
	information_and_referral = models.BinaryField()
	intergenerational = models.BinaryField()
	life_skills = models.BinaryField()
	mental_emotional_wellness = models.BinaryField()
	physical_recreational_activity = models.BinaryField()
	physical_wellness = models.BinaryField()
	policy_planning = models.BinaryField()
	research = models.BinaryField()
	education_support = models.BinaryField()
	social_connections = models.BinaryField()
	violence_prevention = models.BinaryField()
	anmore = models.BinaryField()
	belcara = models.BinaryField()
	bowen_island = models.BinaryField()
	burnaby = models.BinaryField()
	coquitlam = models.BinaryField()
	delta = models.BinaryField()
	gibsons = models.BinaryField()
	langley_city = models.BinaryField()
	langley_district = models.BinaryField()
	lions_bay = models.BinaryField()
	maple_ridge = models.BinaryField()
	new_westminster = models.BinaryField()
	north_vancouver_district = models.BinaryField()
	north_vancouver_city = models.BinaryField()
	pemberton = models.BinaryField()
	pitt_meadows = models.BinaryField()
	port_coquitlam = models.BinaryField()
	port_moody = models.BinaryField()
	richmond = models.BinaryField()
	sunshine_coast = models.BinaryField()
	surrey = models.BinaryField()
	squaish = models.BinaryField()
	vancouver = models.BinaryField()
	west_vancouver = models.BinaryField()
	whistler = models.BinaryField()
	white_rock = models.BinaryField()
	uw_speaker = models.BinaryField()
	day_of_caring = models.BinaryField()
	volunteer_ops = models.BinaryField()
	agency_tour = models.BinaryField()
	agency_fair = models.BinaryField()
	impact_story = models.BinaryField()
	other = models.BinaryField()
	total_clients = models.IntegerField(default=0)
	children_0_to_6 = models.IntegerField(default=0)
	children_6_to_12 = models.IntegerField(default=0)
	toal_children = models.IntegerField(default=0)
	seniors = models.IntegerField(default=0)
	parents_caregivers = models.IntegerField(default=0)
	families = models.IntegerField(default=0)
	contacts = models.IntegerField(default=0)
	meals_snacks = models.IntegerField(default=0)
	counselling_sessions = models.IntegerField(default=0)
	mentors_tutors = models.IntegerField(default=0)
	workshops = models.IntegerField(default=0)
	volunteers = models.IntegerField(default=0)

class Agency(models.Model):
	agencyName = models.CharField(max_length=128)
	program = models.CharField(max_length=128)
	city = models.CharField(max_length=32)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	
	
	
