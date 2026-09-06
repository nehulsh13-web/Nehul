import math

def calculate_trig_values(degrees):
   
    radians = math.radians(degrees)
    
    
    sine_val = math.sin(radians)
    cosine_val = math.cos(radians)
    
    
    if round(cosine_val, 10) == 0:
        tangent_val = "Undefined (Asymptote)"
    else:
        tangent_val = math.tan(radians)

  
    print(f"--- Trigonometric Values for {degrees}° ---")
    print(f"Angle in Radians: {radians:.4f} rad")
    print(f"Sin({degrees}°) = {sine_val:.4f}")
    print(f"Cos({degrees}°) = {cosine_val:.4f}")
    
    if isinstance(tangent_val, float):
        print(f"Tan({degrees}°) = {tangent_val:.4f}")
    else:
        print(f"Tan({degrees}°) = {tangent_val}")

calculate_trig_values(45)
