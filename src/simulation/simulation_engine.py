import pandas as pd
import logging
import time
from src.agents.work_order_coordinator import WorkOrderCoordinator
from src.agents.resource_allocator import ResourceAllocator
# Add import for other agents as you create them

class SimulationEngine:  # Correct indentation
    """
    Manages the simulation of the digital twin.
    """
    #def __init__(self, shipyard_data: pd.DataFrame, supply_chain_data: pd.DataFrame):  # Correct indentation
       
    def __init__(self, shipyard_data: pd.DataFrame, supply_chain_data: pd.DataFrame, time_step=1):
        """
        Initializes the SimulationEngine.
        """
        self.shipyard_data = shipyard_data
        self.supply_chain_data = supply_chain_data
        self.logger = logging.getLogger(__name__)
        self.agents = {}  # Dictionary to store agent instances
        self.time_step = time_step  # Simulation time step (e.g., in minutes, hours)
        self.current_time = 0  # Initialize simulation time
        self._initialize_agents()
        self.simulation_running = False
        self.event_queue = []  # Queue for storing events to be processed

    def _initialize_agents(self):
        """
        Initializes the agents in the simulation.
        """
        self.logger.info("Initializing agents...")
        # Create instances of your agents here
        # Example:
        self.agents['work_order_coordinator'] = WorkOrderCoordinator(self.shipyard_data, self.supply_chain_data)
        self.agents['resource_allocator'] = ResourceAllocator(self.shipyard_data)
        # Add more agents as needed

    def run_simulation_step(self):
        """
        Runs a single step of the simulation.
        """
        self.logger.info(f"Running simulation step... Current Time: {self.current_time}")
        # Orchestrate the actions of the agents in a single simulation step.
        # Example:
        if 'work_order_coordinator' in self.agents:
            self.agents['work_order_coordinator'].process_work_orders()
        if 'resource_allocator' in self.agents:
            self.agents['resource_allocator'].allocate_resources()
        # Add calls to other agent methods here
        # Update any global simulation state

        self._process_events()  # Process any events in the queue

        self.current_time += self.time_step  # Increment simulation time

    def get_simulation_data(self) -> dict:
        """
        Gets the current state of the simulation.
        """
        # Return the data needed to display the simulation state in Streamlit.
        # Example:
        return {
            'shipyard_data': self.shipyard_data,
            'supply_chain_data': self.supply_chain_data,
            'current_time': self.current_time,
            # Add more data as needed
        }

    def start_simulation(self):
        """
        Starts the simulation loop.
        """
        self.logger.info("Starting simulation...")
        self.simulation_running = True
        while self.simulation_running:
            self.run_simulation_step()
            # You might want to add a time.sleep() here to control the simulation speed
            # time.sleep(1)  # Pause for 1 second (adjust as needed)

    def stop_simulation(self):
        """
        Stops the simulation loop.
        """
        self.logger.info("Stopping simulation...")
        self.simulation_running = False

    def add_event(self, event_data: dict):
        """
        Adds an event to the event queue.
        """
        self.event_queue.append(event_data)
        self.logger.info(f"Event added to queue: {event_data}")

    def _process_events(self):
        """
        Processes events in the event queue.
        """
        events_to_remove = []
        for event in self.event_queue:
            event_time = event.get('time')  # Assuming events have a 'time' field
            if event_time is not None and event_time <= self.current_time:
                self.logger.info(f"Processing event: {event}")
                self._handle_event(event)  # Handle the event
                events_to_remove.append(event)

        # Remove processed events (iterate in reverse to avoid index issues)
        for event in reversed(events_to_remove):
            self.event_queue.remove(event)

    def _handle_event(self, event: dict):
        """
        Handles a specific event. This is where you'll define how different events
        affect the simulation.
        """
        event_type = event.get('type')

        if event_type == 'supply_chain_delay':
            # Example: Update supply chain data to reflect a delay
            delay_event_id = event.get('event_id')
            delay_reason = event.get('reason')
            self.logger.warning(f"Applying supply chain delay: {delay_reason} (Event ID: {delay_event_id})")
            # Implement logic to find the relevant supply chain event and update its status/impact
            # You'll likely need to iterate through self.supply_chain_data or use a lookup mechanism
        elif event_type == 'shipyard_equipment_failure':
            # Example: Update shipyard data to reflect equipment failure
            equipment_id = event.get('equipment_id')
            self.logger.error(f"Simulating equipment failure: {equipment_id}")
            # Implement logic to find the affected equipment and update its status
            # You'll likely need to iterate through self.shipyard_data or use a lookup
        # Add more event handling logic here for other event types
        else:
            self.logger.warning(f"Unhandled event type: {event_type}")

if __name__ == "__main__":
        # Configure logging (you might want to do this at the app level)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # Example Usage (You'll likely call this from your Streamlit app)
        # This is just for testing the module in isolation
        shipyard_data = pd.DataFrame({
            'work_order_id': [1, 2, 3],
            'task_status': ['Pending', 'In Progress', 'Pending'],
            'linked_shipyard_event': ['event1', None, 'event2']
        })
        supply_chain_data = pd.DataFrame({
            'linked_shipyard_event': ['event1', 'event2'],
            'delay_reason': ['Supply Delay', 'Equipment Failure']
        })
        engine = SimulationEngine(shipyard_data, supply_chain_data)
    
        # Add some events for testing
        engine.add_event({'type': 'supply_chain_delay', 'event_id': 'event1', 'reason': 'Severe Weather', 'time': 5})
        engine.add_event({'type': 'shipyard_equipment_failure', 'equipment_id': 'crane2', 'time': 10})
    
        engine.start_simulation()  # Start the simulation loop
        # You would likely have a mechanism in your Streamlit app to control the simulation
        # and retrieve data using engine.get_simulation_data()