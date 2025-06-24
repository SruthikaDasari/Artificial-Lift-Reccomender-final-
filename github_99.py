def recommend_artificial_lift(depth_ft, flow_rate_bpd, fluid_type, gas_available):
    if flow_rate_bpd < 500 and depth_ft < 6000:
        return "Sucker Rod Pump (SRP)"
    elif fluid_type == "heavy" and depth_ft < 7000:
        return "Progressing Cavity Pump (PCP)"
    elif flow_rate_bpd > 3000 and gas_available:
        return "Gas Lift"
    elif flow_rate_bpd > 2000 and depth_ft > 5000:
        return "Electrical Submersible Pump (ESP)"
    elif depth_ft > 10000:
        return "Hydraulic Jet Pump"
    else:
        return "Intermittent Gas Lift or Plunger Lift"

# Sample Input
depth = float(input("Enter reservoir depth (ft): "))
flow_rate = float(input("Enter expected flow rate (bpd): "))
fluid_type = input("Enter fluid type (light/heavy): ").lower()
gas_input = input("Is lift gas available? (yes/no): ").lower()
gas_available = gas_input == "yes"

# Output
lift_method = recommend_artificial_lift(depth, flow_rate, fluid_type, gas_available)
print(f"\n✅ Recommended Artificial Lift Method: {lift_method}") 
