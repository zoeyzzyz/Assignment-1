import pandas as pd

def clean(contact_info_file,other_info_file):
    df1=pd.read_csv(contact_info_file)
    df2=pd.read_csv(other_info_file)
    df=pd.merge(df1,df2,left_on='respondent_id',right_on='id')
    df=df.drop(columns=['id'])
    df=df.dropna()
    df=df[(df['job'].str.contains('insurance|Insurance'))==False]
    return df

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('contact_info_file',help='The path to the respondent_contact.csv file')
    parser.add_argument('other_info_file',help='The path to the respondent_other.csv file')
    parser.add_argument('output_file',help='The path to the output file')
    args=parser.parse_args()

    cleaned=clean(args.contact_info_file,args.other_info_file)
    cleaned.to_csv(args.output_file,index=False)