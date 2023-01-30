""" importing required modules """
import json

def handler(event, context):
    return {
        'body':'Hello from new lambda using github.',
        'status_code': 200

    }