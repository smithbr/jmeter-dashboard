from jmd import app


@app.add_template_filter
def category_or(string, default):
    if not string in ['success', 'info', 'warning', 'danger']:
        return default
    else:
        return string
