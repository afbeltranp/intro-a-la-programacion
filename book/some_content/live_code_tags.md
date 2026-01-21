---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.3
kernelspec:
  display_name: base
  language: python
  name: python3
---

# Hello world

```{code-cell} ipython3
print("Hello world!")
```

```{code-cell} ipython3
:tags: ["disable-execution-cell"]

import datetime

# This prints the current date and time once
current_time = datetime.datetime.now()
print("This notebook was last updated at:", current_time)
```
