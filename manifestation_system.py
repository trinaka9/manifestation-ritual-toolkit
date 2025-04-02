# Define the Mudra class
class Mudra:
    def __init__(self, name, element, intention, effect):
        self.name = name
        self.element = element
        self.intention = intention
        self.effect = effect

    def activate(self):
        print(f"👐 {self.name} Mudra ({self.element})")
        print(f"🎯 Intention: {self.intention}")
        print(f"✨ Effect: {self.effect}")

# Define the Manifestation class
class Manifestation:
    def __init__(self, desire, element, mudra=None, method="visualization"):
        self.desire = desire
        self.element = element
        self.mudra = mudra
        self.method = method

    def activate(self):
        print(f"\n🌠 Manifesting: {self.desire}")
        print(f"🌍 Element used: {self.element}")
        print(f"🧘 Method: {self.method}")
        if self.mudra:
            print(f"🙌 Activating with Mudra: {self.mudra.name}")
            self.mudra.activate()
        print("✨ Manifestation ritual complete.\n")

# Create a mudra
gyan = Mudra(
    name="Gyan",
    element="Air",
    intention="Clarity & Wisdom",
    effect="Boosts focus and deepens insight."
)

# Create a manifestation using the mudra
peace_manifestation = Manifestation(
    desire="A peaceful and protected home environment",
    element="Earth",
    mudra=gyan,
    method="journaling"
)

# Activate the manifestation
peace_manifestation.activate()
