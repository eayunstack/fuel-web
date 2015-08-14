# -*- coding: utf-8 -*-

#    Copyright 2015 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import pytest

from fuel_package_updates import utils


@pytest.mark.parametrize('release_version,expected', [
    ('111111-7.0', '7.0'),
    ('2014.4-7.0.1', '7.0.1'),
    ('2015.2.2-6.1', '6.1'),
])
def test_extract_version(release_version, expected):
    assert utils.extract_fuel_version(release_version) == expected