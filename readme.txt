# file may contain just two columns with german/modertongue

objects
    nomen (6 col)
        kuche    # die
        balkon   # der
        zimmer   # das
    verben (4 col)
        akk      # akussativ
        dat      # dativ
    adjektiven/adverbien (2 col)

# Organize data
for each column count the amount of items
    if 4 columns namen
        define key (id item)
        define german (string)
        define modertongue (string)
        define categorical variable (location)
        define categorical variable (match)
    if 4 columns verben
        define key (id item)
        define german (string)
        define modertongue (string)
        define categorical variable (objekt boolean)
        define categorical variable (trennen boolean)
        define categorical variable (match)
    if 2 column adj-adv
        define key (id item)
        define german (string)
        define modertongue (string)
        define categorical variable (match)

# Insert data into a dataframe (json format?)
        nomen (key+5 attributes)
            item (id)
            german (string)
            modertongue (string)
            location (categorical)
            match (boolean)
    verben (key+6 attributes)
        item (id)
            german (string)
            modertongue (string)
objekt (categorical, boolean)
        trennen (categorical, boolean)
        match (boolean)
    adjektiven/adverbien (key+4 attribute)
            item (id)
            german (string)
            modertongue (string)
        match (boolean)

# Evaluation
    from list of num/ids random choose
        if id selected already selected -> next
    if any of the attributes not correctly given -> match = 0
    count all items in dataframe
    count matches
    date + type of object + num of items + fraction of match + percentage of match

# Interface
    ask for each item specifying attribute to evaluate

    
    

    

