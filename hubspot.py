import requests

# Please replace these with the actual values for your EMR system
api_url = 'API_URL' # the endpoint url of the EMR system API
api_key = 'API_KEY' # the API key for your EMR system
patient_id = 'PATIENT_ID' # the ID of the patient

# The data to be sent to the EMR system
# This should be a dictionary where the keys are the field names in the EMR system and the values are the data for those fields
data = {
    'patientId': 'DATA',
    'patientName': 'DATA',
    'birthday': 'DATA',
    'symptoms': 'DATA'
    # ... more fields as required by your EMR system
}

headers = {'API-Key': api_key}

response = requests.post(f'{api_url}/patients/{patient_id}', headers=headers, json=data)

if response.status_code == 200:
    print('Data successfully sent to EMR system')
else:
    print(f'Failed to send data to EMR system: {response.content}')
