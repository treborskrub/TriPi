import numpy as np
import matplotlib.pyplot as plt

# Set academic plotting style parameters for professional publication look
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 1.2

# Define time-steps and system threshold ceilings
time_steps = np.arange(0, 10, 1)
lambda_max = 1.35
absolute_limit = 1.0

# Generate simulated Phase Amplitude Expansion (λ) trajectories
# 1. Telemetry Stream Alpha: Natural cosmic wave fluctuation within bounds
telemetry_lambda = 1.1306 + 0.08 * np.sin(time_steps * 1.2)

# 2. Exploit Vector Beta: Violates boundary conditions on Cycle 2, triggering perimeter deflection
exploit_lambda = np.array([0.95, 2.74, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

# 3. Gapped Thread Gamma: Clears boundary shield, parks in Shortfall Vault on Cycle 3, undergoes linear entropy decay
gapped_lambda = np.array([1.02, 1.15, 0.50, 0.42, 0.35, 0.28, 0.21, 0.14, 0.07, 0.00])

# Create multi-panel sub-plot visualization fabric
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7), sharex=True, gridspec_kw={'height_ratios': [1.2, 1]})
fig.suptitle('Figure 2: Real-Time Wavefront Triage Pipelines & Phase Separation Matrix', 
             fontsize=12, fontweight='bold', color='#111111', y=0.96)

# =====================================================================
# PANEL 1: AMPLITUDE EXPANSION RATIO (λ) TRACKS & CEILINGS
# =====================================================================
# Plot standard limit boundaries
ax1.axhline(lambda_max, color='#B22222', linestyle='--', linewidth=1.5, label=r'Critical Sieve Threshold Limit ($\lambda_{max} = 1.35$)')
ax1.axhline(absolute_limit, color='gray', linestyle=':', linewidth=1.2, label='Structural Invariant Ground Line (1.00)')

# Plot individual process streams
ax1.plot(time_steps, telemetry_lambda, color='#008080', marker='o', markersize=6, linewidth=2, 
         label='TelemetryStream_Alpha (Track: ACTIVE_SCHEDULE)')
ax1.plot(time_steps, exploit_lambda, color='#D9383A', marker='x', markersize=7, linewidth=2, linestyle='-.',
         label='ExploitVector_Beta (Track: VOID_PURGED)')
ax1.plot(time_steps, gapped_lambda, color='#D4AF37', marker='s', markersize=5, linewidth=2, linestyle=':',
         label='GappedThread_Gamma (Track: SHORTFALL_STANDBY)')

# Structural callout highlights for milestones
ax1.annotate('Perimeter Boundary Shield\n[03. DEFLECT] Breach Triggered', xy=(1, 2.74), xytext=(2.2, 2.5),
             arrowprops=dict(facecolor='#D9383A', arrowstyle='->', lw=1.2), fontsize=9, color='#D9383A', bbox=dict(boxstyle='square,pad=0.3', fc='#FFF0F0', ec='#D9383A', lw=0.5))

ax1.annotate('Data Gaps Identified\n[06. BRIDGE] Vault Parking', xy=(2, 0.50), xytext=(3.5, 0.70),
             arrowprops=dict(facecolor='#D4AF37', arrowstyle='->', lw=1.2), fontsize=9, color='#B8860B', bbox=dict(boxstyle='square,pad=0.3', fc='#FFFDF0', ec='#D4AF37', lw=0.5))

ax1.annotate('[09. ATTENUATE]\nPassive Entropy Decay', xy=(5, 0.28), xytext=(6.2, 0.45),
             arrowprops=dict(facecolor='dimgray', arrowstyle='->', lw=1.2), fontsize=9, color='dimgray')

# Panel styling
ax1.set_ylabel(r'Amplitude Expansion Ratio ($\lambda$)', fontweight='bold')
ax1.set_ylim(-0.1, 3.2)
ax1.grid(True, alpha=0.25, linestyle='--')
ax1.legend(loc='upper right', frameon=True, facecolor='#F8F9FA', edgecolor='#E5E5E5', fontsize=9)

# =====================================================================
# PANEL 2: MATRIC STATE SCHEDULER QUEUE CHANNELS
# =====================================================================
# Map processes to discrete queue heights over time-ticks
# Heights: 2 = Active Queue, 1 = Shortfall Vault, 0 = Void Purge / Ground 0V
telemetry_queue = np.full_like(time_steps, 2)

exploit_queue = np.array([2, 0, 0, 0, 0, 0, 0, 0, 0, 0])

gapped_queue = np.array([2, 2, 1, 1, 1, 1, 1, 1, 0, 0])

# Plot horizontal step progressions for queues
ax2.step(time_steps, telemetry_queue, where='mid', color='#008080', linewidth=2.5, alpha=0.85)
ax2.step(time_steps, exploit_queue, where='mid', color='#D9383A', linewidth=2.5, alpha=0.85)
ax2.step(time_steps, gapped_queue, where='mid', color='#D4AF37', linewidth=2.5, alpha=0.85)

# Label queue state tiers on the Y-Axis
ax2.set_yticks([0, 1, 2])
ax2.set_yticklabels(['VOID_PURGED\n(0V Ground)', 'SHORTFALL_STANDBY\n(Vault Fixed)', 'ACTIVE_SCHEDULE\n(T-CPU Matrix)'], 
                    fontweight='bold', fontsize=9)

# Panel styling
ax2.set_xlabel('System Clock Sieve Cycles ($n$)', fontweight='bold')
ax2.set_ylabel('OS Scheduler Track', fontweight='bold')
ax2.set_xlim(-0.2, 9.2)
ax2.set_ylim(-0.5, 2.5)
ax2.grid(True, alpha=0.2, linestyle=':')

# Apply subtle section backgrounds to demarcate queues visually
ax2.axhspan(1.5, 2.5, color='#E6F2F2', alpha=0.3)
ax2.axhspan(0.5, 1.5, color='#FFFDF0', alpha=0.3)
ax2.axhspan(-0.5, 0.5, color='#FFF0F0', alpha=0.3)

plt.tight_layout()
plt.subplots_adjust(top=0.90)

# Display the final chart object canvas
plt.show()
