# <div><img src="https://adviceslip.com/app/img/touch-icon-iphone.png" width="40" /> advice_slip.py

> Web-API for [Advice Slip](https://adviceslip.com) a REST API that serves random pieces of advice, searchable by keyword or retrievable by ID.

</div>

## Quick Start

```python
from advice_slip import AdviceSlip

advice = AdviceSlip()

# Get a random piece of advice
print(advice.get_random_advice())

# Get advice by ID
print(advice.get_advice_by_id(42))

# Search for advice
print(advice.search_advice("money"))
```

---

<div align="center">

## Advice

| Method | Description |
|--------|-------------|
| `get_random_advice()` | Get a random advice slip |
| `get_advice_by_id(slip_id)` | Get a specific advice slip by ID |
| `search_advice(query)` | Search advice slips by keyword |

</div>
