# Copyright (c) DEV Corporation. All rights reserved.
# Licensed under MIT License.

from flask import Blueprint


api_bp = Blueprint('api', __name__)


from . import routes
