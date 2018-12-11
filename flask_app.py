from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    dropdown = request.form.get('input_dropdown', '')
    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    return render_template("main_page.html", input_data=dropdown,
                           output="You're a wizard %s." % name)


def dedupe(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)

    return y

animals = ['cats','cats','cats','dogs','pandas']
print(dedupe(animals))