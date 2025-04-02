def get_energy_tips(category):
    tips = {
        "financial abundance": [
            "Practice gratitude for the money you already have.",
            "Identify and release scarcity mindset.",
            "Visualize yourself already in abundance.",
            "Quit harm-causing habits like overspending or smoking.",
            "Spend time outdoors grounding to attract prosperity."
        ],
        "objects": [
            "Clean and organize your space to make room for the object.",
            "Hold the vision of already using the object with joy.",
            "Write about how it feels to have it now.",
            "Ground your energy by walking barefoot on the earth.",
            "Surround yourself with visual reminders of the object."
        ],
        "love/soulmate": [
            "Practice self-love and care daily.",
            "Release old relationship baggage with forgiveness.",
            "Raise your vibration with music and movement.",
            "Spend time in nature to open your heart.",
            "Visualize the feeling of being loved and seen."
        ],
        "specific outcome": [
            "Clarify exactly what you want and why.",
            "Act as if the outcome already happened.",
            "Stay grounded and present each day.",
            "Identify emotional blocks and reframe them.",
            "Trust the process, even when things shift."
        ],
        "spiritual": [
            "Identify your emotions and choose higher vibrations.",
            "Practice daily gratitude journaling.",
            "Avoid gossip and negative media.",
            "Ground in nature to balance your energy.",
            "Use breathwork to move energy through your body."
        ]
    }
    return tips.get(category, tips["spiritual"])
