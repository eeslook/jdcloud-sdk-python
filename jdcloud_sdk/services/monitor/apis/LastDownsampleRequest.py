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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class LastDownsampleRequest(JDCloudRequest):
    """
    查看某资源的最后一个点
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(LastDownsampleRequest, self).__init__(
            '/regions/{regionId}/metrics/{metric}/lastDownsample', 'GET', header, version)
        self.parameters = parameters


class LastDownsampleParameters(object):

    def __init__(self, regionId, metric, serviceCode, resourceId, ):
        """
        :param regionId: 地域 Id
        :param metric: 监控项英文标识(id)
        :param serviceCode: 资源的类型，取值vm, lb, ip, database 等
        :param resourceId: 资源的uuid
        """

        self.regionId = regionId
        self.metric = metric
        self.serviceCode = serviceCode
        self.resourceId = resourceId
        self.tags = None
        self.startTime = None
        self.endTime = None
        self.timeInterval = None
        self.aggrType = None

    def setTags(self, tags):
        """
        :param tags: (Optional) 自定义标签
        """
        self.tags = tags

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 查询时间范围的开始时间， UTC时间，格式：yyyy-MM-dd'T'HH:mm:ssZ（默认为当前时间，早于30d时，将被重置为30d）
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 查询时间范围的结束时间， UTC时间，格式：2016-12- yyyy-MM-dd'T'HH:mm:ssZ（为空时，将由startTime与timeInterval计算得出）
        """
        self.endTime = endTime

    def setTimeInterval(self, timeInterval):
        """
        :param timeInterval: (Optional) 查询的时间间隔，仅支持分钟级别，例如：1m
        """
        self.timeInterval = timeInterval

    def setAggrType(self, aggrType):
        """
        :param aggrType: (Optional) 聚合方式：max avg min等
        """
        self.aggrType = aggrType
