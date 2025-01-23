def search_parameters(ads):
    parameters = []
    for i in range(len(ads)):
        for j in range(len(ads[i]['ad_parameters'])):
            parameter = ads[i]['ad_parameters'][j]['pl']
            if parameter not in parameters:
                parameters.append(parameter)
    
    return parameters