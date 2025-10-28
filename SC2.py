#Name:
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be given a number as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

#Code Here:
bmi_weight = float(input("bmi weight (lbs):"))
bmi_height = float(input("bmi height (in):"))**2
print(bmi_weight, bmi_height)

bmi_score = bmi_weight / bmi_height
print(bmi_score)

if bmi_score < 18.5:
    print("underweight")
elif bmi_score > 18.5 and bmi_score < 25:
    print("normal")
elif bmi_score > 18.5 and bmi_score > 24.9:
    print("overweight")
else:
    print("obese")