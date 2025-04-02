def generate_ritual_kit(category):
    ritual_kit = {
        "financial": {
            "crystal": "Citrine",
            "frequency": "639Hz – Abundance Alignment",
            "mudra": "Kubera",
            "intention": "Attracting financial flow and wealth",
            "effect": "Unlocks opportunities and abundance mindset",
            "affirmation": "I am a magnet for wealth and prosperity."
        },
        "objects": {
            "crystal": "Clear Quartz",
            "frequency": "741Hz – Manifestation Focus",
            "mudra": "Hakini",
            "intention": "Amplify intention to attract specific object",
            "effect": "Enhances clarity and object manifestation",
            "affirmation": "What I seek is seeking me."
        },
        "love/soulmate": {
            "crystal": "Rose Quartz",
            "frequency": "528Hz – Heart Healing",
            "mudra": "Hridaya",
            "intention": "Calling in divine love and soulmate connection",
            "effect": "Heals emotional blocks and opens heart",
            "affirmation": "I am worthy of deep, unconditional love."
        },
        "specific outcome": {
            "crystal": "Labradorite",
            "frequency": "963Hz – Reality Shifting",
            "mudra": "Dhyana",
            "intention": "Lock in the timeline for the desired outcome",
            "effect": "Assists timeline anchoring and mental clarity",
            "affirmation": "The outcome I desire is already mine."
        },
        "spiritual": {
            "crystal": "Amethyst",
            "frequency": "528Hz – DNA Repair & Healing",
            "mudra": "Gyan",
            "intention": "Spiritual protection and clarity",
            "effect": "Boosts intuition and opens insight",
            "affirmation": "I am connected to divine truth and wisdom."
        }
    }

    return ritual_kit.get(category, ritual_kit["spiritual"])
