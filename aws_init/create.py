import boto3
def create(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        TableName='Music',
        KeySchema=[
            {
                'AttributeName': 'Artist',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'Title',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'artist',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table

if __name__ == '__main__':
    tab = create()
    print("Table status:", tab.table_status)
