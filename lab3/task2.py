# 2) Regex Log Cleaner
#    - Create a file called "access.log" with 10 fake log lines
#      (mix valid emails and invalid strings).
#    - Use regex to extract all valid emails.
#    - Save them into "valid_emails.txt".
#    - Print how many unique emails were found.

import re
from task7 import log_time

@log_time
def regex_log_cleaner():

    log_filename = "access.log"
    fake_logs = [
        "User john.doe@example.com accessed the system",
        "Error from invalid_user at 10:45",
        "Contact admin@mailserver.org for support",
        "Random string without email",
        "User jane_smith99@gmail.com logged in",
        "Failed login by test@.com",
        "Sent report to boss123@company.co.uk",
        "Invalid format user@@site.com",
        "Guest michael-23@yahoo.com joined",
        "Broken entry: userexample.com"
    ]

    with open(log_filename,"w") as f:
        for l in fake_logs:
            f.write(l+'\n')

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    with open(log_filename,'r') as f:
        data=f.read()
    
    emails_found=re.findall(email_pattern,data)

    unq_emails=sorted(set(emails_found))

    print(f"uniqe emails are {len(unq_emails)}")

    output_f="valid_emails.txt"
    with open(output_f,"w") as f:
        for e in unq_emails:
            f.write(e+"\n")
    print(f"\n '{output_f}' is created \n")