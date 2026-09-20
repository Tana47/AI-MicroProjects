# Bayesian Network Modeling & Inference

This repository contains an exploration of Bayesian Networks for problem representation and exact inference, submitted as part of an Artificial Intelligence course assignment.

## Overview

Bayesian Networks are Probabilistic Graphical Models (PGMs) that represent a set of variables and their conditional dependencies via a Directed Acyclic Graph (DAG). 

This project implements Judea Pearl's classic **Alarm Network**. It models the probability of a burglary or earthquake triggering a home alarm, and the subsequent probabilities of two neighbors (John and Mary) calling to report the alarm.

### The Network Structure
* **Nodes:** Burglary, Earthquake, Alarm, JohnCalls, MaryCalls
* **Dependencies:** * Alarm depends on Burglary and Earthquake ($P(A \mid B, E)$).
    * JohnCalls depends on Alarm ($P(J \mid A)$).
    * MaryCalls depends on Alarm ($P(M \mid A)$).

## Tools Used

* **Python 3.x:** The primary programming language.
* **pgmpy:** A pure Python library for working with Probabilistic Graphical Models. It provides tools for defining the DAG, establishing Conditional Probability Tables (CPTs), and running exact inference algorithms.
* **Variable Elimination:** The specific exact inference algorithm used in this codebase to marginalize out unobserved variables and compute posterior probabilities.

## Installation & Setup

1. Clone this repository:
   ```bash
   git clone [https://github.com/yourusername/bayesian-network-inference-ai.git](https://github.com/yourusername/bayesian-network-inference-ai.git)
   cd bayesian-network-inference-ai