import os
import resend
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("RESEND_API_KEY")
resend.api_key = os.getenv("RESEND_API_KEY")
import pandas as pd
df = pd.read_csv("students.csv")

"""
Subject: Monthly English Progress Report

Dear [Parent_Name],

We are pleased to share [Student_Name]'s English assessment results.

Average Score: [Average]

Result: PASS/

Thank you for your continued support of your child's learning.

If you have any questions, please feel free to reply to this email.

Best regards,

ABC English Center
"""
#Calculating average  for each student
score_columns = ['Writing','Listening','Speaking','Reading']
average_score = df[score_columns]
student_average_score = average_score.mean(axis = 1)
df['Average'] = student_average_score
def pass_or_fail(x):
    if x < 50:
        return("FAIL")
    else:
        return("PASS")
df['Result'] = df['Average'].apply(pass_or_fail)
def generate_email(row):
    email = f"""
    Subject: Monthly English Progress Report

    Dear {row['Parent_Name']},

    We are pleased to share {row['First_Name'] + ' ' + row['Last_Name']}'s English assessment results.

    Average Score: {row['Average']}

    Result: {row['Result']}

    Thank you for your continued support of your child's learning.

    If you have any questions, please feel free to reply to this email.

    Best regards,

    Wewest english center
   """
    return email
for index,rows in df.iterrows():
    print (generate_email(rows))
    print('=' * 60)
parents = {
    "from":'onborading@resend.dev',
    'to':'mquan159357@gmail.com',
    'subject':'My first automation ',
    'html':"""
    <h1>Hello</h1>
    <p>This email is  sent automatically by python and resend</p>
    """
}
email = resend.Emails.send(parents)
print(email)



