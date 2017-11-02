import json
import binascii
import os
from django.http import HttpResponse
from mongoengine import (ValidationError,
                         NotUniqueError)
from rest_framework import status


def create_exception(prop):
    try:
        prop.save()

        return HttpResponse(prop.to_json())

    except ValidationError as err:
        return HttpResponse(json.dumps(err.to_dict()), status=status.HTTP_400_BAD_REQUEST)

    except NotUniqueError:
        return HttpResponse(json.dumps({
            'detail': 'Tried to save duplicate unique keys'
        }), status=status.HTTP_400_BAD_REQUEST)


def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()


def check_instance(get_object, model_class, func=''):
    if isinstance(get_object, model_class):
        if func is None:
            return HttpResponse(json.dumps({'detail': 'Document has been deleted'}))

        elif func == 1:
            return HttpResponse(json.dumps({'detail': 'Document has been saved'}))

        else:
            if func:
                return HttpResponse(func)
            else:
                return HttpResponse(get_object.to_json())

    else:
        return HttpResponse(get_object)
