import requests, math, random

class Trial:
    def __init__(self, owner_id=0):
        self.owner_id = owner_id
        self.id = 0
        self.name = 'Default Name'
        self.description = 'Default Description'
        self.difficulty = 1
        self.duration = 0
        
    def __repr__(self):
        return f'<Trial | Name: {self.name} | Owner ID: {self.owner_id}>'
    
    def set_id(self, idno):
        self.id = idno
        
    def set_name(self, name):
        self.name = name
    
    def set_description(self, description):
        self.description = description
        
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
    
    def set_duration(self, unit, quantity):
        if unit == 'days':
            self.duration = quantity * 28800
        elif unit == 'minutes':
            self.duration = quantity * 60
        elif unit == 'seconds':
            self.duration = quantity

def trial_from_dict(trial):
    new_trial = Trial()
    new_trial.set_name(trial['name'])
    new_trial.set_description(trial['description'])
    new_trial.set_difficulty(trial['difficulty'])
    new_trial.set_duration('seconds', trial['duration'])
    
    return new_trial

def get_random_trial(trials):
    random_number = random.randint(0, len(trials)-1)
    return trials[random_number]

class Gauntlet:
    def __init__(self, owner_id=0):
        self.owner_id = owner_id
        self.id = 0
        self.name = 'Default Name'
        self.trials = []
        self.class_time = 0
        self.class_days = 0
        self.weekend_days = 0
        self.extra_days = 0
        self.total_days = 0
        self.total_time = 0
        self.difficulty = 0
        self.description = ''
        
    def __repr__(self):
        return f'<Gauntlet | Name: {self.name} | Owner: {self.owner_id}>'
    
    def reset(self):
        trials_time = sum(trial.duration for trial in self.trials)
        self.class_time = int(trials_time / 60)
        self.class_days = math.ceil(self.class_time / 480)
        self.weekend_days = math.ceil(((self.class_days+ self.extra_days) / 5) * 2)
        self.total_days = self.weekend_days + self.class_days + self.extra_days
        self.total_time = self.total_days * 1440
        
        self.difficulty = sum(trial.difficulty for trial in self.trials) / len(self.trials)
        
    def set_id(self, idno):
        self.id = idno
    
    def set_name(self, name):
        self.name = name
        
    def set_extra_days(self, days):
        self.extra_days = days
        self.reset()
    
    def add_extra_days(self, days):
        self.extra_days += days
        self.reset()
    
    def set_trials(self, trials_list):
        self.trials = trials_list
        self.reset()
        
    def add_trials(self, trials_list):
        for trial in trials_list:
            self.trials.append(trial)
        self.reset()
        
    def set_description(self, description):
        self.description = description
    
    def randomize(self, trials, quantity):
        self.trials = []
        for i in range(0, quantity - 1):
            rand_num = random.randint(0, len(trials)-1)
            self.trials.append(trials[rand_num])
        self.reset()

def get_random_gauntlet(gauntlets):
    random_number = random.randint(0, len(gauntlets)-1)
    return gauntlets[random_number]


class Participant:
    def __init__(self, owner_id=0, attributes={}):
        self.owner_id = owner_id
        self.id = 0
        self.first_name = 'Default_First'
        self.last_name = 'Default_Last'
        self.attributes = attributes
        
    def __repr__(self):
        return f'<Participant | ID: {self.id} | Owner ID: {self.owner_id}>'
    
    def set_id(self, idno):
        self.id = idno
    
    def set_first_name(self, name):
        self.first_name = name
        
    def set_last_name(self, name):
        self.last_name = name
        
    def add_attribute(self, name, num):
        self.attributes[name] = num
    
    def delete_attribute(self, name):
        del self.attributes[name]
        
    def randomize(self, attributes_dict):
        for k,v in attributes_dict.items():
            random_val = random.randint(1, v)
            self.attributes[k] = random_val

def participant_from_dict(participant):
    new_participant = Participant()
    new_participant.set_id(participant['id'])
    new_participant.set_first_name(participant['name_1'].replace(' ', '_'))
    new_participant.set_last_name(participant['name_2'].replace(' ', '_'))
    new_participant.add_attribute('intellect', participant['attribute_1'])
    new_participant.add_attribute('endurance', participant['attribute_2'])
    new_participant.add_attribute('volatility', participant['attribute_3'])
    new_participant.add_attribute('background', participant['attribute_4'])
    new_participant.add_attribute('experience', participant['attribute_5'])
    return new_participant

def get_random_participant(participants):
    random_number = random.randint(0, len(participants)-1)
    return participants[random_number]

class Team:
    def __init__(self, owner_id = 0):
        self.id = 0
        self.owner_id = owner_id
        self.name = 'Default_Name'
        self.participants = []
        
    def set_id(self, idno):
        self.id = idno
        
    def set_name(self, name):
        self.name = name
    
    def set_participants(self, participants):
        self.participants = participants
        
    def add_participant(self, participant):
        self.participants.append(participant)
        
    def remove_participant(self, participant_identifier):
        for participant in self.participants:
            if participant.id == participant_identifier or participant.first_name == participant_identifier:
                self.participants.remove(participant)
                
    def randomize(self, participants, quantity):
        self.participants = []
        for i in range(0, quantity - 1):
            rand_num = random.randint(0, len(participants)-1)
            self.participants.append(participants[rand_num])

