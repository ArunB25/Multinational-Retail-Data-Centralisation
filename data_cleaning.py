from data_extraction import DataExtractor

class DataClean():
    def clean_user_data(self, data_frame):
        data_frame =data_frame
        # datas are all same format
        #no nulls in names
        #phone numbers same format
        #if missing user uuid assign one
        #check for duplicate data in phone number and user uuid
        


if __name__ == '__main__':
    df = DataExtractor().extract_rds_table('legacy_users')
    print(DataClean().clean_user_data(df))