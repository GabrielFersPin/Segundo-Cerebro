# Work with different file formats[[Python Links]]
#Python 

- Reading data from CSV format in Python
    
    ```python
    import pandas as pd
    df = pd.read_csv("adresses.csv", header = none)
    ```
    
    ### Adding column name to the dataframe
    
    ```python
    	df.columns = ['First Name', 'Last Name', 'Location', 'City', 'State', 'Area Code']
    
    ```
    
    ### Selecting a single column
    
    ```python
    df['First Name']
    ```
    
    ### Selecting multiple columns
    
    ```python
    	df = df[['Fisrt Name', 'Last Name', 'Location', 'City', 'etc...']]
    ```
    
    ### Select rows using .iloc() and .loc()
    
    ```python
    #To select the first row
    df.loc[0]
    ```
    
    ```python
    #To select the 0th, 1st and 2nd row of 'First Name' column only
    df.loc[[0, 1, 2], "First Name"]
    ```
    
    ### .iloc() is a index label based selecting method wich means that we have to pass integer index in the method to select specific column/row
    
    ```python
    #To select the 0th, 1st and the 2nd row of "First Name" column only 
    df.iloc[[o, 1, 2], 0]
    ```
    
    ### Transform functions in pandas
    
    ```python
    import pandas as pd
    import numpy as np
    #creat a dataframe
    df = pd.Dataframe(np.array([]))
    # applying the transform function
    df = df.transform(func = lambda x : x + 10)
    # this transform the function adding 10 to every number of the dataframe
    ```
    
- Writing JSON to a file
    - is built on two estructures:
    1. A collection of name/value pairs.
    2. An ordered list of values
    
    ```python
    import json 
    ```
    
    ### JSON file format
    
    - Serialization
        
        Is the process of converting an object into a special format wich is suitable for transmitting over the network or storing in a file or database
        
    - Serialization using dump() function
        
        json.dump() method can be used for writing to JSON file
        
        syntax: json.dump(dict, file_pointer)
        
        parameters: 
        
        1. dictionary - name of the dictionary wich should be converted to JSON object.
        2. file pointer - pointer of the file opened in write or append mode.
            
            ```python
            with open('person.json', 'w') as f:  # writing JSON object
                json.dump(person, f)
            ```
            
    - Serialization using dumps() function
        
        json.dumps() funtion can be used for writing to JSON file.
        
        syntax: json.dumps(dict, indent)
        
        1. Dictionary - name of the dictionary wich should be converted to JSON object.
        2. Indent - defines the number of units for indentation
    
    ### Reading JSON to a file
    
    - Deserialization
        
        it converts the special format returned by the serialization back into a usable object
        
    
    ### Using json.load()
    
    - Loads teh json content from a json file into a dictionary
    - It takes one parameter: File pointer. a file pointer that point to a JSON file
- XLSX file format
    - Reading the data from XLSX with Pandas
    
    ```python
    df = pd.read_excel("File_Name.xlsx")
    ```
    
    ### Writing with xml.etree.ElementTree
    
    The xml.etree.ElementTree module can bulti-in with python. It provides functionality for parsing and creating XML documents. ElementTree represents the document XML as a tree
    
    ```python
    import xml.etree.ElementTree as ET
    
    # create the file structure
    employee = ET.Element('employee')
    details = ET.SubElement(employee, 'details')
    first = ET.SubElement(details, 'firstname')
    second = ET.SubElement(details, 'lastname')
    third = ET.SubElement(details, 'age')
    first.text = 'Shiv'
    second.text = 'Mishra'
    third.text = '23'
    
    # create a new XML file with the results
    mydata1 = ET.ElementTree(employee)
    # myfile = open("items2.xml", "wb")
    # myfile.write(mydata)
    with open("new_sample.xml", "wb") as files:
        mydata1.write(files)
    ```
    
    ### Reading with xml.etree.ElementTree
    
    ```python
    tree = etree.parse("Sample-employee-XML-file.xml")
    
    root = tree.getroot()
    columns = ["firstname", "lastname", "title", "division", "building","room"]
    
    datatframe = pd.DataFrame(columns = columns)
    
    for node in root: 
    
        firstname = node.find("firstname").text
    
        lastname = node.find("lastname").text 
    
        title = node.find("title").text 
        
        division = node.find("division").text 
        
        building = node.find("building").text
        
        room = node.find("room").text
        
        datatframe = datatframe.append(pd.Series([firstname, lastname, title, division, building, room], index = columns), ignore_index = True)
    ```
    
    ### Reading xml file format using pandas.read_xml function
    
    ```python
    # Herein xpath we mention the set of xml nodes to be considered for migrating  to the dataframe which in this case is details node under employees.
    df=pd.read_xml("Sample-employee-XML-file.xml", xpath="/employees/details")
    ```
    
- Saving data
    
    Pandas enables us to save the dataset to csv by using the dataframe.to_csv() method, you can add the file path and name along with quotation marks in parentheses.
    
    ```python
    datatframe.to_csv("employee.csv", index=False)
    ```
    
    ### Read and save in other data formats
    
    | Data Format | Read | Save |
    | --- | --- | --- |
    | csv | pd.read_csv() | df.to_csv() |
    | json | pd.read_json() | df.to_json() |
    | excel | pd.read_excel() | df.to_excel() |
    | hdf | pd.read_hdf() | df.to_hdf() |
    | sql | pd.read_sql() | df.to_sql() |
- Binary file format
    
    ### Reading the image file
    
    - PIL
        
        PIL is the Python Image Library wich provides the python interpreter with image editing capabilities
        
        ```python
        # importing PIL 
        from PIL import Image 
        
        # Uncomment if running locally
        # import urllib.request
        # urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "dog.jpg")
        
        filename = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"
        
        async def download(url, filename):
            response = await pyfetch(url)
            if response.status == 200:
                with open(filename, "wb") as f:
                    f.write(await response.bytes())
        
        await download(filename, "dog.jpg")
        ```
        
        ```python
        # Read image 
        img = Image.open('dog.jpg') 
          
        # Output Images 
        display(img)
        ```