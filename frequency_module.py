import random

def get_frequency(category):
    tips = {
        "financial abundance": [
            "Listen to 639Hz to attract abundance.",
            "Clean and organize your space to welcome wealth.",
            "Visualize financial blessings flowing into your life."
        ],
        "objects": [
            "Use 417Hz for manifestation power.",
            "Surround your space with the item’s image or symbol.",
            "Affirm: 'This object is already mine, I am grateful.'"
        ],
        "love/soulmate": [
            "Tune into 528Hz for love and DNA repair.",
            "Wear rose quartz or meditate on heart-opening scenes.",
            "Affirm: 'I attract divine love effortlessly.'"
        ],
        "specific outcome": [
            "Focus on 741Hz to clear negative thought loops.",
            "Speak your desired outcome aloud with confidence.",
            "Use fire or candle rituals to energize the result."
        ],
        "spiritual": [
            "Meditate with 963Hz to connect with Source.",
            "Sit under the moon or sun for energetic alignment.",
            "Write channeled messages to elevate your vibration."
        ]
    }
    return tips.get(category, ["Take deep breaths and trust your journey."])
