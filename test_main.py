from main import stats_overview, number_of_applicants
from mylib.lib import (
    grab_mean,
    grab_median,
    grab_std,
    grab_min,
    grab_max,
)
import pandas as pd

# Create a sample DataFrame
Data = {
    "Apps Received": [110, 210, 180],
    "Female": [40, 80, 70],
    "Male": [60, 110, 80],
    "Unknown_Gender": [10, 20, 30],
}

sample_df = pd.DataFrame(Data)


def test_stats_overview():
    summary_stats = stats_overview(sample_df)
    assert summary_stats["Apps Received"]["mean"] == grab_mean(
        sample_df["Apps Received"]
    )
    assert summary_stats["Apps Received"]["50%"] == grab_median(
        sample_df["Apps Received"]
    )
    assert summary_stats["Apps Received"]["min"] == grab_min(sample_df["Apps Received"])
    assert summary_stats["Apps Received"]["max"] == grab_max(sample_df["Apps Received"])
    assert summary_stats["Apps Received"]["std"] == grab_std(sample_df["Apps Received"])


def test_number_of_applicants():
    assert number_of_applicants(sample_df) == (500, 190, 250, 60)


if __name__ == "__main__":
    test_stats_overview()
    test_number_of_applicants()
    print("All tests passed!")
