import pandas as pd
from fpdf import FPDF

from pdf_code import create_pdf


df = pd.read_csv('articles.csv')


class Article:
    def __init__(self, article_id, df, pdf_func=create_pdf):
        # find the article in df
        result = df.loc[df['id'] == int(article_id)]
        if result.empty:
            raise ValueError(f"No article found with id={article_id}")
        self.data = result.iloc[0]

        # store PDF function
        self.pdf_func = pdf_func

    def print_pdf(self):
        # use the injected function
        self.pdf_func(self.data)


while True:
    print(df)
    try:
        user_input = input('Choose an article to buy: ')
        if user_input == 'q':
            break
        article = Article(user_input, df)
        article.print_pdf()
    except (IndexError) as e:
        print(e)
