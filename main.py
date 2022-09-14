import faker

faker_obj = faker.Faker()

gender = 'M' 
male_profile = faker_obj.simple_profile(sex=gender)
phone = faker_obj.phone_number()
print("Male profile generated is as follows:\n", male_profile , phone)

gender = 'F'
male_profile = faker_obj.simple_profile(sex=gender)
print("Female profile generated is as follows:\n", male_profile, phone)