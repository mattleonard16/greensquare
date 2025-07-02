# GreenSquare Background Agent

A simple, extensible background agent that can run continuously and execute scheduled tasks.

## Features

- Continuous background execution
- Configurable task scheduling
- Graceful shutdown handling
- Comprehensive logging
- Error handling and recovery
- Thread-safe operation

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the background agent:
```bash
python background_agent.py
```

The agent will start and begin executing the configured tasks at their specified intervals.

## Configuration

The script includes example tasks:
- **Health Check**: Runs every 30 seconds
- **System Status**: Reports CPU and memory usage every minute
- **Periodic Cleanup**: Runs cleanup tasks every 5 minutes

### Adding Custom Tasks

To add your own tasks, create a function and add it to the agent:

```python
def my_custom_task():
    # Your task logic here
    print("Executing custom task")

# Add to agent with desired interval (in seconds)
agent.add_task(my_custom_task, interval=120)  # Every 2 minutes
```

## Logs

The agent logs to both:
- Console output (stdout)
- Log file (`agent.log`)

## Stopping the Agent

The agent handles graceful shutdown via:
- Ctrl+C (SIGINT)
- Kill signals (SIGTERM)

## Extending the Agent

The `BackgroundAgent` class is designed to be easily extended. You can:
- Add more sophisticated task scheduling
- Implement task priorities
- Add configuration file support
- Integrate with external systems
- Add monitoring and alerting capabilities 