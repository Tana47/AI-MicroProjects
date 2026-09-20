# AI Assignment: Knowledge Graphs Exploration & Implementation

This repository contains an academic exploration of Knowledge Graphs (KGs) along with a hands-on Python demonstration utilizing network visualization libraries. 

## Repository Contents
* `build_kg.py` - Python script constructing an AI concepts Knowledge Graph.
* `knowledge_graph.png` - Visual output outputted by the program pipeline.

---

## 1. What is a Knowledge Graph?

A **Knowledge Graph** represents a network of real-world entities (objects, events, situations, or concepts) and illustrates the semantic relationships between them. Data is explicitly stored in the form of graph structures using **Triples**:

$$\text{(Subject)} \xrightarrow{\text{[Predicate]}} \text{(Object)}$$

### Key Benefits of Knowledge Graphs in AI
* **Semantic Context:** Helps machines understand data relationships, not just flat statistical patterns.
* **Explainability:** Provides an auditable trail for AI reasoning paths (Crucial for Neuro-symbolic AI architectures).
* **Data Integration:** Harmonizes disparate, heterogeneous structural silos into an un-siloed graph space.

---

## 2. Tooling Ecosystem Comparison

| Tool | Application Category | Ideal Use Case |
| :--- | :--- | :--- |
| **NetworkX** | Python Analysis Library | Mathematical network study, fast data structuring, prototyping. |
| **Neo4j** | Graph Database (NoSQL) | Massively scalable production systems requiring fast multi-hop queries. |
| **Protégé** | Ontology Application | Formal semantic data mapping and engineering logical schemas. |
| **RDFLib** | Python Library | Building strict W3C compliant Semantic Web / Linked Data graphs. |

---

## 3. Getting Started & Setup

### Prerequisites
Make sure you have Python 3.8+ installed along with the required libraries.

```bash
pip install networkx matplotlib