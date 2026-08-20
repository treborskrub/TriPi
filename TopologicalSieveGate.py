import numpy as np
import unittest
from enum import IntEnum

# =====================================================================
# TRINARY STATE DEFINITIONS
# =====================================================================
class TrinaryLogic(IntEnum):
    RELEVANT = 1      # Wave Crest (+1.0) / Active valid signal payload
    UNKNOWN = 0       # Structural Ground Neutral (0.0) / Waiting or missing payload
    IRRELEVANT = -1   # Wave Trough (-1.0) / Dead-end noise to be filtered
    
# =====================================================================
# SYSTEM MODULE: Pi-Phi-1-3-Shortfall-Sieve
# =====================================================================
class TopologicalSieveGate:
    """
    Implements a zero-overhead wave-domain input validator.
    Uses binary frequency management of a trinary spatial geometry
    to force chaotic noise into total destructive phase collapse (0V).
    """
    def __init__(self, num_nodes: int = 14):
        self.num_nodes = num_nodes
        # Restored to exact original hardware emulation precision
        self.phi = 1.61803398875  
        self.sieve_threshold = np.pi * self.phi * (1.0 / 3.0)
        self.lambda_max = 1.10  # Maximum tolerated amplitude expansion ratio

    def binary_to_balanced_ternary(self, bitstream: str) -> np.ndarray:
        """
        Compresses asymmetrical binary strings into Balanced Ternary vectors (-1, 0, +1).
        Maps bits directly to physical wave-crests (+1), troughs (-1), and neutral ground (0).
        """
        ternary_vector = []
        for i in range(0, len(bitstream), 2):
            chunk = bitstream[i:i+2]
            if chunk == "11":
                ternary_vector.append(float(TrinaryLogic.RELEVANT))     # Phase Crest (+1.0)
            elif chunk == "00":
                ternary_vector.append(float(TrinaryLogic.IRRELEVANT))   # Phase Trough (-1.0)
            else:
                ternary_vector.append(float(TrinaryLogic.UNKNOWN))      # Structural Ground Neutral (0.0)
            if len(ternary_vector) == self.num_nodes:
                break

        # Pad system fabric to preserve trinary coordination geometry dimensions
        while len(ternary_vector) < self.num_nodes:
            ternary_vector.append(float(TrinaryLogic.UNKNOWN))
        return np.array(ternary_vector[:self.num_nodes])

    def audit_signal_wavefront(self, initial_state: np.ndarray, iterations: int = 3) -> tuple:
        """
        Passes continuous waves through the 3D HCP boundary filter.
        Applies Early-Exit routing: if an absolute dead end / toxic sequence
        is encountered via trinary minimum logic rules, it forces instant phase collapse.
        """
        state = np.copy(initial_state)
        
        # --- EARLY EXIT TRINARY RELEVANCE GATE ---
        global_logic_state = int(np.min(state))
        if global_logic_state == TrinaryLogic.IRRELEVANT and np.max(state) <= 0.0:
            return np.zeros(self.num_nodes), True, 0.0, 0

        # Sieve operations execute over minimum 3 passes to confirm temporal sync
        for cycle in range(1, iterations + 1):
            old_state = np.copy(state)

            # Simulate spatial refraction (1/3 split) and geometric circular closure (π)
            rotation_matrix = np.roll(state, 1) * (1.0 / 3.0)
            state = (state * np.cos(self.sieve_threshold)) + (rotation_matrix * np.sin(self.sieve_threshold))

            # Calculate Phase Amplitude Expansion Ratio (λ)
            norm_old = np.linalg.norm(old_state)
            lambda_ratio = 0.0 if norm_old == 0 else np.linalg.norm(state - old_state) / norm_old

            # Hardware-Level Error Check Boundary
            if lambda_ratio > self.lambda_max:
                return np.zeros(self.num_nodes), True, lambda_ratio, cycle

        return state, False, lambda_ratio, iterations

# =====================================================================
# UNIT TESTING SUITE
# =====================================================================
class TestTopologicalSieve(unittest.TestCase):
    def setUp(self):
        """Initializes the 14-node hardware gate emulator cleanly within the cell context."""
        self.gate = TopologicalSieveGate(num_nodes=14)

    def test_binary_to_ternary_mapping(self):
        """Validates that binary strings compress cleanly into [-1, 0, +1] states."""
        bitstream = "110011"  # Crest, Trough, Crest
        vector = self.gate.binary_to_balanced_ternary(bitstream)

        self.assertEqual(vector[0], 1.0)
        self.assertEqual(vector[1], -1.0)
        self.assertEqual(vector[2], 1.0)
        self.assertEqual(len(vector), 14)  # Ensures structural grid sizing holds

    def test_valid_signal_preservation(self):
        """Ensures structurally-harmonized waves pass through the sieve without collapsing."""
        # Aligned with the structurally sound live sandbox sequence length
        valid_stream = "11001111000011001111"
        valid_wave = self.gate.binary_to_balanced_ternary(valid_stream)

        output, collapsed, _, _ = self.gate.audit_signal_wavefront(valid_wave, iterations=3)
        self.assertFalse(collapsed, "Sieve incorrectly collapsed a valid signal structure.")
        self.assertFalse(np.all(output == 0.0), "Valid output wavefront was erased to zero.")

    def test_chaotic_noise_collapse(self):
        """Validates that extreme amplitude expansion triggers immediate destructive phase collapse (0V)."""
        chaotic_wave = np.array([5.0, -5.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

        output, collapsed, _, _ = self.gate.audit_signal_wavefront(chaotic_wave, iterations=3)
        self.assertTrue(collapsed, "Sieve failed to trigger a destructive interference safety reflex on noise.")
        np.testing.assert_array_equal(output, np.zeros(14), "Corrupted wavefront was not cleanly cleared to 0V ground.")

# Sandbox runner
if __name__ == "__main__":
    print("Running Unit Tests...")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTopologicalSieve)
    unittest.TextTestRunner(verbosity=2).run(suite)
