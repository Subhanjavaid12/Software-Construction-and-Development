"""
salary_calculator.py
Independent Challenge: Employee Salary Calculator with cohesive functions.
"""


def calculate_gross_salary(basic_salary: float, allowance: float) -> float:
    """Calculates the total earnings before any deductions."""
    if basic_salary < 0 or allowance < 0:
        raise ValueError("Basic salary and allowance cannot be negative.")
    return basic_salary + allowance


def calculate_tax(gross_salary: float, tax_rate: float) -> float:
    """
    Calculates the tax deduction amount based on gross salary.
    tax_rate is expected as a decimal (e.g., 0.15 for 15%) or whole percentage (15).
    """
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative.")

    # Normalize percentage if passed as e.g. 15 instead of 0.15
    rate = tax_rate / 100.0 if tax_rate > 1 else tax_rate
    return gross_salary * rate


def calculate_net_salary(gross_salary: float, tax_amount: float) -> float:
    """Calculates final take-home pay by subtracting deductions from gross earnings."""
    return gross_salary - tax_amount


def display_salary_slip(
    employee_name: str,
    basic_salary: float,
    allowance: float,
    gross_salary: float,
    tax_amount: float,
    net_salary: float,
) -> None:
    """Handles presentation and output formatting."""
    print("=" * 40)
    print(f"SALARY SLIP: {employee_name.upper()}")
    print("=" * 40)
    print(f"Basic Salary : ${basic_salary:,.2f}")
    print(f"Allowance    : ${allowance:,.2f}")
    print(f"Gross Salary : ${gross_salary:,.2f}")
    print(f"Tax Deducted : ${tax_amount:,.2f}")
    print("-" * 40)
    print(f"Net Salary   : ${net_salary:,.2f}")
    print("=" * 40)


def main() -> None:
    # Example inputs
    employee_name = "Jane Doe"
    basic_salary = 5000.00
    allowance = 1200.00
    tax_rate = 0.15  # 15%

    # Business calculations
    gross = calculate_gross_salary(basic_salary, allowance)
    tax = calculate_tax(gross, tax_rate)
    net = calculate_net_salary(gross, tax)

    # Presentation
    display_salary_slip(employee_name, basic_salary, allowance, gross, tax, net)


if __name__ == "__main__":
    main()