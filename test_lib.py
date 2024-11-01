from mylib.lib import (
    grab_mean,
    grab_median,
    grab_min,
    grab_max,
    total_applicants,
    total_female_applicant,
    total_male_applicant,
)

import pandas as pd

# Create a sample DataFrame
Data = {
    "Apps Received": [100, 200, 150],
    "Female": [40, 80, 70],
    "Male": [60, 110, 80],
}

sample_df = pd.DataFrame(Data)


def test_grab_mean():
    assert grab_mean(sample_df["Apps Received"]) == 150.0
    print("Mean Test Passed")


def test_grab_median():
    assert grab_median(sample_df["Female"]) == 70.0
    print("Median Test Passed")


def test_grab_min():
    assert grab_min(sample_df["Apps Received"]) == 100
    print("Min Test Passed")


def test_grab_max():
    assert grab_max(sample_df["Apps Received"]) == 200
    print("Max Test Passed")


def test_total_applicants():
    assert total_applicants(sample_df) == 450
    print("Total_applicants test passed!")


def test_female_applicants():
    assert total_female_applicant(sample_df) == 190
    print("Total_female_applicants test passed!")


def test_male_applicants():
    assert total_male_applicant(sample_df) == 250
    print("Total_male_applicants test passed!")


if __name__ == "__main__":
    test_grab_mean()
    test_grab_median()
    test_grab_min()
    test_grab_max()
    test_total_applicants()
    test_female_applicants()
    test_male_applicants()
