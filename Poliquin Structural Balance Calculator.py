def calculate_ratios(bench_press_kg, squat_kg):
    # Upper Body Ratios
    incline_bench_press = bench_press_kg * 0.91
    parallel_bar_dip = bench_press_kg * 1.17
    dumbbell_press_per_arm = bench_press_kg * 0.30
    triceps_extension = bench_press_kg * 0.40
    chin_ups = bench_press_kg * 0.87
    scott_curls = bench_press_kg * 0.46
    reverse_curls = bench_press_kg * 0.40
    flat_powel_raise = bench_press_kg * 0.106
    bent_over_dumbbell_trap3_raise = bench_press_kg * 0.106
    seated_dumbbell_external_rotation = bench_press_kg * 0.098

    # Lower Body Ratios
    front_squat = squat_kg * 0.85
    deadlift = squat_kg * 1.25
    power_clean = squat_kg * 0.66
    power_snatch = squat_kg * 0.51
    peterson_step_up = squat_kg * 0.46
    triple_jumpers_step_up = squat_kg * 0.30
    full_snatch = squat_kg * 0.66
    close_grip_bench_press_lower = squat_kg * 0.66

    results = {
        'Incline Bench Press': incline_bench_press,
        'Parallel Bar Dip': parallel_bar_dip,
        '1-Arm Dumbbell Press (per arm)': dumbbell_press_per_arm,
        'Lying Triceps Extension': triceps_extension,
        'Supinated Chin-ups': chin_ups,
        'Scott Barbell Curls': scott_curls,
        'Standing Reverse Curls': reverse_curls,
        'Flat Powel Raise': flat_powel_raise,
        'Bent-over Dumbbell Trap-3 Raise': bent_over_dumbbell_trap3_raise,
        'Seated Dumbbell External Rotation': seated_dumbbell_external_rotation,
        'Front Squat': front_squat,
        'Deadlift': deadlift,
        'Power Clean': power_clean,
        'Power Snatch': power_snatch,
        'Peterson Step-up': peterson_step_up,
        'Triple Jumpers Step-up': triple_jumpers_step_up,
        'Full Snatch': full_snatch,
        'Close Grip Bench Press (Lower)': close_grip_bench_press_lower
    }

    return results

def main():
    try:
        bench_press_kg = float(input("Podaj wartość w kilogramach dla Close Grip Bench Press: "))
        squat_kg = float(input("Podaj wartość w kilogramach dla High Bar Back Squat: "))

        results = calculate_ratios(bench_press_kg, squat_kg)

        print("\nWyniki:")
        for exercise, value in results.items():
            print(f"{exercise}: {value:.2f} kg")

    except ValueError:
        print("Proszę podać prawidłową wartość liczbową.")

if __name__ == "__main__":
    main()
