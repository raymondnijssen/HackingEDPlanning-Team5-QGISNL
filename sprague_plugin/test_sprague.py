import sprague

age_groups = {
    0: [0, 4, 3913900],
    5: [5, 9, 3516700],
    10: [10, 14, 3669300],
    15: [15, 19, 3996400],
    20: [20, 24, 4297200],
    25: [25, 29, 4306300],
    30: [30, 34, 4125500],
    35: [35, 39, 4194400],
    40: [40, 44, 4625600],
    45: [45, 49, 4643100],
    50: [50, 54, 4094400],
    55: [55, 59, 3614100],
    60: [60, 64, 3808000],
    65: [65, 69, 3017500],
    70: [70, 74, 2462800],
    75: [75, 79, 2006000],
    80: [80, -1, 2890900]
}

sprague_calculator = sprague.SpragueCalculator()

print(sprague_calculator)

sprague_calculator.set_by_age_groups(age_groups, max_age=79)

for age_key, age_value in sprague_calculator.ages.items():
    print(age_key, round(age_value))
