from faker import Faker

faker1= Faker()

def profiles(num):
    lls = []
    for _ in range(num):
        profile = {
            'name': faker1.name(),
            'city': faker1.city()
        }
        lls.append(profile)
    return lls



# def save_to_csv(lls):
#     header=profile[0]


    
print(profiles(7))