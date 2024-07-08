from faker import Faker
import csv

# Initialize Faker
fake = Faker()

# Function to generate fake profiles
def generate_fake_profiles(num_profiles):
    profiles = []
    for _ in range(num_profiles):
        profile = {
            'name': fake.name(),
            'address': fake.address(),
            'email': fake.email(),
            'date_of_birth': fake.date_of_birth(),
            'phone_number': fake.phone_number(),
            'credit_card': fake.credit_card_full(),
            'company': fake.company(),
            'job': fake.job()
        }
        profiles.append(profile)
    return profiles

# Function to save data to CSV
def save_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

# Generate 10 fake profiles
fake_profiles = generate_fake_profiles(10)

# Print the generated profiles
for profile in fake_profiles:
    print(profile)

# Save the fake profiles to a CSV file
save_to_csv(fake_profiles, 'fake_profiles.csv')

# Create a Faker instance for French locale
fake_fr = Faker('fr_FR')

# Generate and print some French locale fake data
print("Nom (French):", fake_fr.name())
print("Adresse (French):", fake_fr.address())
