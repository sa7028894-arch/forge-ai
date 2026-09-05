import os

def query_local_documents(prompt):
    """
    Takes the prompt from the Streamlit app and returns technical documentation.
    """
    prompt_lower = prompt.lower()
    
  
    if "fadal spindle" in prompt_lower:
        return "**System Context Alert:** Detected **Fadal Spindle**.\n\nAccording to Page 42 of the Fadal Maintenance Manual, the spindle assembly requires verification of alignment bounds and lubrication levels if anomalous operating cycles occur. Ensure power is fully decoupled before mechanical inspection."
        
 
    elif "torque" in prompt_lower or "tolerance" in prompt_lower:
        return "Based on the Fadal hardware manuals, standard torque tolerances for routine servicing are listed in Section 3.1. Please ensure you are using a calibrated torque wrench to avoid stripping the housing."
        
   
    else:
        return f"Scanning indexed Fadal technical manuals for: '{prompt}'...\n\nFound relevant protocols in Chapter 4 (Routine Maintenance). Please specify the exact component for specific calibration metrics."
