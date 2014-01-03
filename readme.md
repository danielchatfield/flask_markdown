# Flask Markdown extension

A simple extension for adding a `{% markdown %}{% endmarkdown %}` tag to Jinja templates.

## Usage

```python
from flask.ext.markdown import markdown

app = Flask()

markdown(app)

```


## Features

### Automatic indentation detection

This works:

```
<article class="article container-very-tight pad-medium highlight-first">
    {% markdown %}
        Terms of Service
        ================

        In short, we run this website called Volcanic Pixels and you are more
        than welcome to use it and the products distributed through it. All we
        ask is that you don't use it for things which are illegal or harmful.

        ***

        ...
    {% endmarkdown %}
</article>
```

## Want a new feature? Bug report?

Open an issue on github, or better submit a pull request.