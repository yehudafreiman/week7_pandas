
import pandas as pd

from utils import load_json

if __name__ == "__main__":

    # load json
    df = load_json("orders_simple.json")

    # cleaning data
    df["total_amount"] = df["total_amount"].str.replace('$', '')

    df["items_html"] = df["items_html"].str.replace('<b>', '')
    df["items_html"] = df["items_html"].str.replace('</b>', ' ')
    df["items_html"] = df["items_html"].str.replace('<br>', '')

    df["coupon_used"] = df["coupon_used"].replace({'': 'no coupon'})

    # converse data type
    df["total_amount"] = df["total_amount"].astype(float)
    df["order_date"] = pd.to_datetime(df["order_date"])

    # create column order_month
    df["order_month"] = df['order_date'].dt.month

    # create column high_value_order
    average_total_amount = df["total_amount"].mean()
    df["high_value_order"] = [True if x > average_total_amount else False for x in df["total_amount"]]

    # sort df by total_amount
    df = df.sort_values("total_amount", ascending=False)

    # create column rating_average
    rating_average_by_country = df.groupby("country")["rating"].mean()
    df["rating_average"] = df.groupby("country")["rating"].transform('mean')

    


    # export to csv
    df.to_csv("clean_orders_205368319.csv")


   