class Influencer:
    def __init__(self, owner_id=0, attributes={}):
        self.owner_id = owner_id
        self.id = 0
        self.first_name = 'Default_First'
        self.last_name = 'Default_Last'
        self.attributes = attributes
        
    def __repr__(self):
        return f'<Influencer | ID: {self.id} | Owner ID: {self.owner_id}>'
    
    def set_id(self, idno):
        self.id = idno
    
    def set_first_name(self, name):
        self.first_name = name
        
    def set_last_name(self, name):
        self.last_name = name
        
    def add_attribute(self, name, num):
        self.attributes[name] = num
    
    def delete_attribute(self, name):
        del self.attributes[name]
        
    def randomize(self, attributes_dict):
        for k,v in attributes_dict.items():
            random_val = random.randint(1, v)
            self.attributes[k] = random_val

def influencer_from_dict(influencer):
    new_influencer = Influencer()
    new_influencer.set_id(influencer['id'])
    new_influencer.set_first_name(influencer['name_1'].replace(' ', '_'))
    new_influencer.set_last_name(influencer['name_2'].replace(' ', '_'))
    new_influencer.add_attribute('quality', influencer['attribute_1'])
    new_influencer.add_attribute('commitment', influencer['attribute_2'])
    new_influencer.add_attribute('volatility', influencer['attribute_3'])
    new_influencer.add_attribute('availability', influencer['attribute_4'])
    return new_influencer  

def get_random_influencer(influencers):
    random_number = random.randint(0, len(influencers)-1)
    return influencers[random_number]

class Event:
    def __init__(self, gauntlets, owner_id=0):
        self.owner_id = owner_id
        self.id = 0
        self.name = 'Default_Name'
        self.description = 'Default_Description'
        self.gauntlets = gauntlets
        self.teams = []
        self.influencers = []
        self.obstacles = []
        self.class_time = sum([gauntlet['class_time'] for gauntlet in self.gauntlets])
        self.class_days = sum([gauntlet['class_days'] for gauntlet in self.gauntlets])
        self.total_days = sum([gauntlet['total_days'] for gauntlet in self.gauntlets])
        self.total_time = sum([gauntlet['total_time'] for gauntlet in self.gauntlets])
        self.difficulty = sum([gauntlet['difficulty'] for gauntlet in self.gauntlets]) / len(self.gauntlets)
        
    def __repr__(self):
        return f'<Event | ID: {self.id} | Owner ID: {self.owner_id}>'
    
    def set_time(self):
        self.class_time = sum([gauntlet['class_time'] for gauntlet in self.gauntlets])
        self.class_days = sum([gauntlet['class_days'] for gauntlet in self.gauntlets])
        self.total_days = sum([gauntlet['total_days'] for gauntlet in self.gauntlets])
        self.total_time = sum([gauntlet['total_time'] for gauntlet in self.gauntlets])
        self.difficulty = sum([gauntlet['difficulty'] for gauntlet in self.gauntlets]) / len(self.gauntlets)
    
    def set_id(self, idno):
        self.id = idno
    
    def set_name(self, name):
        self.name = name
        
    def set_description(self, description):
        self.description = description
        
    def set_gauntlets(self, gauntlets):
        self.gauntlets = gauntlets
        self.set_time()
        
    def add_gauntlet(self, gauntlet):
        self.gauntlets.append(gauntlet)
        self.set_time()
        
    def remove_gauntlet(self, gauntlet_identifier):
        if len(self.gauntlets) <= 1:
            return f'Must have at least 1 gauntlet in an event!'
        else:
            for gauntlet in self.gauntlets:
                if gauntlet.id == gauntlet_identifier or gauntlet.name == gauntlet_identifier:
                    self.gauntlets.remove(gauntlet)
        self.set_time()
        
    def set_teams(self, teams):
        self.teams = teams
        
    def add_team(self, team):
        self.teams.append(team)
        
    def remove_team(self, team_identifier):
        for team in self.teams:
            if team.id == team_identifier or team.name == team_identifier:
                self.teams.remove(team)
        
    def set_influencers(self, influencers):
        self.influencers = influencers
        
    def add_influencer(self, influencer):
        self.influencers.append(influencer)
        
    def remove_influencer(self, influencer_identifier):
        for influencer in self.influencers:
            if influencer.id == influencer_identifier or influencer.first_name == influencer_identifier:
                self.influencers.remove(influencer)
                
    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        
    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)
        
    def remove_obstacle(self, obstacle_identifier):
        for obstacle in self.obstacles:
            if obstacle.id == obstacle_identifier or obstacle.name == obstacle_identifier:
                self.obstacles.remove(obstacle)
                
    def randomize_all(self, parts_dict):
#         parts_dict = {
#             'gauntlets': [quantity, [gauntlets_list]],
#             'teams': [quantity, [participants_list]],
#             'influencers': [quantity, [influencers_list]],
#             'obstacles': [quantity, [obstacles_list]]
#         }
        self.gauntlets = []
        self.teams = []
        self.influencers = []
        self.obstacles = []
        
        for k,v in parts_dict.items():
            if k == 'gauntlets':
                quantity = v[0]
                for i in range(0, quantity):
                    random_number = random.randint(0, len(v[1])-1)
                    self.gauntlets.append(v[1][random_number])
            elif k == 'teams':
                quantity = v[0]
                for i in range(0, quantity):
                    random_number = random.randint(0, len(v[1])-1)
                    self.teams.append(v[1][random_number])
            elif k == 'influencers':
                quantity = v[0]
                for i in range(0, quantity):
                    random_number = random.randint(0, len(v[1])-1)
                    self.influencers.append(v[1][random_number])
            elif k == 'obstacles':
                quantity = v[0]
                for i in range(0, quantity):
                    random_number = random.randint(0, len(v[1])-1)
                    self.obstacles.append(v[1][random_number])
            
        self.set_time()

def get_random_event(events):
    random_number = random.randint(0, len(events)-1)
    return events[random_number]