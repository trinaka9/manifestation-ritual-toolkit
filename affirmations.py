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

# ✅ Function for importing
def get_affirmations(count):
    return random.sample(affirmations, count)

# Optional: Run interactively when executed directly
if __name__ == "__main__":
    name = input("What's your name? ")
    count = int(input("How many affirmations do you want today? "))

    selected = get_affirmations(count)

    print(f"\n{name}, here are your affirmations:")
    for line in selected:
        print("⭐", line)

    save = input("\nDo you want to save these to your affirmation journal? (yes/no): ").lower()

    if save == "yes":
        with open("daily_journal.txt", "a") as file:
            file.write(f"\n{name}'s Affirmations:\n")
            for line in selected:
                file.write(f"⭐ {line}\n")
            file.write("\n")
        print("✅ Saved to daily_journal.txt")
