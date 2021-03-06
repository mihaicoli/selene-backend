# Mycroft Server - Backend
# Copyright (C) 2020 Mycroft AI Inc
# SPDX-License-Identifier: 	AGPL-3.0-or-later
#
# This file is part of the Mycroft Server.
#
# The Mycroft Server is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Entry point for the API that supports the Mycroft Marketplace."""
from flask import Flask

from selene.api import get_base_config, selene_api, SeleneResponse
from selene.util.log import configure_logger
from .endpoints import AudioFileEndpoint, DesignationEndpoint, TagEndpoint

_log = configure_logger("precise_api")


# Define the Flask application
precise = Flask(__name__)
precise.config.from_object(get_base_config())
precise.response_class = SeleneResponse
precise.register_blueprint(selene_api)

audio_file_endpoint = AudioFileEndpoint.as_view("audio_file_endpoint")
precise.add_url_rule(
    "/api/audio/<string:file_name>", view_func=audio_file_endpoint, methods=["GET"]
)

designation_endpoint = DesignationEndpoint.as_view("designation_endpoint")
precise.add_url_rule(
    "/api/designation", view_func=designation_endpoint, methods=["GET"]
)

tag_endpoint = TagEndpoint.as_view("tag_endpoint")
precise.add_url_rule("/api/tag", view_func=tag_endpoint, methods=["GET", "POST"])
