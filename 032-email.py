import smtplib

def main():
  FROM_EMAIL = ""
  APP_PASS = ""
  TO_EMAIL = ""
  with smtplib.SMTP("smtp.gmail.com") as conn:
    conn.starttls()
    conn.login(user=FROM_EMAIL, password=APP_PASS)
    conn.sendmail(from_addr=FROM_EMAIL, to_addrs=TO_EMAIL, msg="Subject:Python-generated email\nThis message was sent from a Python script")


if __name__ == "__main__":
  main()