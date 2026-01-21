# Some content

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

```{figure} ../figures/logo.png
---
width: 80%
align: center
name: fig-example
---
Logo.
```

```{video} https://www.youtube.com/watch/B1J6Ou4q8vE
```

$$ F_{res} = m \cdot a $$ 

$$ E = m \cdot c^2 $$

```{math}
v = a \cdot t
```

The displacement can be found using the equation $s = v \cdot t$.

# Tables

| Column 1 | Column 2 | Column 3 |
|---|---|---|
| Data 1  | Data 2  | Data 3  |
| Data 4  | Data 5  | Data 6  |


```{table} Table caption
:widths: auto
:align: center

| Header 1      | Header 2      | Header 3      |
|---------------|---------------|---------------|
| Row 1, Col 1  | Row 1, Col 2  | Row 1, Col 3  |
| Row 2, Col 1  | Row 2, Col 2  | Row 2, Col 3  |
```


```{list-table} Sample Data Table
:header-rows: 1
* - Category
  - Value 1
  - Value 2
* - Item A
  - 10
  - 20
* - Item B
  - 15
  - 30
```


# Cross Reference

[Go text and code](text_and_code.ipynb)
[Go to Exercise 7](../exercises/007.md)

$$ F = m \cdot a$$ (eq:Newton)

Refer to Equation {eq}`eq:Newton`

```{table} Example Table
:name: tab-example
| Column 1 | Column 2 |
|----------|----------|
| A        | B        |
```


{numref}`My table {number} <tab-example>`

{numref}`Figure {number} <fig-example>`


Here is the [link to the template](https://teachbooks.github.io/template/).




