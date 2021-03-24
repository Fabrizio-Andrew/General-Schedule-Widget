import json
import xml.etree.ElementTree as ET
import boto3

# param1 = year
# param2 = locality
# param3 = grade (optional)

s3 = boto3.resource('s3')

def BuildGradeObject(grade):
    gradeobject = { 'Grade': grade.find('{http://schemas.datacontract.org/2004/07/PayTables.Business}Value').text }
    i = 1
    for step in grade.findall('./{http://schemas.datacontract.org/2004/07/PayTables.Business}Steps/{http://schemas.datacontract.org/2004/07/PayTables.Business}Step'):
        step_data = {
            'Annual': step.find('{http://schemas.datacontract.org/2004/07/PayTables.Business}Annual').text,
            'Hourly': step.find('{http://schemas.datacontract.org/2004/07/PayTables.Business}Hourly').text,
            'Statutory_Cap_Applies': step.find('{http://schemas.datacontract.org/2004/07/PayTables.Business}Statutory_Cap_Applies').text
        }
        gradeobject[f'Step_{i}'] = step_data
        i += 1
    return(gradeobject)

#def lambda_handler(event, context)
    #bucketname = event['pathParameters']['param1']
    #filename = event['pathParameters']['param2']
    #obj = s3.Object(bucketname, filename)
obj = '2021/DCB.xml'
root = ET.parse(obj).getroot()
print('------------')
print(root)
grades = root.find('{http://schemas.datacontract.org/2004/07/PayTables.Business}Grades')


i = 1
for grade in grades:
    print(i)
    print(BuildGradeObject(grade))
    i = i+1




    


        
        


    