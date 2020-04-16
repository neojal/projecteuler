def main():
    # usa yearly working days estimated = 250
    vacations = 10
    working_days = 250 - vacations
    hours_per_day = 8
    total_hours = working_days * hours_per_day

    usd_to_peso = 21

    usd_rate = 20
    usd_rate_min = 19

    year_salary_min = total_hours * usd_rate_min * usd_to_peso
    year_salary = total_hours * usd_rate * usd_to_peso

    social_security_etc = 12 * 10_000

    print("")
    print("minimal estimated year salary in pesos (", usd_rate_min, "/ hr ) = $", year_salary_min)
    print("minus social security: $", year_salary_min - social_security_etc)
    print("")
    print("estimated year salary in pesos(", usd_rate, "/ hr ) = $", year_salary)
    print("minus social security: $", year_salary - social_security_etc)


if __name__ == "__main__":
    main()
