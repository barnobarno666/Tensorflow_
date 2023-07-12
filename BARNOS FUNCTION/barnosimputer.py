def BarnosImputer(dataframe):
    from math import ceil
    from random import shuffle
    
    for colum in list(dataframe.columns):
        n=dataframe[colum].isna().sum()
        if n>0:
            new_Data={}
            hello=(dataframe[colum].value_counts('P')).to_dict()
            unique_value=list(hello.keys())
            proportions=list(hello.values())
            n=dataframe[colum].isna().sum()
            #make a list with the proportions
            print(proportions,colum)
        
            for i  in range(len(proportions)):
                proportions[i]=ceil(proportions[i]*n)
            print(proportions)
            values_to_fill_with=[]
            #create a new list with the values
            for j  in range (len(proportions)):
                number_of_times=(proportions[j])
                for k in range(number_of_times):
                    values_to_fill_with.append(unique_value[j])
            shuffle(values_to_fill_with)
            #cut the list with nun values num
            #values_to_fill_with=values_to_fill_with[0:n]
            #find the index with missing values
            missing_column=dataframe[dataframe[column].isna()].index.to_list()
            #fill 
            print(f'value of missing is {n}',f'value od missing column : {len(missing_column)}',f'value of value to fill column:  {len(values_to_fill_with)}')
            for i  in range(len(missing_column)):
                dataframe[column][missing_column[i]]=values_to_fill_with[i]
        else:pass
    return dataframe