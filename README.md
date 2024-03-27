# PetstoreSdk Python SDK 1.0.0

A Python SDK for PetstoreSdk.

- API version: 1.0.0
- SDK version: 1.0.0

## Table of Contents

- [Installation](#installation)
- [Authentication](#authentication)
- [Services](#services)

## Installation

```bash
pip install petstore-pypi
```

## Authentication

### Access Token

The PetstoreSdk API uses a access token as a form of authentication.

The access token can be set when initializing the SDK like this:

```py
PetstoreSdk(
    access_token="YOUR_ACCESS_TOKEN"
)
```

Or at a later stage:

```py
sdk.set_access_token("YOUR_ACCESS_TOKEN")
```

## Services

### PetsService

#### **list_pets**

```py
from petstore_sdk import PetstoreSdk, Environment

sdk = PetstoreSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.pets.list_pets(limit=24)

print(result)
```

#### **create_pets**

```py
from petstore_sdk import PetstoreSdk, Environment
from petstore_sdk.models import Pet

sdk = PetstoreSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = Pet(**{
    "id_": 3,
    "name": "name",
    "tag": "tag"
})

result = sdk.pets.create_pets(request_body=request_body)

print(result)
```

#### **show_pet_by_id**

```py
from petstore_sdk import PetstoreSdk, Environment

sdk = PetstoreSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.pets.show_pet_by_id(pet_id="petId")

print(result)
```
