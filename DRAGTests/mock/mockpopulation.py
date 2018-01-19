from DRAGProj.dragcommon.track import Track


class MockPopulation:
    def __init__(self):
        self.population = []
        self.child_population = []
        self._populate()
        self._populate_child_population()

    def _populate(self):
        for i in range(10):
            self.population.append(Track([1, 2, 3, 4, 5, 6, 7, 8], 1))

    def _populate_child_population(self):
        for i in range(10):
            self.child_population.append(Track([8, 7, 6, 5, 4, 3, 2, 1], 1))
