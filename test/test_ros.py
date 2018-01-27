#!/usr/bin/env python

import pytest
import roslibpy as rp
from asynctest import mock


@mock.patch('websockets.connect')
@pytest.mark.asyncio
async def test_connect(ctx):
    url = 'ws://localhost:9090'
    async with rp.ROS(url) as ros:
        assert ros._url == url
        assert ros._conn is not None
        assert ros._socket is not None
        assert ros._loop is not None


@mock.patch('websockets.connect')
@mock.patch('websockets.WebSocketCommonProtocol.send')
@pytest.mark.asyncio
async def test_subscribe(ctx, foo):
    url = 'ws://localhost:9090'
    async with rp.ROS(url) as ros:
        battery_status = rp.Topic(
                ros,
                'topic_name'
                'message_type')

        add_subscriber(
