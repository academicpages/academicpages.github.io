import numpy as np

# Total simulations for Monte Carlo (10,000 iterations, illustrative)
simulations = 10000  

# ----- QUALITY RISK -----
# Simulate combined quality failure probability per year (2–4%)  
# Accounts for AI inspection, conditional detection failure, and mitigation
quality_failure = np.random.rand(simulations) < np.random.uniform(0.02, 0.04, simulations)

# ----- SUPPLY CHAIN RISK -----
# Base disruption probabilities for transport delays (15–25%) and supplier failures (10–20%)
transport_issue = np.random.rand(simulations) < np.random.uniform(0.15, 0.25, simulations)
supplier_issue = np.random.rand(simulations) < np.random.uniform(0.10, 0.20, simulations)

# Conditional stock-out occurs if upstream issues arise (5–10%), reflecting mitigation measures
conditional_stockout = np.random.rand(simulations) < np.random.uniform(0.05, 0.10, simulations)
stockout_event = (transport_issue | supplier_issue) & conditional_stockout

# Materialized impact: only a subset of disruptions affects operations (35–50%), due to buffers, diversification, and AI planning
materialized_impact = np.random.rand(simulations) < np.random.uniform(0.35, 0.50, simulations)
supply_disruption = (transport_issue | supplier_issue | stockout_event) & materialized_impact

# ----- DIGITAL AVAILABILITY RISK -----
# Simulate system outages (1–3%) and short data-loss events (0.1–1%)
system_failure = np.random.rand(simulations) < np.random.uniform(0.01, 0.03, simulations)
minor_data_loss = np.random.rand(simulations) < np.random.uniform(0.001, 0.01, simulations)
digital_disruption = system_failure | minor_data_loss

# ----- OVERALL OPERATIONAL DISRUPTION -----
# Operational escalation factor (40–60%) models that not all events result in major disruptions
escalation_factor = np.random.rand(simulations) < np.random.uniform(0.40, 0.60, simulations)
overall_disruption = (quality_failure | supply_disruption | digital_disruption) & escalation_factor

# ----- RESULTS -----
print("Yearly Quality Degradation Probability:", round(quality_failure.mean()*100,2), "%")
print("Yearly Supply Chain Disruption Probability:", round(supply_disruption.mean()*100,2), "%")
print("Yearly Digital Disruption Probability:", round(digital_disruption.mean()*100,2), "%")
print("Overall Operational Disruption Probability:", round(overall_disruption.mean()*100,2), "%")
