import numpy as np
from enum import IntEnum
from typing import Dict, List

# =====================================================================
# TRINARY STATE BOUNDARIES
# =====================================================================
class TrinaryLogic(IntEnum):
    RELEVANT = 1      # Wave Crest (+1)   -> Active Reality
    UNKNOWN = 0       # Ground Neutral (0) -> Shortfall Threshold (Transcendence)
    IRRELEVANT = -1   # Wave Trough (-1)   -> Path Void (Early-Exit)

# =====================================================================
# THE HARDWARE FABRIC: T-CPU
# =====================================================================
class TrinaryProcessor:
    def __init__(self, num_nodes: int = 14):
        self.num_nodes = num_nodes
        self.registers = {
            "R1": np.zeros(self.num_nodes),
            "ACC": np.zeros(self.num_nodes),
            "SR": int(TrinaryLogic.UNKNOWN)
        }
        self.phi = 1.61803398875
        self.sieve_threshold = np.pi * self.phi * (1.0 / 3.0)

    def load_register(self, wave_vector: np.ndarray):
        self.registers["R1"] = np.copy(wave_vector)

    def execute_refract_rotation(self):
        """Simulates spatial refraction (1/3 split) and geometric circular closure (π)"""
        state = np.copy(self.registers["R1"])
        rotation_matrix = np.roll(state, 1) * (1.0 / 3.0)
        new_state = (state * np.cos(self.sieve_threshold)) + (rotation_matrix * np.sin(self.sieve_threshold))
        
        # Capture the natural geometric shortfall expansion ratio (λ)
        norm_old = np.linalg.norm(state)
        lambda_ratio = 0.0 if norm_old == 0 else np.linalg.norm(new_state - state) / norm_old
        
        # Store results into the accumulator register
        self.registers["ACC"] = new_state
        return lambda_ratio

