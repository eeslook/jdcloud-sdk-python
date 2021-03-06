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


class AddDomainRequest(JDCloudRequest):
    """
    添加主域名
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AddDomainRequest, self).__init__(
            '/regions/{regionId}/domainAdd', 'POST', header, version)
        self.parameters = parameters


class AddDomainParameters(object):

    def __init__(self, regionId, packId, domainName, ):
        """
        :param regionId: 实例所属的地域ID
        :param packId: 域名的套餐类型, 0->免费 ,1->企业版, 2->高级版
        :param domainName: 要添加的域名
        """

        self.regionId = regionId
        self.packId = packId
        self.domainName = domainName
        self.domainId = None
        self.buyType = None
        self.timeSpan = None
        self.timeUnit = None
        self.billingType = None

    def setDomainId(self, domainId):
        """
        :param domainId: (Optional) 域名ID，升级高级版必填
        """
        self.domainId = domainId

    def setBuyType(self, buyType):
        """
        :param buyType: (Optional) 1->新购买、3->升级，收费套餐的域名必填
        """
        self.buyType = buyType

    def setTimeSpan(self, timeSpan):
        """
        :param timeSpan: (Optional) 1，2，3 ，时长，收费套餐的域名必填
        """
        self.timeSpan = timeSpan

    def setTimeUnit(self, timeUnit):
        """
        :param timeUnit: (Optional) 时间单位，收费套餐的域名必填
        """
        self.timeUnit = timeUnit

    def setBillingType(self, billingType):
        """
        :param billingType: (Optional) 计费类型，收费套餐的域名必填
        """
        self.billingType = billingType

