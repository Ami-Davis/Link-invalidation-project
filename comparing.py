

class Comparing:

    def __init__(self, scores, onto1, onto2):
        self.threshold = 1.0
        self.scores = scores
        self.functional_prop = []
        self.source = onto1
        self.target = onto2

    def create_functional_prop(self, threshold):
        self.threshold = threshold
        for property in self.scores.keys():
            if self.scores[property]>= threshold:
                self.functional_prop.append(property)

    def fetch(self, element1, property, threshold, possible_twins):
        # TODO
        # According to the property call the appropriate comparing function
        new_possible_twins = []
        for twin in possible_twins:
            comparing_result = 0 # call the comparing function here
            if comparing_result >= threshold:
                new_possible_twins.append(twin)
        return new_possible_twins

    def find_twins(self, threshold):
        res = []
        for element1 in self.source.keys():
            possible_twins = self.target.keys()
            for property in self.source[element1].keys():
                if property not in self.functional_prop:
                    continue
                possible_twins = self.fetch(element1, property, threshold, possible_twins)
            if len(possible_twins) == len(self.target.keys()):
                continue
            for twin in possible_twins:
                res.append((element1,twin))

        return res