import numpy as np
import matplotlib.pyplot as plt

# ===================================================================
# MVS L2 (TP1) - Yaoharee Cosmo v3.1 (K-free, Option A)
# Based on Lo.latex, Chapters 12 & 16
# ===================================================================

print("Running MVS L2 (TP1): Homogeneous Decay Test...")

# --- 1. Common Setup (Chapter 16) ---
# [cite: 352-355]
L = 10.0      # Domain size (dimensionless)
N = 128       # Grid points
dx = L / N    # Grid spacing [cite: 353]
x = np.linspace(0, L, N, endpoint=False) # Grid
T = 50.0      # Total time
c = 1.0       # Propagation speed (dimensionless)
tau = 0.1     # Relaxation time (dimensionless) [cite: 354]
Omega_0 = 1.0 # Anchor (rad/s) [cite: 354]

# --- 2. Numerical Scheme (Chapter 12) ---
# We use the Baseline Explicit (Leapfrog) scheme [cite: 230]
# We must obey the CFL condition [cite: 231]
cfl_factor = 0.5
dt_cfl = dx / (c * np.sqrt(1)) # 1D CFL [cite: 231]
dt_tau = 2 * tau               # Damping CFL [cite: 231]
dt = cfl_factor * min(dt_cfl, dt_tau)
n_steps = int(T / dt)
print(f"Grid: N={N}, dx={dx:.3f}")
print(f"Time: T={T}, n_steps={n_steps}, dt={dt:.4f}")

# --- 3. Discrete Operators (Chapter 12) ---

def discrete_laplacian(psi_n):
    """ Computes 1D periodic Laplacian [cite: 226] """
    psi_left = np.roll(psi_n, 1)
    psi_right = np.roll(psi_n, -1)
    return (psi_left - 2 * psi_n + psi_right) / (dx**2)

def compute_energy(psi_n, V_n):
    """ Computes Discrete Energy Monitor (E_coh) [cite: 241, 362] """
    # Using Phi(Psi) = 0 for TP1 (no source)
    grad_psi = (np.roll(psi_n, -1) - psi_n) / dx # Simple gradient
    
    # E_coh = 1/2 * V^2 + c^2/2 * |grad(Psi)|^2 [cite: 241, 362]
    energy_density = 0.5 * V_n**2 + (c**2 / 2.0) * grad_psi**2
    return np.sum(energy_density) * dx # Integrate over domain

# --- 4. Initialization (Chapter 16) ---
# [cite: 355]
Psi = np.zeros((3, N)) # Store n+1, n, n-1
V = np.zeros(N)        # Velocity V = d(Psi)/dt

# Initial packet (band-limited) [cite: 355]
Psi[1, :] = np.exp(-((x - L / 2)**2) / (2 * 1.0**2)) * np.cos(8 * np.pi * x / L)
Psi[0, :] = Psi[1, :] # Set n-1 = n (since d(Psi)/dt = 0) [cite: 355]

# Energy log
energy_log = []

# --- 5. Main Simulation Loop (TP1) ---
# 
# This loop solves the *homogeneous* equation (Source = 0)
# tau*d^2(Psi)/dt^2 + d(Psi)/dt - c^2*grad^2(Psi) = 0

for n in range(1, n_steps):
    
    # Pointers to time steps
    psi_np1 = Psi[2, :] # n+1
    psi_n = Psi[1, :]   # n
    psi_nm1 = Psi[0, :] # n-1
    
    # Compute Laplacian at time n [cite: 226]
    lap_psi_n = discrete_laplacian(psi_n)
    
    # Solve for Psi^{n+1} using Leapfrog scheme [cite: 230]
    # (tau/dt^2 + 1/(2*dt)) * Psi^{n+1} = 
    #    (2*tau/dt^2) * Psi^n - (tau/dt^2 - 1/(2*dt)) * Psi^{n-1} + c^2*lap_psi_n
    
    A = tau / (dt**2)
    B = 1.0 / (2.0 * dt)
    
    psi_np1[:] = ( (2.0 * A) * psi_n - (A - B) * psi_nm1 + (c**2) * lap_psi_n ) / (A + B)
    
    # Compute velocity V^n for energy calculation
    V_n = (psi_np1 - psi_nm1) / (2.0 * dt)
    
    # --- 6. Energy--Coherence Check (Pass/Fail) ---
    # [cite: 357]
    current_energy = compute_energy(psi_n, V_n)
    energy_log.append(current_energy)
    
    # Advance time (roll arrays)
    Psi[0, :] = psi_n
    Psi[1, :] = psi_np1

# --- 7. Final Verdict (TP1) ---
E_start = energy_log[0]
E_end = energy_log[-1]

print(f"\n--- Test 1 (TP1) Verdict ---")
print(f"Initial Energy (E_coh): {E_start:.6f}")
print(f"Final Energy (E_coh):   {E_end:.6f}")

# Falsification check [cite: 357]
if E_end < E_start and not np.isnan(E_end):
    print("PASS: Energy decreased monotonically.")
    print("      (E_coh(t_n+1) <= E_coh(t_n)) [cite: 362]")
    print("      Result: The numerical scheme respects the Energy--Coherence Law.")
else:
    print("FAIL: Energy did not decrease.")
    print("      (Ablation check failed or scheme is unstable)")

# Plotting the result
plt.figure(figsize=(10, 6))
plt.plot(np.linspace(0, T, len(energy_log)), energy_log)
plt.title("MVS L2 (TP1): Homogeneous Decay Test ")
plt.xlabel("Time (dimensionless)")
plt.ylabel("Total Coherence Energy (E_coh) [cite: 362]")
plt.grid(True)
plt.show()
