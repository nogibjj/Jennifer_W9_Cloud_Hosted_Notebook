import pandas as pd
import matplotlib.pyplot as plt


# Load dataset
def load_dataset(dataset):
    df = pd.read_csv(dataset)
    return df


# define functions to grab statistical values
def grab_mean(df):
    return df.mean().round(2)


def grab_median(df):
    return df.median().round(2)


def grab_std(df):
    return df.std().round(2)


def grab_min(df):
    return df.min().round(2)


def grab_max(df):
    return df.max().round(2)


# Calculate total number of applicants
def total_applicants(df):
    total_apps = df["Apps Received"].sum()
    print(f"Total applicants: {total_apps:,}")
    return total_apps


# calculate total number of applicants by gender
def total_female_applicant(df):
    total_female_applicants = df["Female"].sum()
    print(f"Total female applicants: {total_female_applicants:,}")
    return total_female_applicants


def total_male_applicant(df):
    total_male_applicants = df["Male"].sum()
    print(f"Total male applicants: {total_male_applicants:,}")
    return total_male_applicants


def total_unknown_applicant(df):
    total_unknown_applicants = df["Unknown_Gender"].sum()
    print(f"Total unknown gender applicants: {total_unknown_applicants:,}")
    return total_unknown_applicants


def gender_total(df):
    gender_total = df[["Female", "Male", "Unknown_Gender"]].sum()
    return gender_total


# gender chart
def gender_chart(gender_total):
    plt.figure(figsize=(10, 6))
    plt.bar(gender_total.index, gender_total.values)
    plt.title("Number of Applicants by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Number of Applicants")
    plt.show()


# calculate total number of applicants by ethnicity
def ethnicity_total(df):
    ethnicity_total = df[
        [
            "Black",
            "Hispanic",
            "Asian",
            "Caucasian",
            "American Indian/ Alaskan Native",
            "Filipino",
            "Unknown_Ethnicity",
        ]
    ].sum()
    return ethnicity_total


# ethnicity chart
def ethnicity_chart(ethnicity_total):
    plt.figure(figsize=(18, 6))
    # colors = plt.cm.viridis(np.linspace(0, 1, len(ethnicity_total)))
    colors = [
        "#E94E1B",
        "#F47B20",
        "#F2D700",
        "#009B77",
        "#800080",
        "#004B87",
        "#000000",
    ]

    plt.bar(ethnicity_total.index, ethnicity_total.values, color=colors)
    plt.title("Number of Applicants by Ethnicity")
    plt.xlabel("Ethnicity")
    plt.ylabel("Number of Applicants")
    plt.show()
