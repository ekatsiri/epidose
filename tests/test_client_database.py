__copyright__ = """
    Copyright 2020 Diomidis Spinellis

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
__license__ = "Apache 2.0"

from datetime import datetime, timedelta, timezone
import pytest

from dp3t.protocols.client_database import ClientDatabase


############################
### TEST CLIENT DATABASE ###
############################


def test_database_initialization():
    d = ClientDatabase(':memory:')
    print(d.last_ephid_change())
    assert d.last_ephid_change() == datetime(1970, 1, 1, 0, 0)
