from openai import AzureOpenAI

OPENAI_API_KEY = 'CLW2Qniw6YNf0bHoe9j0kVGiuNE7jxqmOguOsaFA7yftmfqgMIcSJQQJ99BDACHYHv6XJ3w3AAAAACOGEYlZ'
OPENAI_VERSION = '2025-03-01-preview'
AZURE_ENDPOINT = 'https://sli39-m9z5fe1j-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4o-transcribe/audio/transcriptions?api-version=2025-03-01-preview'



client = AzureOpenAI(
    api_key = OPENAI_API_KEY,
    api_version = OPENAI_VERSION,
    azure_endpoint = AZURE_ENDPOINT
)

response = client.chat.completions.create(
    model="gpt-4o-transcribe",  # or your deployment name, e.g., "gpt-35-turbo"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."}
    ]
)

print(response.choices[0].message.content)
