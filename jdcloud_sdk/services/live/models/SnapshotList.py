# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class SnapshotList(object):

    def __init__(self, publishDomain=None, appName=None, streamName=None, snapshotTime=None, height=None, width=None, ossBucket=None, ossEndpoint=None, ossObject=None):
        """
        :param publishDomain: (Optional) 推流域名
        :param appName: (Optional) 流所属应用名称
        :param streamName: (Optional) 直播流名称
        :param snapshotTime: (Optional) 截图时间
        :param height: (Optional) 图片高
        :param width: (Optional) 图片宽
        :param ossBucket: (Optional) OSSBucket的名称
        :param ossEndpoint: (Optional) OSSEndpoint域名
        :param ossObject: (Optional) OSSObject
        """

        self.publishDomain = publishDomain
        self.appName = appName
        self.streamName = streamName
        self.snapshotTime = snapshotTime
        self.height = height
        self.width = width
        self.ossBucket = ossBucket
        self.ossEndpoint = ossEndpoint
        self.ossObject = ossObject
