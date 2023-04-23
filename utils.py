import json


def parse_form_data(req, name):
    return json.loads(req.form[name])


def parse_form_elem(req, name):
    return json.loads(req.args.get(name))
