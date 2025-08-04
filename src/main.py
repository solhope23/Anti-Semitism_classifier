import pandas as pd
from data_researcher import DataResearcher

df = pd.read_csv("../data/tweets_dataset.csv")
x = [0, 1]
# print(DataResearcher.get_average_length(df, x))
# def sorrrrr(dd):
#     return len(dd)
print(df["Text"].head())
print("\n")
print(df[df["Biased"] == 0].sort_values("Text",)["Text"].head(3))

# print(DataResearcher.get_common_words(df))
# x = ["Text", "Biased"]
# b = 0
# for i in df:
#     print(i)
#     b += 1
#     if b == 2:
#         break
# df.columns

# print(df.head())
# for i in range(10):
#     print(i)
#     print(df.iloc[i][x])
# print(df.columns)
# print(df["Text"])
# f = df["Biased"].value_counts().to_dict()
# f["total"] = sum(f)
# print(f)
# print(len(df))


# l = ['a', 'g', 'f', 'w', 'a']
# d = {}
# for i in l:
#     d[i] = d.get(i, 0)
#     d[i] += 1
# print(d)


# a = {1: "F", 3: "d", 7: "v"}
# print(len(a))
# print(max(a))
#
# a = [1, 2]
# b = dict(for i in a
