import numpy as np
import matplotlib.pyplot as plt

def plot_discrete_log_problem(g, p):
    """
    Generates a plot of the modular exponentiation: y = g^x mod p.
    
    Args:
        g (int): The base (generator).
        p (int): The prime modulus.
    """
    
    x_values = np.arange(0, 2*p - 1)
    
    # Calculate y = g^x mod p using np.vectorize and pow(g, int(x), p) 
    # The int(x) cast avoids TypeErrors with NumPy's internal types.
    mod_exp = np.vectorize(lambda x: pow(g, int(x), p)) 
    y_values = mod_exp(x_values)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(x_values, y_values, c='blue', marker='o', s=50)
    plt.plot(x_values, y_values, linestyle='--', color='lightgray', linewidth=1, zorder=-1)
    
    plt.title(f'Modular Exponentiation: y = {g}^x mod {p}', fontsize=14)
    plt.xlabel('x (Exponent)', fontsize=12)
    plt.ylabel(f'y = {g}^x mod {p}', fontsize=12)
    
    plt.xticks(x_values)
    plt.yticks(np.arange(0, p))
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    plt.show()

# --- Parameters ---
PRIME_MODULUS = 17 
GENERATOR = 3  

# Function call
plot_discrete_log_problem(GENERATOR, PRIME_MODULUS)