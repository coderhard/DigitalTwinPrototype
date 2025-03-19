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
```
DigitalTwinPrototype/
├───data/
│   ├───Digital_Shipyard_50k_With_Attacks.csv # Not included yet. Contact author for details.
│   └───Synthetic_Supply_Chain_Dataset.csv # Not included yet. Contact author for details.
├───src/
│   ├───agents/
│   │   ├───work_order_coordinator.py
│   │   ├───resource_allocator.py
│   │   └───... # Future other agent modules
│   ├───simulation/
│   │   └───simulation_engine.py
│   ├───utils/
│   │   └───data_loader.py
│   └───digtwin_streamlit_app.py
├───.gitignore
```

## LLM Agents

The prototype includes the following simulated LLM agents: 

* **Work Order Coordinator (WOC):** Task scheduling, resource allocation, and workflow management. 
* **Resource Allocator:** Allocates resources (cranes, AGVs) to work orders.
* **Inventory Manager (IM):** Inventory tracking and management. 
* **Predictive Maintenance Advisor (PMA):** Equipment monitoring and predictive maintenance. 

## Datasets

The prototype uses the following synthetic datasets: 

* **Digital Shipyard Dataset (Digital\_Shipyard\_50k\_With\_Attacks.csv):** Synthetic Operational events within a shipyard environment, for an LLM agent-enabled digital twin environment, including LLM agent actions, equipment status, and attack flags. 
* **Synthetic Supply Chain Dataset:** Container and shipment operations data, including operational events, attack events, and impact metrics. 

## Development Status

* [Describe the current state of the project. For example:]
    * "Basic simulation loop and data visualization are implemented."
    * "LLM agent logic for Work Order Coordinator is partially implemented."
    * "Further development is ongoing."

## Contributing

* [If you want others to contribute, add guidelines here. For example:]
    * "Pull requests are welcome. Please follow the project's coding conventions."

## License

* [Specify the license under which your project is released. For example:]
    * "This project is licensed under the MIT License."
