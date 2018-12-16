# `googletrans` Error
## 1. AttributeError: 'NoneType' object has no attribute 'group'
```
OS : Ubuntu 16.04
Problem with : python3.5, googletrans
```

When I tried this python3 codes, the error came out with the error :  <br>` AttributeError: 'NoneType' object has no attribute 'group'`
```python3
from googletrans import Translator
translator = Translator()
translator.translate('안녕하세요.').text
```

### How to solve it?
> $ pip3 install git+https://github.com/BoseCorp/py-googletrans.git --upgrade

##### How can I download `googletrans`?
> $ pip3 install googletrans 
