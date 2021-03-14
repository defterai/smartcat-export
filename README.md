# SmartCAT Export
Export SmartCAT multi-language document to file

## Usage

```
name: Export Document
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: defterai/smartcat-export@master
      name: Export SmartCat document
      with:
        account_id: ${{ secrets.SMARTCAT_ACCOUNT_ID }}
        auth_key: ${{ secrets.SMARTCAT_API_KEY }}
        document_id: b2274ec73fedfdb987bb3170
        language_id: 1058
        filename: file.xlsx
```

## Arguments
| Argument | Description | Required |
|---|---|---|
| account_id | SmartCAT account identifier | + |
| auth_key | SmartCAT auth API key | + |
| document_id | Export document identifier | + |
| language_id | Export document language identifier | + |
| filename | Export document file name | + |
