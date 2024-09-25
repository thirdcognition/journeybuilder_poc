import random

def get_position_data():

    type = ["New hire onboarding", "Project onboarding", "Skill development", "Customer onboarding"]
    team = ["Business", "Product", "Sales", "Tech"]
    position = ["Product", "Customer Success", "Account", "Business Development", "Development"]
    level = ["Manager", "Director"]
    location = ["Helsinki", "Stockholm", "New York", "Berlin", "San Fransisco", "Tokyo"]
    modules = random.randint(7, 9)
    length = random.randint(8, 12)
    position_data = {}

    position_data["type"] = random.choice(type)
    position_data["team"] = random.choice(team)
    position_data["position"] = random.choice(position) + " " + random.choice(level)
    position_data["location"] = random.choice(location)
    position_data["modules"] = modules
    position_data["length"] = length

    return position_data

