# core.py
# This is the main script that will call modules from your manifestation toolkit

from affirmations import get_affirmations
from laws import get_universal_law
from frequency_module import get_frequency
from moon_phases import get_moon_phase_guidance
from rituals import generate_ritual_kit
from energy_tips import get_energy_tips

print("\n🧬 Welcome to the Manifestation Ritual Toolkit!")
desire = input("\n✨ What would you like to manifest today? ")
category = input("Choose a category (financial, objects, love/soulmate, specific outcome, spiritual): ").lower()
method = input("How will you activate it (journaling, meditation, charged water, etc)? ")

# Generate personalized ritual tools
ritual = generate_ritual_kit(category)

print("\n💎 Ritual Kit")
print("------------------------")
print("🔮 Crystal:", ritual['crystal'])
print("🔊 Frequency:", ritual['frequency'])
print("🧘 Mudra:", ritual['mudra'])
print("💭 Intention:", ritual['intention'])
print("🌟 Effect:", ritual['effect'])
print("📿 Core Affirmation:", ritual['affirmation'])

# Add extra affirmations
print("\n✨ Additional Affirmations")
affirmation = get_affirmations(category)
print(f"✨ {affirmation}")

# Add moon phase insights
print("\n🌕 Moon Phase Insight")
print(get_moon_phase_guidance())

energy_tips = get_energy_tips(category)
print("\n⚡ Energy Tips to Raise Your Frequency")
for tip in energy_tips:
    print(f"- {tip}")

# Add Universal Law lesson
print("\n📖 Universal Law Focus")
print(get_universal_law(category))

print("\n🔁 Activation Method:", method)
print("\n🌈 You’re aligned. Reality is shifting. Keep trusting the magic.")
