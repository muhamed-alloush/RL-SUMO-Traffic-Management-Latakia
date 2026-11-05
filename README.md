# RL-SUMO-Traffic-Management-Latakia

A Reinforcement Learning-based traffic light control system designed to optimize traffic flow, reduce congestion, and minimize waiting times during peak hours. This project is applied to the real-world road network map of the Al-Ziraa neighborhood in Latakia.

## 📌 Project Overview
Urban traffic congestion is a critical issue in modern cities. This project implements an intelligent traffic management system using SUMO (Simulation of Urban MObility) integrated with Reinforcement Learning (RL) algorithms via Python. Instead of traditional fixed-timing traffic lights, the agent learns optimal signal policies through environment interactions to dynamically adapt to real-time traffic demands.

## 🚀 Key Features
* Real-World Mapping: Utilizes actual geographic and road network data from the Al-Ziraa neighborhood in Latakia, extracted via OpenStreetMap (OSM).
* Traffic Simulation: Simulates realistic vehicle movements, routing, and peak-hour traffic volumes using SUMO.
* Reinforcement Learning Control: Employs Python scripts (run_3.py, test.py) to train an RL agent to manage intersection signals intelligently.
* Performance Optimization: Focuses on minimizing vehicle waiting times, reducing queue lengths, and alleviating overall traffic congestion.

## 🛠️ Project Structure
* osm.net.xml - The road network layout and infrastructure map of Al-Ziraa.
* myproject.sumocfg - Main configuration file for running the SUMO simulation.
* run_3.py - Core Python script for training and executing the Reinforcement Learning model.
* test.py - Evaluation script to test the performance of the trained agent.
* run.bat - Batch script for quick execution.

## ⚙️ How to Run
1. Ensure you have SUMO (Simulation of Urban MObility) and Python installed on your system.
2. Clone this repository:
   `bash
   git clone [https://github.com/your-username/RL-SUMO-Traffic-Management-Latakia.git](https://github.com/your-username/RL-SUMO-Traffic-Management-Latakia.git)
3. Open the project directory and run the simulation using the provided configuration or Python scripts.

## 🎯 Future Improvements
* Integrating advanced Deep Q-Networks (DQN) for multi-intersection coordination.
* Expanding the simulation scale to cover broader districts in Latakia.
