"""Temperature calculations used in Lab 2 and tested in Lab 3."""


def find_min_max(temperatures):
    """Return the minimum and maximum as a tuple."""
    return min(temperatures), max(temperatures)


def calc_average(temperatures):
    """Return the arithmetic mean of a nonempty sequence."""
    if not temperatures:
        raise ValueError("At least one temperature is required")
    return sum(temperatures) / len(temperatures)


def calc_median_temperature(temperatures):
    """Return the median without modifying the input sequence."""
    if not temperatures:
        raise ValueError("At least one temperature is required")
    ordered = sorted(temperatures)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


if __name__ == "__main__":
    values = [24, 30, 26, 28]
    print("Minimum and maximum:", find_min_max(values))
    print("Average:", calc_average(values))
    print("Median:", calc_median_temperature(values))
