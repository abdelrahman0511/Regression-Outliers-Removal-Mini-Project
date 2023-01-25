#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    
    for point in zip(predictions, ages, net_worths):
        cleaned_data.append((point[1], point[2], (point[0]-point[2])))
    
    # Sorting data descending based on the error
    cleaned_data.sort(key = lambda i:i[2], reverse = True)

    # Selecting the 90% of the data with least error (Removing 10% of the ouliers)
    cleaned_data = cleaned_data[(round(len(cleaned_data)*0.1)):]
    
    return cleaned_data

