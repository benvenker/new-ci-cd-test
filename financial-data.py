from plaid import Client

# Instantiate the Plaid client
client = Client(client_id='client_id', secret='secret', public_key='public_key', environment='sandbox')

# Assume we have an access token
access_token = 'access_token'

# Get identity data
response = client.Identity.get(access_token)

# Get the account holder's name, address, etc.
for account in response['accounts']:
    names = account['names']
    addresses = account['addresses']

# Now `names` and `addresses` contain the name and address information for the account holder
