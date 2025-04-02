import random

# List of affirmations using "I" statements
affirmations = [
    "I am powerful and capable.",
    "Everything is working in my favor.",
    "I am exactly where I need to be.",
    "Abundance flows to me effortlessly.",
    "My energy creates my reality.",
    "I am aligned with my highest timeline.",
    "I am a magnet for miracles.",
    "I am calm, grounded, and in control.",
    "All the right opportunities are flowing to me now.",
    "I am becoming more of who I truly am every day."
    "I get job offers often and easily."
    "I am wanted for my AI work and cybersecurity."
]

# Ask for name
name = input("What's your name? ")

# Ask how many affirmations
count = int(input("How many affirmations do you want today? "))

# Generate affirmations
print(f"\n{name}, here are your affirmations:")
selected = random.sample(affirmations, count)

for line in selected:
    print("🌟", line)

# Ask to save affirmations to a journal file
save = input("\nDo you want to save these to your affirmation journal? (yes/no): ").lower()

if save == "yes":
    with open("daily_journal.txt", "a") as file:
        file.write(f"\n{name}'s Affirmations:\n")
        for line in selected:
            file.write(f"- {line}\n")
        file.write("-----------\n")
    print("✅ Saved to daily_journal.txt")
