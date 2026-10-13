# Drone Mission Intelligence & Safety Validation

A Python project exploring input validation and safety-oriented checks for simulated drone mission data.

## Features

- Validates required mission fields.
- Checks battery values are between 0 and 100.
- Rejects negative wind-speed values.
- Validates GPS status as a Boolean.
- Reports missing or invalid inputs.
- Includes automated unit tests using Python's `unittest` framework.

## Project Structure

```text
drone-mission-intelligence/
├── mission_validator.py
├── test_mission_validator.py
├── README.md
└── .gitignore
```

## Requirements

- Python 3.9 or later
- No third-party packages required

## Run the Example

```bash
python mission_validator.py
```

## Run Tests

```bash
python -m unittest -v test_mission_validator
```

## Scope and Limitations

This project currently focuses on mission-input validation. It does not implement a complete autonomous drone system, live drone control, RAG, computer vision, or multi-agent orchestration.

It is an educational software project and must not be used as a substitute for real-world flight-safety systems.
