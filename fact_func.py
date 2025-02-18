import math

def gamma_fact(x):
    """
    Computes the Gamma function approximation for positive numbers.
    
    Parameters:
    x (float): The input value (should be positive and not a negative integer).
    
    Returns:
    float: The approximate Gamma function value.
    """
    if x <= 0 and x == int(x):  # Gamma is not defined for negative integers and zero
        raise ValueError("Gamma function is not defined for non-positive integers.")
    
    # Stirling's Approximation for large x: Γ(x) ≈ √(2π/x) * (x/e)^x
    if x > 1:
        return math.sqrt(2 * math.pi / x) * (x / math.e) ** x
    else:
        # Use recurrence relation: Γ(x) = Γ(x+1) / x
        return gamma_fact(x + 1) / x

# Example usage
num = 5.5
print(f"Gamma({num}) ≈ {gamma_fact(num)}")
