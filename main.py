import datetime
import random

# List of cybersecurity facts
cyber_security_facts = [
    "90% of cyber attacks are caused by human error.",
    "Phishing is the most common attack vector for cybercriminals.",
    "Multi-factor authentication adds an extra layer of security.",
    "Ransomware attacks are on the rise, targeting individuals and organizations.",
    "Regular software updates help protect against known vulnerabilities.",
    "Social engineering exploits human psychology to gain unauthorized access.",
    "Zero-day vulnerabilities are unknown to software vendors and can be exploited by attackers.",
    "Security breaches can lead to financial losses, data breaches, and reputation damage.",
    "Firewalls act as a barrier between trusted and untrusted networks.",
    "A strong password is a crucial defense against unauthorized access.",
    "Security awareness training helps educate users about cyber threats.",
]

# Get today's date
today = datetime.date.today()

# Calculate an index based on the date
random.seed(today.year + today.month + today.day)
random_index = random.randint(0, len(cyber_security_facts) - 1)

# Get the fact for the day
fact_of_the_day = cyber_security_facts[random_index]

# Display the fact
print(f"🔐 Cybersecurity Fact of the Day ({today}):")
print(f"{fact_of_the_day}")