import requests
import pandas as pd

def get_investment_fund_data():
    url = 'https://fund.fipiran.ir/api/v1/fund/fundcompare'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://fund.fipiran.ir/mf/list',
        'Cookie': '_ga_GMN6YQMVMN=GS1.1.1688036114.1.0.1688036114.0.0.0; _ga=GA1.1.1888402578.1688036115',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error retrieving data.")
        return None

def extract_fund_information_and_save(data):
    df = pd.DataFrame(data['items'], columns=["regNo", "name"]) # needed columns will be defined here
    df.to_csv('/home/mehrnoosh/PycharmProjects/technical_test_middle_east_bank/raw_data.csv', index=False)
    return df


def run_pipeline():
    # Step 1: Gather Daily Investment Fund Information
    raw_data = get_investment_fund_data()

    if raw_data is not None:

        # Step 2: Parse the response JSON and extract relevant information
        analysable_data = extract_fund_information_and_save(raw_data)

        # Print or process the extracted fund information as needed
        print(analysable_data)

    else:
        print("Pipeline execution failed.")