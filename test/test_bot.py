import unittest
from unittest.mock import AsyncMock
from textwrap import dedent
from bot import start_command, replying_text

class TestBot(unittest.IsolatedAsyncioTestCase):

    async def test_start_command_send_welcome_message(self):
        mock_message = AsyncMock()
        expected_text = dedent(f'''
        Bem-vindo ao Bot de Teste'''
        )
        await start_command(client= None, message= mock_message)

        mock_message.reply_text.assert_called_once_with(expected_text)

    async def test_replying_text_send_same_text_reply(self):
        mock_message = AsyncMock()
        expected_text = f'You say:\n __{mock_message.text}__'

        await replying_text(client= None, message= mock_message)

        mock_message.reply_text.assert_called_once_with(expected_text)