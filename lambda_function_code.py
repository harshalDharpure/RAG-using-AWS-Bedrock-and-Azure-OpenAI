import os
import boto3

boto3_session = boto3.session.Session()
bedrock_agent_runtime_client = boto3.client('bedrock_agent_runtime_client')

kb_id = os.environ.get("KNOWLEDGE_BASE_ID")

def retrieve(input, kb_id):
    response = bedrock_agent_runtime_client.retrieve(
        knowledgeBaseId=kb_id,
        retrieveQuery={
            'text': input_text
        },
        retrievalConfiguration={
            'vectorSearchConfiguration': {
                'numberOfResults':1
            }
        }
        )
        return response
        
def lambda_handler(event, context):
    if 'question' not in event:
        return {
            'statusCode': 400,
            'body': 'No Question Provided'
        }
    
    query = event['question']
    response = retrieve(query, kb_id)
    return {
            'statusCode': 200,
            'body': {
                'question': question.strip(),
                'answer': response
            }
        }
