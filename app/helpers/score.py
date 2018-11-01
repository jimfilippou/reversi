class Score:

    def __init__(self, human, ai):
        self._human = human
        self._ai = ai
        self._total = human + ai

    @property
    def human(self):
        return self._human

    @human.setter
    def human(self, value):
        self._human = value
        self.update_total()

    @property
    def ai(self):
        return self._ai

    @ai.setter
    def ai(self, value):
        self._ai = value
        self.update_total()

    @property
    def total(self):
        return self._total

    def update_total(self):
        self._total = self._ai + self._human
