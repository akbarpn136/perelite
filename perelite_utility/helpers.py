import json
import binascii
import os
from django.http import HttpResponse
from mongoengine import (ValidationError,
                         NotUniqueError,
                         DoesNotExist,
                         MultipleObjectsReturned)


def create_exception(prop):
    try:
        prop.save()

        return HttpResponse(prop.to_json())

    except ValidationError as err:
        return HttpResponse(json.dumps(err.to_dict()))

    except NotUniqueError:
        return HttpResponse(json.dumps({
            'detail': 'Tried to save duplicate unique keys'
        }))


def retrieve_exception(query):
    try:
        return query

    except DoesNotExist:
        return HttpResponse(json.dumps({
            'detail': 'Matching query does not exist.'
        }))

    except MultipleObjectsReturned:
        return HttpResponse(json.dumps({
            'detail': 'Multiple object found'
        }))


def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()


def check_instance(get_object, model_class, func=None):
    if isinstance(get_object, model_class):
        if func is None:
            return HttpResponse(json.dumps({'detail': 'Document has been deleted'}))

        elif func == 1:
            return HttpResponse(json.dumps({'detail': 'Document has been saved'}))

        else:
            return HttpResponse(func)

    else:
        return get_object
