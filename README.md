# UAV Orientation Estimation via Magnetometer-Informed PDE Modeling

A standalone Python implementation of a rotation matrix evolution framework on the SO(3) manifold for estimating UAV orientation using real-time magnetometer data. This work was carried out independently as part of my contribution to the UAV Tracking & Communication Lab in 2025.

## Overview

This project implements a mathematically rigorous model for estimating the 3D orientation of a UAV using data from a 3-axis magnetometer (MLX90392). The model reframes orientation estimation as a partial differential equation (PDE)-driven process on SO(3), allowing for extensibility into optimization, stochastic analysis, and geometric control.

## My Contribution

This repository contains only my individual contributions and experiments, completed during my time at the UAV Tracking & Communication Lab. All work here:

- Was developed independently
- Does not contain any proprietary or team-sensitive code or data
- Serves as a personal research artifact demonstrating:

  - Applied Lie Group Theory
  - PDE-constrained estimation
  - Serial data parsing and sensor modeling
  - Orientation tracking algorithms

## Getting Started

### Prerequisites

- Python 3.8+
- ESP32 S2 Lolin Mini connected to an MLX90392 magnetometer
- Required packages:

```bash
pip install numpy pandas scipy pyserial
```

## Usage

### To run with live data:

1. Upload Arduino code to stream MLX90392 data over Serial
2. Edit `main.py` to set the correct `COM` port
3. Run:

```bash
python main.py
```

### To run simulation from stored magnetometer data:

1. Place your magnetometer CSV log as `raw.csv` in the root folder
2. Run:

```bash
python simulate_from_data.py
```

## About the Original Lab Work

This project emerged as part of my work at the UAV Tracking & Communication Lab (2025).
The version here isolates and refactors that research for broader scientific and technical exploration, particularly in the context of PDE-based estimation and SO(3) manifold modeling.

## License

This project is licensed under the MIT License.

## Citation

```bibtex
@misc{srekhi2025uavpde,
  author       = {Simar Rekhi},
  title        = {UAV Orientation Estimation via Magnetometer-Informed PDE Modeling},
  year         = {2025},
  note         = {Standalone contribution at UAV Tracking & Communication Lab},
  howpublished = {\url{https://github.com/simar-rekhi/uav-field-modeling}}
}
```
