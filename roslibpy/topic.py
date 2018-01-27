#!/usr/bin/env python

import asyncio
import json
import logging
import uuid
from typing import Callable

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)


class subscribe(object):
    def __init__(self, ros: 'ROS', topic: 'Topic'):
        self._ros = ros
        self._topic = topic

    async def __aenter__(self) -> 'subscribe':
        self._ros.add_subscriber(self._topic)
        return self

    async def __aexit__(self, *args, **kwargs) -> None:
        self._ros.remove_subscriber(self._topic)


class Topic(object):
    def __init__(
            self,
            ros: 'ROS',
            topic: str,
            message_type: str = '',
            throttle_rate: int = 0,
            queue_length: int = 0):

        if throttle_rate < 0:
            raise ValueError('Throttle rate must be >= 0')

        self._id = str(uuid.uuid1())
        self._ros = ros
        self._queue = asyncio.Queue

        self._subscribe_msg = json.dumps({
            'op': 'subscribe',
            'id': self._id,
            'topic': topic,
            'type': message_type,
            'throttle_rate': throttle_rate,
            'queue_length': queue_length})

        self._unsubscribe_msg = json.dumps({
            'op': 'unsubscribe',
            'id': self._id,
            'topic': topic})

    async def __aenter__(self) -> 'Topic':
        self.subscribe()
        return self

    async def __aexit__(self, *args, **kwargs) -> None:
        self.unsubscribe()

    async def subscribe(self, callback: Callable=None):
        """
        Subscribe to the topic
        """
        LOGGER.info('Subscription added')
        await self._ros.send(self._subscribe_msg)

    async def unsubscribe(self):
        """
        Unsubscribe to the topic
        """
        LOGGER.info('Subscription removed')
        await self._ros.send(self._unsubscribe_msg)
