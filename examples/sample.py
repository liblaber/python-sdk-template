from petstore_sdk import PetstoreSdk, Environment

sdk = PetstoreSdk(access_token="YOUR_ACCESS_TOKEN", base_url=Environment.DEFAULT.value)

result = sdk.pets.list_pets(limit=24)

print(result)
