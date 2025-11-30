# Function to mimic an Auth Decision
def check_access(user_role, risk_score):
    """
    Decides if a user gets access based on role and risk.
    """
    print(f"Checking access for: {user_role} (Risk Score: {risk_score})")

    # LOGIC GATE: If High Risk, always block
    if risk_score > 80:
        return "DENIED: Risk too high (MFA Required)"
    
    # LOGIC GATE: Admin access
    if user_role == "admin":
        return "GRANTED: Full Access"
    
    # LOGIC GATE: Standard user
    elif user_role == "user":
        return "GRANTED: Standard Access"
    
    # LOGIC GATE: Unknown
    else:
        return "DENIED: Invalid Role"

# --- THE EXECUTION ---
# Let's test our logic with different scenarios
print("--- SCENARIO 1 ---")
result1 = check_access("admin", 10)
print("Result:", result1)

print("\n--- SCENARIO 2 ---")
result2 = check_access("user", 95)
print("Result:", result2)