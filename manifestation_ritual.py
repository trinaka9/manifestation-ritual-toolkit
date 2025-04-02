import random

# Categories and aligned ritual components
manifestation_data = {
    "financial abundance": {
        "crystal": "Citrine",
        "frequency": "639Hz - Abundance Alignment",
        "mudra": "Kubera",
        "intention": "Attracting financial flow and wealth",
        "effect": "Unlocks opportunities and abundance mindset",
        "affirmation": "I am a magnet for wealth and prosperity."
    },
    "objects": {
        "crystal": "Pyrite",
        "frequency": "741Hz - Manifestation Activation",
        "mudra": "Prana",
        "intention": "Calling in physical resources or items",
        "effect": "Magnifies attraction of tangible goals",
        "affirmation": "Everything I desire flows easily into my life."
    },
    "love/soulmate": {
        "crystal": "Rose Quartz",
        "frequency": "528Hz - Heart Healing",
        "mudra": "Hridaya",
        "intention": "Calling in divine connection and love",
        "effect": "Opens heart and aligns you to soul partnerships",
        "affirmation": "I am worthy of deep, soulful love."
    },
    "specific outcome": {
        "crystal": "Clear Quartz",
        "frequency": "963Hz - Divine Alignment",
        "mudra": "Hakini",
        "intention": "Clarifying and energizing a specific result",
        "effect": "Focuses will and energy on one outcome",
        "affirmation": "My vision is clear, and my reality aligns with it."
    },
    "spiritual": {
        "crystal": "Amethyst",
        "frequency": "528Hz - DNA repair and heart healing",
        "mudra": "Gyan",
        "intention": "Clarity & Wisdom",
        "effect": "Boosts focus and deepens insight",
        "affirmation": "I trust my intuition and walk in truth."
    }
}

# Ask user for input
manifest = input("What would you like to manifest today? ")
category = input("Choose a category (financial abundance, objects, love/soulmate, specific outcome, spiritual): ").lower()
method = input("How will you activate it (journaling, meditation, charged water, etc)? ")

# Use data if category is valid
if category in manifestation_data:
    data = manifestation_data[category]
    print("\n✨ Manifesting:", manifest)
    print("🔮 Crystal:", data["crystal"])
    print("🔊 Frequency:", data["frequency"])
    print("🧘 Mudra:", data["mudra"])
    print("💭 Intention:", data["intention"])
    print("🌟 Effect:", data["effect"])
    print("📿 Affirmation:", data["affirmation"])
    print("🌊 Method:", method)
    print("\nManifestation ritual complete.")
else:
    print("Category not found. Please choose from the suggested list.")
