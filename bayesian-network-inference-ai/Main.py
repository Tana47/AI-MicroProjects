"""
Bayesian Network Implementation: The Alarm Problem
Requires: pip install pgmpy
"""

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def main():
    print("--- Bayesian Network: Modeling & Representation ---")
    
    # 1. Define the Network Structure (Directed Acyclic Graph)
    # Edges indicate conditional dependence: Burglary -> Alarm <- Earthquake
    model = BayesianNetwork([
        ('Burglary', 'Alarm'),
        ('Earthquake', 'Alarm'),
        ('Alarm', 'JohnCalls'),
        ('Alarm', 'MaryCalls')
    ])

    # 2. Define the Conditional Probability Distributions (CPTs)
    
    # P(Burglary)
    cpd_burglary = TabularCPD(variable='Burglary', variable_card=2, values=[[0.999], [0.001]], state_names={'Burglary': ['False', 'True']})
    
    # P(Earthquake)
    cpd_earthquake = TabularCPD(variable='Earthquake', variable_card=2, values=[[0.998], [0.002]], state_names={'Earthquake': ['False', 'True']})

    # P(Alarm | Burglary, Earthquake)
    # The values array maps to: [P(Alarm=False), P(Alarm=True)]
    # Columns represent combinations of evidence: (B=F,E=F), (B=F,E=T), (B=T,E=F), (B=T,E=T)
    cpd_alarm = TabularCPD(
        variable='Alarm', variable_card=2,
        values=[
            [0.999, 0.71, 0.06, 0.05], # Alarm = False
            [0.001, 0.29, 0.94, 0.95]  # Alarm = True
        ],
        evidence=['Burglary', 'Earthquake'],
        evidence_card=[2, 2],
        state_names={'Alarm': ['False', 'True'], 'Burglary': ['False', 'True'], 'Earthquake': ['False', 'True']}
    )

    # P(JohnCalls | Alarm)
    cpd_john = TabularCPD(
        variable='JohnCalls', variable_card=2,
        values=[[0.95, 0.10], [0.05, 0.90]],
        evidence=['Alarm'], evidence_card=[2],
        state_names={'JohnCalls': ['False', 'True'], 'Alarm': ['False', 'True']}
    )

    # P(MaryCalls | Alarm)
    cpd_mary = TabularCPD(
        variable='MaryCalls', variable_card=2,
        values=[[0.99, 0.30], [0.01, 0.70]],
        evidence=['Alarm'], evidence_card=[2],
        state_names={'MaryCalls': ['False', 'True'], 'Alarm': ['False', 'True']}
    )

    # 3. Add CPTs to the model and validate
    model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_john, cpd_mary)
    
    if model.check_model():
        print("Model structure and CPTs are valid and successfully constructed!\n")

    # 4. Inferencing using Variable Elimination
    print("--- Bayesian Inference Execution ---")
    infer = VariableElimination(model)

    # Query 1: What is the probability of a burglary if John calls?
    print("\nQuery 1: P(Burglary | JohnCalls = True)")
    q1 = infer.query(variables=['Burglary'], evidence={'JohnCalls': 'True'})
    print(q1)

    # Query 2: What is the probability of a burglary if both John and Mary call?
    print("\nQuery 2: P(Burglary | JohnCalls = True, MaryCalls = True)")
    q2 = infer.query(variables=['Burglary'], evidence={'JohnCalls': 'True', 'MaryCalls': 'True'})
    print(q2)

    # Query 3: Intercausal Reasoning (Explaining Away)
    # What if John and Mary call, but we KNOW an earthquake happened?
    print("\nQuery 3: P(Burglary | JohnCalls = True, MaryCalls = True, Earthquake = True)")
    q3 = infer.query(variables=['Burglary'], evidence={'JohnCalls': 'True', 'MaryCalls': 'True', 'Earthquake': 'True'})
    print(q3)
    print("Notice how the probability of a burglary drops drastically in Query 3. The earthquake 'explains away' the alarm.")

if __name__ == '__main__':
    main()