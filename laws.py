import random

def get_universal_law(category):
    laws_by_category = {
        "financial abundance": [
            {
                "law": "Law of Compensation",
                "description": "The more good you put out into the world, the more abundance returns to you."
            },
            {
                "law": "Law of Attraction",
                "description": "Like attracts like. Focusing on wealth draws wealth into your experience."
            }
        ],
        "objects": [
            {
                "law": "Law of Vibration",
                "description": "Everything has a frequency. Align with the vibration of the object you want to manifest."
            },
            {
                "law": "Law of Perpetual Transmutation of Energy",
                "description": "You can change energy with your intention. Thought into form."
            }
        ],
        "love/soulmate": [
            {
                "law": "Law of Divine Oneness",
                "description": "We are all connected. Loving yourself invites love from others."
            },
            {
                "law": "Law of Giving and Receiving",
                "description": "To receive love, give love freely and without expectation."
            }
        ],
        "specific outcome": [
            {
                "law": "Law of Cause and Effect",
                "description": "Every action you take creates a result. Choose actions aligned with your desired outcome."
            },
            {
                "law": "Law of Clarity",
                "description": "Be clear in your intentions and the Universe will respond."
            }
        ],
        "spiritual": [
            {
                "law": "Law of Inspired Action",
                "description": "Don't just visualize—take aligned spiritual action."
            },
            {
                "law": "Law of Correspondence",
                "description": "As within, so without. Your inner world shapes your outer reality."
            }
        ]
    }

    selected = random.choice(laws_by_category.get(category.lower(), [
        {"law": "Law of Attraction", "description": "You attract what you are. Stay aligned."}
    ]))

    return f"{selected['law']}: {selected['description']}"
