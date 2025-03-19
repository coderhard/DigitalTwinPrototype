# Digital Twin Prototype: Supply Chain Simulation
**Author**: CoderHard

## Overview

This project is a Digital Twin Prototype for simulating supply chain operations. It uses Streamlit for the web interface, pandas for data manipulation, and various other libraries for data visualization and processing. The prototype includes functionalities for loading datasets, running simulations, and allocating resources such as cranes, AGVs, and forklifts to work orders.

## Features

- **Streamlit Web Interface**: Interactive web application for visualizing and interacting with the simulation.
- **Data Loading**: Load and preprocess datasets for the digital shipyard and synthetic supply chain.
- **Simulation Engine**: Run simulation steps and update the status of work orders.
- **Resource Allocation**: Allocate resources (cranes, AGVs, forklifts) to work orders based on availability and dependencies.
- **Logging**: Detailed logging of simulation steps and resource allocation.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/digital-twin-prototype.git
    cd digital-twin-prototype
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv .venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        .venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source .venv/bin/activate
        ```

4. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit application**:
    ```sh
    streamlit run src/digtwin_streamlit_app.py
    ```

2. **Open the application in your browser**:
    - Local URL: `http://localhost:8501`
    - Network URL: `http://<your-ip-address>:8501`

## Project Structure
