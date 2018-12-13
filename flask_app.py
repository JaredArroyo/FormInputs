from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')

    cap_name = name.upper()
    first_letter_of_name = name[0]
    first_letter_of_cap_name = cap_name[0]
    if(first_letter_of_name != first_letter_of_cap_name):
        return render_template("main_page.html", output="Please re-enter First Name '%s' start with capital letter" % name)
    else:
        dropdown = request.form.get('input_dropdown', '')
        select = request.form.get('input_select', '')
        freeform = request.form.get('input_freeform', '')
        return render_template("main_page.html", input_data=dropdown,
                            output="You're a wizard %s." % name)