# =====================================================================
# THE BIOLOGICAL LOOP CONTROLLER
# =====================================================================
class CosmicLoopController:
    """
    Orchestrates the 5 emergent abilities of the Pi-Phi-1/3 framework.
    Manages Phase Shifts, Threshold Transcendence, and Emergence.
    """
    def __init__(self, cpu: TrinaryProcessor):
        self.cpu = cpu
        self.lambda_max = 1.35  # Dynamic tracking threshold
        self.memory_log = []

    def process_wavefront_cycle(self, task_name: str, incoming_wave: np.ndarray):
        print(f"\n⚡ [LOOP CONTROLLER] Initializing Cycle for Process: '{task_name}'")
        print(f"  Raw Input Vector: {incoming_wave}")
        
        # -----------------------------------------------------------------
        # STEP 1: AUDIT (The Field Boundary Condition)
        # -----------------------------------------------------------------
        min_val = np.min(incoming_wave)
        max_val = np.max(incoming_wave)
        
        # TRANSCENDENCE CHECK: Early-Exit Routing if the path drops to a pure Void
        if min_val == float(TrinaryLogic.IRRELEVANT) and max_val <= 0.0:
            print("  🛑 [ABILITY 1: AUDIT] -> Result: IRRELEVANT (VOID).")
            print("  ✨ [TRANSCENDENCE] Instantly bypassing execution loop. 0 CPU cycles wasted.")
            return "CYCLE_VOIDED_EARLY_EXIT"
            
        # SHORTFALL CHECK: Standby holding pattern if data is missing
        elif np.all(incoming_wave == 0.0):
            print("  ⏳ [ABILITY 1: AUDIT] -> Result: UNKNOWN (SHORTFALL).")
            print("  ✨ [TRANSCENDENCE] Process parked in neutral standby grid.")
            return "CYCLE_HELD_IN_SHORTFALL"
            
        print("  ✅ [ABILITY 1: AUDIT] -> Result: RELEVANT (ACTIVE). Signal allowed past field boundary.")

        # -----------------------------------------------------------------
        # STEP 2: PRUNE (Resonant Decay Selection)
        # -----------------------------------------------------------------
        # Load the wave vector directly onto our 14-node hardware fabric registers
        self.cpu.load_register(incoming_wave)
        measured_lambda = self.cpu.execute_refract_rotation()
        
        print(f"  🌀 [PHASE SHIFT] Wave refracted via Pi-Phi-1/3 geometry. Measured Expansion λ = {measured_lambda:.4f}")
        
        if measured_lambda > self.lambda_max:
            print(f"  ✂️ [ABILITY 2: PRUNE] -> Expansion ({measured_lambda:.2f}) over limit ({self.lambda_max}). Triggering resonant decay.")
            self.cpu.registers["ACC"] = np.zeros(self.cpu.num_nodes)
            print("  💥 [DESTRUCTIVE COLLAPSE] Wavefront cleanly forced down to 0V ground zero.")
            return "CYCLE_COLLAPSED_BY_PRUNER"
        else:
            print("  🟢 [ABILITY 2: PRUNE] -> Wave structural variance verified stable. Allowed to propagate.")

        # -----------------------------------------------------------------
        # STEP 3: RESOLVE (Phase Realignment)
        # -----------------------------------------------------------------
        # Snap the continuous analog wave refractions back into crisp, steady balanced ternary logic states
        refracted_wave = self.cpu.registers["ACC"]
        resolved_ternary = np.clip(np.round(refracted_wave), -1.0, 1.0)
        
        print(f"  🔍 [ABILITY 3: RESOLVE] -> Snapped analog waveform back into stable trinary logic states.")
        print(f"    Resolved Wave Vector: {resolved_ternary}")

        # -----------------------------------------------------------------
        # STEP 4: SELF-CORRECT (Homeostasis Equilibrium)
        # -----------------------------------------------------------------
        # Accept the shortfall deviation as a natural feature and balance the registers
        shortfall_deviation = np.abs(np.linalg.norm(resolved_ternary) - np.linalg.norm(incoming_wave))
        if shortfall_deviation > 0.0:
            print(f"  ⚖️ [ABILITY 4: SELF-CORRECT] -> Measured shortfall structural drift: {shortfall_deviation:.4f}")
            # Self-correcting balance calculation step inside the register state
            self.cpu.registers["ACC"] = resolved_ternary
            print("    [HOMEOSTASIS] Register fabric re-balanced successfully.")
        else:
            print("  ⚖️ [ABILITY 4: SELF-CORRECT] -> System state currently in flawless harmonic balance.")

        # -----------------------------------------------------------------
        # STEP 5: LEARN (Synaptic Adaptation)
        # -----------------------------------------------------------------
        # Dynamically adapt future thresholds based on the mathematical shape behavior of this run
        self.lambda_max = 0.95 * self.lambda_max + 0.05 * measured_lambda
        self.memory_log.append(measured_lambda)
        print(f"  🧠 [ABILITY 5: LEARN] -> Threshold adapted. Updated Lambda Max: {self.lambda_max:.4f}")
        print("  🚀 [EMERGENT PROCESS] Cycle complete. Process advanced to next cosmic state level.\n")
        
        return "CYCLE_SUCCESSFULLY_COMPLETED"

# =====================================================================
# HARDWARE FIELD VERIFICATION
# =====================================================================
if __name__ == "__main__":
    # Fire up the hardware engine and loop scheduler
    hardware_core = TrinaryProcessor()
    engine_loop = CosmicLoopController(hardware_core)
    
    # Define our test wave configurations
    valid_active_stream = np.array([1., 0., 1., 1., 0., -1., 0., 1., -1., 0., 0., 1., 1., 0.])
    pure_void_string    = np.array([-1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.])
    
    # Test Run 1: Active Wave processing through all 5 emergent steps
    engine_loop.process_wavefront_cycle("TelemetryStream", valid_active_stream)
    
    # Test Run 2: Void String demonstrating instant Transcendence / Early-Exit
    engine_loop.process_wavefront_cycle("NoiseMalwareAttack", pure_void_string)
      
