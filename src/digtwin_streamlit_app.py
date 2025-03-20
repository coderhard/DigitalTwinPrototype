import streamlit as st
import pandas as pd
from utils.data_loader import load_dataset
import sys
import os 
# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

print("sys.path:", sys.path)

from src.simulation.simulation_engine import SimulationEngine

def main():
    """
    Main function to run the Streamlit application.
    """
    st.title("Digital Twin Prototype: Supply Chain Simulation")

    # Load Datasets
    shipyard_data = load_dataset("Digital_Shipyard_50k_With_Attacks.csv")
    supply_chain_data = load_dataset("Supply_Chain_50k_With_Attacks.csv")

    if shipyard_data is None or supply_chain_data is None:
        st.error("Failed to load datasets. Please check the data files.")
        return

    # Initialize Simulation Engine
    simulation_engine = SimulationEngine(shipyard_data, supply_chain_data)

    # --- Dashboard ---
    st.header("Dashboard")
    #st.write("This is where the dashboard will go.")

    if st.button("Run Simulation Step"):
        simulation_engine.run_simulation_step()

        # --- Retrieve and Display Simulation Data ---
        simulation_data = simulation_engine.get_simulation_data()
        updated_shipyard_data = simulation_data['shipyard_data']
        updated_supply_chain_data = simulation_data['supply_chain_data']
        current_time = simulation_data['current_time']

        st.write(f"Current Simulation Time: {current_time}")
        
        #After running a simulation step, display the updated shipyard_data
        st.subheader("Updated Shipyard Data")
        st.dataframe(updated_shipyard_data.head())

        #After running a simulation step, display the updated supply_chain_data
        st.subheader("Updated Supply Chain Data")
        st.dataframe(updated_supply_chain_data.head())

    else:
        st.write("Press the button to run a simulation step.")

    # --- Agent Interaction Panel ---
    st.header("Agent Interaction Panel")
    st.write("This is where the agent interaction panel will go.")

    # --- Settings/Controls ---
    st.header("Settings/Controls")
    st.write("This is where the settings/controls will go.")
        

if __name__ == "__main__":
    main()