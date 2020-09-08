from dataclasses import dataclass
import numpy as np

@dataclass
class Needle:
    width: float
    cos_angle: float
    center: float


class BuffonDistribution:

    def __init__(self, needle_width, strip_width):
        self.needle_width = float(needle_width)  # width of the needle
        self.strip_width = float(strip_width)  # witdh of the space
        self.needle_center = None

    def sample(self):
        # throwing a needle
        needle_center = np.random.uniform(0, self.strip_width)
        c = self._sample_cosine_random_angle()
        needle = Needle(width=self.needle_width, center=needle_center, cos_angle=c)
        return needle

    def _sample_cosine_random_angle(self, ):
        while True:
            u = 2 * np.random.uniform(0, 1.) -1 #(-1, 1)
            v = np.random.uniform(0, 1.) #(0, 1)
            r = v * v + u * u
            if r < 1:
                break
        return (u * u - v * v) / r


class Simulation:

    def __init__(self, n_throws=1000, n_simulations=10, needle_width=1, strip_width=1):
        self.n_throws = n_throws
        self.n_simulations = n_simulations
        self.needle_width = needle_width
        self.strip_width = strip_width
        self.buffon_dist = BuffonDistribution(needle_width=needle_width, strip_width=strip_width)

    def hit(self, needle):
        if needle.center + needle.cos_angle * self.needle_width / 2 >= self.strip_width or needle.center - needle.cos_angle * self.needle_width / 2 <=0:
            return True
        return False

    def run(self):
        pi_estimates = []
        for i in range(self.n_simulations):
            n_hits = 0
            for j in range(self.n_throws):
                needle = self.buffon_dist.sample()
                if self.hit(needle):
                    n_hits += 1

            estimate = self.needle_width/self.strip_width * float(self.n_throws) / float(n_hits)
            pi_estimates.append(estimate)
        return pi_estimates


if __name__ == "__main__":
    simulation = Simulation(n_throws=80000, needle_width=1, strip_width=4)
    pi_estimates = simulation.run()
    print(pi_estimates)