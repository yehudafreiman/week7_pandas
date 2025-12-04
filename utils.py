import pandas as pd

def load_json(json_name):
    df = pd.read_json(json_name)
    return df

def export_csv(df, csv_name):
    df = df.to_csv(csv_name)
    return df

def cleaning_data(df, column_name):
    if column_name == "total_amount":
        df[column_name] = df[column_name].str.replace('$', '')
    if column_name == "items_html":
        df[column_name] = df[column_name].str.replace('<b>', '')
        df[column_name] = df[column_name].str.replace('</b>', ' ')
        df[column_name] = df[column_name].str.replace('<br>', '')
    else:
        df[column_name] = df[column_name].replace({'': 'no coupon'})
    return df

def converse_data_type(df, column_name):
    if column_name == "total_amount":
        df["total_amount"] = df["total_amount"].astype(float)
    else:
        df["order_date"] = pd.to_datetime(df["order_date"])
    return df

def create_column(df, column_name):
    if column_name == "order_month":
        df["order_month"] = df['order_date'].dt.month
    if column_name == "high_value_order":
        average_total_amount = df["total_amount"].mean()
        df["high_value_order"] = [True if x > average_total_amount else False for x in df["total_amount"]]
    if column_name == "rating_average":
        df["rating_average"] = df.groupby("country")["rating"].transform('mean')
    else:
        df["delivery_status"] = ["delayed" if x > 7 else "on time" for x in df["shipping_days"]]
    return df

def sort_values(df, column_name):
    df = df.sort_values(column_name, ascending=False)
    return df

def filtering_by_condition(df, column1_name, column2_name):
    df = df[(df[column1_name] > 1000) & (df[column2_name] > 4.5)]
    return df











