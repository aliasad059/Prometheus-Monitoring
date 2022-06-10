# Prometheus-Monitoring-System
The final project of the Computer Network course at Amirkabir University of Technology. The project is the implementation of a monitoring Prometheus metric client that receives metrics from different agents and merge them into Prometheus metrics and exposes them for Prometheus Scraper.

## Requirements
```
prometheus-client
psutil
```

## How to use it?
- To run this project, you should run the server first.
```bash
python3 server.py
```

- Then in a separate shell, run an agent to extract metrics from the system and send them to the server.

Note: you can also run multiple agents, each of them can be connected to the server in a separate thread
```bash
python3 agent.py
```

## Metrics
### CPU
- CPU's current frequency
### Memory
- Memory's current available volume
### Disk
- Percentage of available disk space
### Battery
- Percentage of Battery Power

## Links
You can access my project report [here](https://docs.google.com/document/d/1sF050nCwx8SHX9RulWxx8VwDIoIhQy4XMtqrdF99FqI)(in Persian).
