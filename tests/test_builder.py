
import unittest
from unittest.mock import patch, mock_open

import json

from reportworm_builder.builder import Builder

"""
there's a lot more of this class that can be covered... it's not
really written in a way that's condusive to test coverage ... kinda
over-engineered, sorry
"""

class TestBuilder(unittest.TestCase):

    build_data = {
        "builder": {
            "steps": [
                "test_step",
            ],
            "refs": {
                "tpl": "tests/templates"
            },
            "common": [
                {
                    "type": "html",
                    "tokens": [
                        {
                            "token": "__TOKEN_FLAG_TEST__",
                            "type": "flag",
                            "name": "mode",
                            "values": [
                                { "value": "prod", "type": "tpl", "ref": "flag-prod" },
                                { "values": [ "dev", "local" ], "type": "tpl", "ref": "flag-dev" }
                            ]
                        },
                        {
                            "token": "__SITES_NAV_TEST__",
                            "type": "sites_nav",
                            "nav_type": "menu"
                        },
                    ],
                },
            ],
            "test_step": {
                "type": "html",
                "base-ref": "home",
                "out": "public/index.html",
            }
        },
    }

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(build_data))
    def test_init_creates_steps(self, mock_file):

        builder = Builder({}, {})

        self.assertEqual(len(builder.steps), 1)


    """
    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(build_data))
    def test_builder_builds(self, mock_file):

        builder = Builder({}, {})

        compiled = builder.steps[0].compile()

        print(compiled)
    """
