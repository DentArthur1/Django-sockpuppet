from sockpuppet.reflex import Reflex


class YourReflexNameReflex(Reflex):
    def increment(self, step=1):
        self.count = int(self.element.dataset['count']) + step
        self.broadcast({'count': self.count})  # Invia il nuovo valore al client