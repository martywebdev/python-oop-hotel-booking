import pandas as pd
from fpdf import FPDF

from pdf_code import Receipt


df = pd.read_csv('articles.csv')


class Article:
    def __init__(self, article_id, df, pdf_cls=Receipt):
        # find the article in df
        self.df = df  # keep reference
        result = df.loc[df['id'] == int(article_id)]
        if result.empty:
            raise ValueError(f"No article found with id={article_id}")
        self.data = result.iloc[0]
        self.index = result.index[0]
        # store PDF function
        self.pdf_cls = pdf_cls

    def available(self):
        return self.data['in stock'] > 0

    def sales(self):
        self.df.at[self.index, 'in stock'] -= 1
        self.df.to_csv('articles.csv', index=False)

    def print_pdf(self):
        # use the injected function
        receipt = self.pdf_cls(self.data)  # instantiate class
        receipt.generate()   


while True:
    print(df)
    try:
        user_input = input('Choose an article to buy: ')
        if user_input == 'q':
            break
        article = Article(user_input, df)
        if article.available():
            article.sales()
            article.print_pdf()
    except (IndexError, ValueError) as e:
        print(e)
