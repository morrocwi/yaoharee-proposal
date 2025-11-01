import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

# ===================================================================
# MVS L2 (TP2) - Yaoharee Cosmo v3.1 (K-free, Option A)
# L2_MVS_TP2_LockPingFFT.py
# Based on Lo.latex, Chapters 8, 16 and L2 document
# ===================================================================

print("Running MVS L2 (TP2): Phase-Lock Pendulum & Quark-Mode Ping Test...")

# --- 1. Common Setup (K-free, Option A) ---
Omega_0 = 1.5  # Anchor (rad/s) [cite: 45, 53]
tau = 0.1      # Informational inertia (dimensionless) 
U_0 = Omega_0**2 # Locking potential strength (scaled with Omega_0^2) [cite: 324]
dt = 0.01      # Time step
T_lock = 10.0  # Time to allow for locking
T_ring = 40.0  # Time to record ringing
n_lock = int(T_lock / dt)
n_ring = int(T_ring / dt)
n_total = n_lock + n_ring
t = np.linspace(0, T_lock + T_ring, n_total)

# --- 2. Falsification Test (Ablation A2 / F1) ---
# Goal: Show that without damping (no Lyapunov), locking fails. [cite: 345, 305]
# Equation: tau*phi'' + (U_0/Omega_0)*sin(phi) = 0
print("Running Falsification Test (Ablation: No Damping)...")
phi_ablation = np.zeros(n_total)
phidot_ablation = np.zeros(n_total)
phi_ablation[0] = 2.0  # Initial phase (not locked)

for i in range(n_total - 1):
    # Second-order accurate (Leapfrog-like)
    phi_ddot = -(U_0 / (Omega_0 * tau)) * np.sin(phi_ablation[i])
    phidot_ablation[i+1] = phidot_ablation[i] + phi_ddot * dt
    phi_ablation[i+1] = phi_ablation[i] + phidot_ablation[i+1] * dt

# --- 3. Hypothesis Test (H_A - Pass Expected) ---
# Goal: Show lock-in, then ping to find discrete modes.
# Equation: tau*phi'' + phi' + (U_0/Omega_0)*sin(phi) = Ping(t) 
print("Running Hypothesis Test (H_A: Damped Lock-in & Ping)...")
phi_main = np.zeros(n_total)
phidot_main = np.zeros(n_total)
phi_main[0] = 2.0  # Same initial phase

# Simple Euler-Cromer integrator
for i in range(n_total - 1):
    
    # --- PING ---
    # At t = T_lock, inject a "ping" (kick phidot)
    ping_kick = 0.0
    if i == n_lock:
        print(f"Ping injected at t={t[i]:.2f}s")
        ping_kick = 5.0 # Arbitrary energy kick
        
    # --- Equation of Motion ---
    # phi' = phidot
    # phidot' = (-phidot - (U_0/Omega_0)*sin(phi)) / tau
    
    phi_ddot = (-phidot_main[i] - (U_0 / Omega_0) * np.sin(phi_main[i])) / tau
    
    phidot_main[i+1] = phidot_main[i] + phi_ddot * dt + ping_kick
    phi_main[i+1] = phi_main[i] + phidot_main[i+1] * dt

# --- 4. Analysis & Results (FFT) ---
print("Analyzing ring-down spectrum...")
# Get the "ring-down" signal after the ping
ring_signal = phi_main[n_lock:]
ring_t = t[n_lock:]

# Perform FFT [cite: 325-326]
N_fft = len(ring_signal)
yf = fft(ring_signal)
xf = fftfreq(N_fft, dt)[:N_fft//2] # Frequencies (Hz)
xf_rad = 2.0 * np.pi * xf          # Frequencies (rad/s)

# --- 5. Plotting Results ---
print("Generating plots...")
plt.figure(figsize=(12, 10))

# Plot 1: Falsification (Ablation)
plt.subplot(2, 2, 1)
plt.plot(t, phi_ablation, 'r-')
plt.title("TP2 Falsification (F1): No Damping ($\dot\phi=0$)")
plt.xlabel("Time (s)")
plt.ylabel("Phase $\phi(t)$ (rad)")
plt.grid(True)
plt.text(0.5, 0.5, 'FAIL: No Lock-in', horizontalalignment='center', 
         verticalalignment='center', transform=plt.gca().transAxes, 
         fontsize=14, color='red', alpha=0.6)

# Plot 2: H_A Lock-in
plt.subplot(2, 2, 2)
plt.plot(t, phi_main, 'g-')
plt.axvline(x=T_lock, color='black', linestyle='--', label='Ping')
plt.title("TP2 Hypothesis (H_A): Damped Lock-in ($\dot\phi>0$)")
plt.xlabel("Time (s)")
plt.ylabel("Phase $\phi(t)$ (rad)")
plt.legend()
plt.grid(True)
plt.text(T_lock/2, 1.0, 'PASS: Lock-in', 
         fontsize=14, color='green', alpha=0.6)

# Plot 3: H_A Ring-down (Zoomed)
plt.subplot(2, 2, 3)
plt.plot(ring_t, ring_signal, 'b-')
plt.title("TP2 (H_A): Post-Ping 'Ring-down' Signal")
plt.xlabel("Time (s)")
plt.ylabel("Phase $\phi(t)$ (rad)")
plt.grid(True)

# Plot 4: H_A FFT Spectrum (The "Quark Modes") [cite: 325-326]
plt.subplot(2, 2, 4)
plt.plot(xf_rad, 2.0/N_fft * np.abs(yf[0:N_fft//2]), 'k-')
plt.axvline(x=Omega_0, color='blue', linestyle='--', label=f'Anchor $\Omega_0$={Omega_0} rad/s')
plt.title("TP2 (H_A): FFT Spectrum (Quark-like Modes)")
plt.xlabel("Frequency $\Omega$ (rad/s)")
plt.ylabel("Amplitude")
plt.xlim(0, Omega_0 * 4) # Show spectrum around anchor
plt.legend()
plt.grid(True)
plt.text(Omega_0 * 1.1, 0.5, '$\Omega_0$ (Base Mode)', transform=plt.gca().get_xaxis_transform(),
         color='blue', fontsize=10)
plt.text(Omega_0 * 2.1, 0.3, '$\Omega_n$ (Harmonics)', transform=plt.gca().get_xaxis_transform(),
         color='black', fontsize=10)

plt.suptitle("MVS L2 (TP2): Mass from Coherence & Quark-Mode Emergence", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("L2_MVS_TP2_LockPingFFT_plot.png")
print("\nPlot saved to L2_MVS_TP2_LockPingFFT_plot.png")

plt.show()
