from mylib.lib import (
    load_dataset,
    total_applicants,
    total_female_applicant,
    total_male_applicant,
    total_unknown_applicant,
    gender_total,
    gender_chart,
    ethnicity_total,
    ethnicity_chart,
)


csv = "Job_Applicants.csv"
df = load_dataset(csv)


def stats_overview(df):
    summary_stats = df[["Apps Received", "Female", "Male", "Unknown_Gender"]].describe()
    summary_stats.loc["total"] = df[
        ["Apps Received", "Female", "Male", "Unknown_Gender"]
    ].sum()
    summary_stats = summary_stats.round(2)
    print(summary_stats)
    return summary_stats


def number_of_applicants(df):
    total_apps = total_applicants(df)
    total_female = total_female_applicant(df)
    total_male = total_male_applicant(df)
    total_unknown = total_unknown_applicant(df)
    return total_apps, total_female, total_male, total_unknown


def gender_visulization(df):
    total_gender = gender_total(df)
    gender_chart(total_gender)


def ethi_visulization(df):
    total_ethi = ethnicity_total(df)
    ethnicity_chart(total_ethi)


if __name__ == "__main__":
    stats_overview(df)
    number_of_applicants(df)
    gender_visulization(df)
    ethi_visulization(df)
