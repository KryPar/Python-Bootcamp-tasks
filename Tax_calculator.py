print("This program calculates taxes ")

FEDERAL_STANDARD_DEDUCTION = 13200

FEDERAL_TAX_BRACKETS = [
    (10400, 0.10),
    (41225, 0.12),
    (89400, 0.22),
    (174050, 0.24),
    (215400, 0.32),
    (549900, 0.35),
    (1000000, 0.37)
]

gross_salary = float(input("Enter your gross salary: "))

deducted_salary = gross_salary - FEDERAL_STANDARD_DEDUCTION

print(f"Gross salary: ${gross_salary:.2f}")

federal_tax = 0
previous_bracket_limit = 0
if deducted_salary > 0:
    
    for bracket_limit, tax_rate in FEDERAL_TAX_BRACKETS:
        if deducted_salary > bracket_limit:
            federal_tax += (bracket_limit - previous_bracket_limit) * tax_rate
        else:
            federal_tax += (deducted_salary - previous_bracket_limit) * tax_rate
            break
        previous_bracket_limit = bracket_limit

print(f"Federal tax: ${federal_tax:.2f}")

def calculate_california_tax(deducted_salary):
    state_tax = 0
    previous_bracket_limit = 0
    if deducted_salary > 0:
    
        for bracket_limit, tax_rate in STATE_TAX_BRACKETS["California"]:
            if deducted_salary > bracket_limit:
                state_tax += (bracket_limit - previous_bracket_limit) * tax_rate
            else:
                state_tax += (deducted_salary - previous_bracket_limit) * tax_rate
                break
            previous_bracket_limit = bracket_limit
        return state_tax

def calculate_new_york_tax(deducted_salary):

    state_tax = 0
    previous_bracket_limit = 0
    if deducted_salary > 0:
        for bracket_limit, tax_rate in STATE_TAX_BRACKETS["New York"]:
            if deducted_salary > bracket_limit:
                state_tax += (bracket_limit - previous_bracket_limit) * tax_rate
            else:
                state_tax += (deducted_salary - previous_bracket_limit) * tax_rate
                break
            previous_bracket_limit = bracket_limit
        return state_tax

STATE_STANDARD_DEDUCTION = {
 'California': 4609,
 'New York': 8000 
}

STATE_TAX_BRACKETS = {
'California': [
(9076, 0.01),
(22771, 0.02),
(34211, 0.04),
(48898, 0.06),
(48897, 0.08),
(59878, 0.093),
(71805, 0.103),
(100000, 0.113)
],
'New York': [
(8500, 0.04),
(11700, 0.045),
(13900, 0.0525),
(21400, 0.059),
(80650, 0.0645),
(215400, 0.0685),
(1077550, 0.0882),
(1000000, 0.103)
]
}

state = input("Enter your state (California or New York):")

state_tax = 0
previous_bracket_limit = 0

if state == "California":
    deducted_salary = gross_salary - STATE_STANDARD_DEDUCTION["California"]
    state_tax = calculate_california_tax(deducted_salary)

elif state == "New York":
    deducted_salary = gross_salary - STATE_STANDARD_DEDUCTION["New York"]
    state_tax = calculate_new_york_tax(deducted_salary)
else:
    print("Wrong state")

fica_rate = 0.0765
fica_salary_cap = 147000

fica_tax = min(gross_salary,fica_salary_cap)*fica_rate
net_salary = gross_salary - federal_tax - fica_tax - state_tax

print(f"State tax: ${state_tax:.2f}")
print(f"Fica tax: ${fica_tax:.2f}")
print(f"Net Salary: ${net_salary:.2f} ")