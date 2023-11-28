print("Melanie Dental Clinic")
print("____________________")

name = input("Patient's name: ")
visited_before = input("Has the patient been here before? (Yes/No): ")
last_visit = input("How many days since your last visit: ")
height = int(input("What is the patient’s height (in cm)?: "))
current_weight = float(input("What is the patient’s weight (in kg)?: "))
last_weighed = input("When was the patient last weighed in (1/1/2000 if never weighed)?: ")
previous_weight = float(input("What was the patient’s weight (in kg, -1 if never weighed)?: "))
practitioner_assessment = int(input("Practitioner’s overall assessment of the patient’s health (-5 to +5)?: "))

print("Return Report")
print("____________________")

BMI = (current_weight / (height ** 2)) * 100

if BMI > 30:
    intermediate_score = 0
elif 25 <= BMI <= 29.9:
    intermediate_score = 3
elif 18.5 <= BMI <= 24.9:
    intermediate_score = 5
else:
    intermediate_score = 3

final_score = intermediate_score + practitioner_assessment

if final_score > 5:
    health_condition = 'Great condition!'
elif 3 <= final_score <= 5:
    health_condition = 'Need a little work'
elif 1 <= final_score < 3:
    health_condition = 'Need a lot of work'
else:
    health_condition = 'At risk!'

print("Receipt for patient name: {name}")
print("Patient weight: {current_weight} kg")
print("Days since last visit: {last_visit}")
print("------------------------------")
print("BMI: {BMI}")
print("Intermediate Health Score: {intermediate_score}")
print("Practitioner's Assessment of Health: {practitioner_assessment}")
print("------------------------------")
print("Final Score: {final_score}")
print("Health Condition: {health_condition}")
