#!/usr/bin/env python3
"""
Simple Background Agent
A basic background agent that can run continuously and perform scheduled tasks.
"""

import time
import threading
import signal
import sys
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('agent.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

class BackgroundAgent:
    def __init__(self):
        self.running = False
        self.tasks = []
        self.logger = logging.getLogger(__name__)
        
    def add_task(self, task_func, interval=60):
        """Add a task to be executed at regular intervals"""
        self.tasks.append({
            'function': task_func,
            'interval': interval,
            'last_run': 0
        })
        
    def start(self):
        """Start the background agent"""
        self.running = True
        self.logger.info("Background agent started")
        
        # Set up signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
        
        # Start the main loop in a separate thread
        agent_thread = threading.Thread(target=self._run_loop)
        agent_thread.daemon = True
        agent_thread.start()
        
        return agent_thread
        
    def stop(self):
        """Stop the background agent"""
        self.running = False
        self.logger.info("Background agent stopped")
        
    def _signal_handler(self, signum, frame):
        """Handle shutdown signals"""
        self.logger.info(f"Received signal {signum}, shutting down...")
        self.stop()
        
    def _run_loop(self):
        """Main execution loop"""
        while self.running:
            current_time = time.time()
            
            for task in self.tasks:
                if current_time - task['last_run'] >= task['interval']:
                    try:
                        self.logger.info(f"Executing task: {task['function'].__name__}")
                        task['function']()
                        task['last_run'] = current_time
                    except Exception as e:
                        self.logger.error(f"Error executing task {task['function'].__name__}: {e}")
            
            time.sleep(1)  # Check every second

# Example tasks
def health_check():
    """Example health check task"""
    logging.info("Health check: Agent is running normally")

def system_status():
    """Example system status task"""
    import psutil
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    logging.info(f"System Status - CPU: {cpu_percent}%, Memory: {memory_percent}%")

def periodic_cleanup():
    """Example cleanup task"""
    logging.info("Performing periodic cleanup tasks")

if __name__ == "__main__":
    # Create and configure the agent
    agent = BackgroundAgent()
    
    # Add example tasks
    agent.add_task(health_check, interval=30)  # Every 30 seconds
    agent.add_task(system_status, interval=60)  # Every minute
    agent.add_task(periodic_cleanup, interval=300)  # Every 5 minutes
    
    # Start the agent
    agent_thread = agent.start()
    
    try:
        # Keep the main thread alive
        while agent.running:
            time.sleep(1)
    except KeyboardInterrupt:
        agent.stop()
        
    print("Background agent terminated") 