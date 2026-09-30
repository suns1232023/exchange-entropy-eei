import unittest
import numpy as np
from eei import EEICalculator, normalize_series, NetworkTopologyMetrics


class TestEEICalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = EEICalculator(c1_threshold=0.7, c2_threshold=0.3)

    def test_eei_high_regime(self):
        np.random.seed(42)
        delta_P = np.random.normal(0, 1, 100)
        delta_F = 0.9 * delta_P + np.random.normal(0, 0.1, 100)
        delta_N = 0.1 * delta_P + np.random.normal(0, 0.1, 100)

        res = self.calculator.compute_eei(delta_F, delta_N, delta_P)
        regime, _ = self.calculator.classify_regime(res["eei"])

        self.assertGreater(res["eei"], 0.7)
        self.assertEqual(regime, "Phase I: High-EEI")

    def test_normalization(self):
        data = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
        norm = normalize_series(data)
        self.assertAlmostEqual(float(np.mean(norm)), 0.0, places=5)
        self.assertAlmostEqual(float(np.std(norm)), 1.0, places=5)

    def test_isolation_intensity(self):
        adj = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
        partition = np.array([1, 1, 2])
        sigma = NetworkTopologyMetrics.compute_silo_isolation_intensity(adj, partition)
        self.assertEqual(sigma, 1.0)


if __name__ == "__main__":
    unittest.main()
