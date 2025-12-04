from utils import load_json, export_csv, cleaning_data, converse_data_type, create_column, sort_values, filtering_by_condition

if __name__ == "__main__":

    # load json
    df = load_json("orders_simple.json")

    # cleaning data
    df = cleaning_data(df, "total_amount")
    df = cleaning_data(df, "items_html")
    df = cleaning_data(df, "coupon_used")

    # converse data type
    df = converse_data_type(df, "total_amount")
    df = converse_data_type(df, "order_date")

    # create columns
    create_column(df, "order_month")
    create_column(df, "high_value_order")
    create_column(df, "rating_average")
    create_column(df, "delivery_status")

    # sort df by total_amount
    df = sort_values(df, "total_amount")

    # filtering by condition
    df = filtering_by_condition(df, "total_amount", "rating")

    # export to csv
    df = export_csv(df, "clean_orders_205368319.csv")

