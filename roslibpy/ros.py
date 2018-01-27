#!/usr/bin/env python

import asyncio
import json
import logging
import websockets
import pika

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)


class ROS(object):
    """
    Class to represent a connection to ROSBridge.
    """
    def __init__(self, url: str='', loop=None):
        self._conn = None
        self._socket = None
        self._url = url
        self._loop = loop or asyncio.get_event_loop()

        self._broker = pika.BlockingConnection(
                pika.ConnectionParameters(host='localhost'))
        channel = self._broker.channel()

        channel.exchange_declare(
                exchange='rostopics',
                exchange_type='topic')

    async def __aenter__(self) -> 'ROS':
        self._conn = websockets.connect(self._url)
        self._socket = await self._conn.__aenter__()
        return self

    async def __aexit__(self, *args, **kwargs) -> None:
        self._broker.disconnect()
        await self._conn.__aexit__(*args, **kwargs)

    async def authenticate(self) -> None:
        pass

    async def send(self, msg):
        await self._conn.ws_client.send(msg)

    async def recv(self) -> None:
        channel = self._broker.channel()
        message = await self._conn.ws_client.recv()

        routing_key = json.loads(message)['topic']
        channel.basic_publish(
                exchange='rostopics',
                routing_key=routing_key,
                body=message)
        print('message published')
