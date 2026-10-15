"""Calculate annual export changes, PV statistics and wind-turbine maximum power points."""
from pathlib import Path
import csv
import math
from statistics import mean

ROOT = Path(__file__).resolve().parent

def rows(name):
    with (ROOT / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))

def require(condition, message):
    if not condition:
        raise ValueError(message)

def close(actual, expected, tolerance, description):
    require(math.isfinite(actual) and abs(actual - expected) <= tolerance,
            f"{description}: {actual} differs from {expected}")

def main():
    annual = rows("5208_annual_summary.csv")
    require(len(annual) == 3, "Expected three annual scenarios")
    exports = []
    for row in annual:
        require(int(row["steps"]) == 365 * 24 * 12, "Invalid 5-minute annual length")
        require(int(row["voltage_violation_steps"]) == 0, "Unexpected Task II violation count")
        require(0.9 <= float(row["min_voltage_pu"]) <= float(row["max_voltage_pu"]) <= 1.1,
                "Task II voltage extrema disagree with the documented course interval")
        hours = float(row["reverse_flow_hours"])
        close(hours * 12, round(hours * 12), 1e-7, "Reverse-flow step integrality")
        require(0 <= hours <= 8760, "Invalid reverse-flow duration")
        exports.append(float(row["annual_export_kwh"]))
    require(exports[0] > exports[1] > exports[2], "Unexpected export scenario ordering")
    reduction = 100 * (1 - exports[1] / exports[0])
    close(reduction, 21.87745, 0.02, "10 kWh annual export reduction (%)")
    print(f"Task II: 3 x 105120 steps; 10 kWh export reduction {reduction:.2f}%")

    expected = [("normal", 4.064, 4.463, 0.0127), ("tilted", 2.153, 2.336, 0.0217)]
    averages = []
    for condition, target_mean, target_max, target_residual in expected:
        samples = rows(f"5206_mppt_{condition}.csv")
        require(len(samples) == 201, f"{condition}: expected 201 samples")
        power = [float(r["pv_power_w"]) for r in samples]
        residual = max(abs(float(r["pv_power_w"]) - float(r["pv_voltage_v"]) *
                           float(r["pv_current_a"])) for r in samples)
        close(mean(power), target_mean, 0.001, f"{condition} mean power")
        close(max(power), target_max, 1e-8, f"{condition} max power")
        close(residual, target_residual, 0.0001, f"{condition} power-product residual")
        averages.append(mean(power))
        print(f"MPPT {condition}: {len(samples)} points; mean {mean(power):.6f} W; "
              f"max residual {residual:.6f} W")
    print(f"Tilted mean-power reduction: {100 * (1 - averages[1] / averages[0]):.2f}%")

    wind = rows("5206_wind_measurements.csv")
    require(len(wind) == 27, "Expected 27 wind-turbine operating points")
    for speed, target_power, target_rpm in [(5, 22.61, 458), (7, 65.35, 889), (10, 181.0, 1022)]:
        group = [r for r in wind if int(r["wind_speed_ms"]) == speed]
        require(len(group) == 9, f"Expected nine points at {speed} m/s")
        best = max(group, key=lambda r: abs(float(r["electrical_power_w_signed"])))
        power = abs(float(best["electrical_power_w_signed"]))
        close(power, target_power, 1e-8, f"Wind {speed} m/s maximum power")
        close(float(best["rotor_speed_rpm"]), target_rpm, 1e-8, "MPP rotor speed")
        print(f"Wind {speed} m/s: MPP {power:.2f} W at {target_rpm} rpm")
    print("Data calculations completed successfully.")

if __name__ == "__main__":
    main()
