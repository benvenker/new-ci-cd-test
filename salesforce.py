from simple_salesforce import Salesforce

sf = Salesforce(username='my_username', password='my_password', security_token='my_token')

record = {
    'LastName' : 'Smith',
    'Email' : 'example@example.com',
    'Phone' : '123-456-7890'
}

sf.Contact.create(record)
