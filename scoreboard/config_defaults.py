# Copyright 2016 David Tomaschik <david@systemoverlord.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os


class Defaults(object):
        ATTACHMENT_BACKEND = 'file://attachments'
        COUNT_QUERIES = False
        CSP_POLICY = None
        CWD = os.path.dirname(os.path.realpath(__file__))
        DEBUG = False
        EXTEND_CSP_POLICY = None
        ERROR_404_HELP = False
        FIRST_BLOOD = 0
        GAME_TIME = (None, None)
        LOGIN_METHOD = 'local'
        MAIL_FROM = 'ctf@scoreboard'
        MAIL_FROM_NAME = None
        MAIL_HOST = 'localhost'
        NEWS_POLL_INTERVAL = 60000
        RULES = '/rules'
        SCORING = 'plain'
        SYSTEM_NAME = 'root'
        TEAMS = False
        TEASE_HIDDEN = True
        TITLE = 'Scoreboard'
