<<<<<<< HEAD
## Acknowledgments

The sensor pattern was designed by Prof. Sonia Roberts (Wesleyan University).  
Knitout code implementation by Marouan El-Asery.

This code uses the [Knitout](https://github.com/textiles-lab/knitout) format developed by the CMU Textiles Lab.


=======
# Knitted Soft Sensor: Resistive Pressure Sensing

**Smart Textiles | Soft Robotics | Knitout**

This project explores the fabrication and control of machine-knitted resistive pressure sensors for soft robotic applications. By integrating conductive yarns into specific knit structures, we create textile interfaces that respond to deformation with measurable resistance changes.

## Technical Implementation

- **Material & Structure**: Uses silver-plated conductive nylon plated with elastomeric yarn to create a stretchable, conductive mesh.
- **Sensing Mechanism**: Piezoresistive behavior where resistance decreases as the knit structure is compressed or stretched, increasing contact points between conductive loops.
- **Fabrication**: Manufactured on a Shima Seiki SWG091N2 industrial flat-bed knitting machine using low-level `knitout` instructions for precise carrier control.

## Usage

This repository contains the `knitout` generation scripts and the raw sensor data analysis tools.

```python
# Example: analyze_sensor_data.py
import pandas as pd
import matplotlib.pyplot as plt

# Load resistance data
data = pd.read_csv('sensor_log.csv')
plt.plot(data['time'], data['resistance'])
plt.title('Step Response: 50% Strain')
plt.show()
```

---
*Part of the Computational Textiles portfolio.*
>>>>>>> 63d6160 (Initial commit for Knitted Soft Sensor)
