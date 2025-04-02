import random

def get_moon_phase_guidance():
    moon_phases = [
        {
            "phase": "New Moon",
            "meaning": "Time for setting new intentions and planting seeds.",
            "tip": "Write down what you want to manifest and charge it under the moonlight."
        },
        {
            "phase": "Waxing Crescent",
            "meaning": "Take action on your intentions.",
            "tip": "Visualize your goals growing with the moon."
        },
        {
            "phase": "First Quarter",
            "meaning": "Overcome obstacles and stay committed.",
            "tip": "Reaffirm your goals and remove distractions."
        },
        {
            "phase": "Waxing Gibbous",
            "meaning": "Refine your intentions and prepare for manifestation.",
            "tip": "Fine-tune your vision with clarity and gratitude."
        },
        {
            "phase": "Full Moon",
            "meaning": "Peak manifestation and release what no longer serves you.",
            "tip": "Perform a release ritual and express gratitude."
        },
        {
            "phase": "Waning Gibbous",
            "meaning": "Harvest insights and share knowledge.",
            "tip": "Journal your lessons and realign if needed."
        },
        {
            "phase": "Last Quarter",
            "meaning": "Let go and forgive.",
            "tip": "Declutter, reflect, and clear mental/emotional blocks."
        },
        {
            "phase": "Waning Crescent",
            "meaning": "Rest and renew.",
            "tip": "Meditate, rest, and prepare for the next cycle."
        }
    ]
    return random.choice(moon_phases)
