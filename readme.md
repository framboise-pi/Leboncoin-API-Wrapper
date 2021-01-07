# Leboncoin API Wrapper [![PyPI](https://img.shields.io/pypi/v/leboncoin-api-wrapper)](https://pypi.org/project/leboncoin-api-wrapper/)

Allow easy access to leboncoin api using python

## Installation
```bash
pip install leboncoin-api-wrapper
```

## Usage
```python
from leboncoin_api_wrapper import Leboncoin

lbc = Leboncoin()
lbc.searchFor("iphone")
lbc.setLimit(10)
lbc.maxPrice(2000)
lbc.setDepartement("tarn")
results = lbc.execute()

for ad in results["ads"]:
    print(ad["subject"], ad["price"])
print("\n")

for ad in results["shippable_ads"]:
    print(ad["subject"])
    print(ad["body"])
    print("\n")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)
