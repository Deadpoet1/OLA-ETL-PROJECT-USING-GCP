import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df1, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    df1['Id']=df1.index+1
    df1['fare_amount']=pd.to_numeric(df1['fare_amount'],errors='coerce')
    df1['pickup_datetime']=pd.to_datetime(df1['pickup_datetime'],format='mixed')
    df1['fare_amount_value']=df1['fare_amount']
    df1['Passenger_counts']=df1['passenger_count']
    df1['pickup_year']=df1['pickup_datetime'].dt.year
    df1['pickup_month']=df1['pickup_datetime'].dt.month_name()
    df1['pickup_date']=df1['pickup_datetime'].dt.date
    

    df1['pickup_date'] = pd.to_datetime(df1['pickup_date'], format='%Y-%m-%d') 

    df1['pickup_day']=df1['pickup_datetime'].dt.day_name()
    df1['pickup_time']=df1['pickup_datetime'].dt.time
    df1['pickup_time'] = pd.to_datetime(df1['pickup_time'], format='%H:%M:%S') 
    df1['pickup_hour']=df1['pickup_datetime'].dt.hour
    df1['pickup_longitude_value']=df1['pickup_longitude']
    df1['pickup_latitude_value']=df1['pickup_latitude']
    df1['dropoff_longitude_value']=df1['dropoff_longitude']
    df1['dropoff_latitude_value']=df1['dropoff_latitude']
    df1.drop(['fare_amount','passenger_count','pickup_datetime','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude'], axis=1, inplace=True)
    return df1


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'