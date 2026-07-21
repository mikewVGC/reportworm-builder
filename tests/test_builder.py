
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
