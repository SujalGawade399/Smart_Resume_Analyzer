# version 1.

# from skills import skill_list
# resume_text=input("Paste your Resume here: ")

# found=[]
# for skill in skill_list:
#     if skill in resume_text:
#         found.append(skill)

#         print("Skills found in resume:")
#         print(found)


#imorting the skill list from existing skills.py file.
from skills import skill_list
resume_text=input("\n Paste your Resume here: ")
job_text=input("\n Paste the Job Description here:")

resume_skills=[]
job_skills=[]

# Checking for skills in resume and job description
for skill in skill_list:
    if skill.lower() in resume_text.lower():
        resume_skills.append(skill)

    if skill.lower() in job_text.lower():
        job_skills.append(skill)

required_skills=[ ]

for skill in job_skills:
    if skill not in resume_skills:
      required_skills.append(skill)   

# Calculating the percentage of match between resume and job description
percentage=(len(resume_skills)/len(job_skills))*100

print("\n****** Smart Resume Analyzer ******")
print("\n Skills found in Resume:")
print(resume_skills)

print("\n Skills needed for the Job:")
print(job_skills)

print("\n Skills Recommendation:")
print("Learn the following skills :")
print(required_skills)

print ("\n Match Percentage : ")
print (percentage, "%")