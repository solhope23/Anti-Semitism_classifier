class DataResearcher:

    @staticmethod
    def get_total_tweets(df):
        return df["Biased"].value_counts().to_dict()

    @staticmethod
    def get_average_length(df, cls_categories):
        average_length = {'total': 0}
        for category in cls_categories:
            new_df = df[df["Biased"] == category]
            for i in range(len(new_df)):
                len_of_words = len(new_df.iloc[i]["Text"].split())
                average_length["total"] += len_of_words
                average_length[category] = average_length.get(category, 0) + len_of_words
            average_length[category] /= len(new_df)
        average_length["total"] /= len(df)
        return average_length

    @staticmethod
    def get_common_words(df):
        words = {}
        for i in range(len(df)):
            split_text = df.iloc[i]["Text"].split()
            for word in split_text:
                words[word] = words.get(word, 0) + 1
        words = sorted(words, key=lambda k: words[k], reverse=True)
        return words[:10]


    @staticmethod
    def get_longest_3_tweets(df):