import os
import resend
from dotenv import load_dotenv
load_dotenv()
print("API_KEY:", os.getenv("RESEND_API_KEY"))
print("Current directory",os.getcwd())
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
def build_email_payload(row):
   return  {
    "from":'onboarding@resend.dev',
    'to':row['Parent_Email'],
    'subject':f'Monthly english report: {row['First_Name']} {row['Last_Name']} ',
    'html':generate_email(row)
    }
def build_email_payload(row):
   return  {
    "from":'onboarding@resend.dev',
    'to':row['Parent_Email'],
    'subject':'My first automation ',
    'html':generate_email(row)
    }
yes = 0
no = 0
for index, row in df.iterrows():
   
    try:
      payload = build_email_payload( row)
      email = resend.Emails.send(payload)
      print(f"sent report to {row['Parent_Email']}")
      yes += 1
    except Exception as e:
        print(f"Failed to send report to {row['Parent_Email']} because: {e}")
        no += 1

print(f"""
total email sended: {yes} emails,
total emails failed to send: {no} emails,
""")
