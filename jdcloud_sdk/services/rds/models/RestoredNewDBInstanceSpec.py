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


class RestoredNewDBInstanceSpec(object):

    def __init__(self, instanceClass, instanceStorageGB, azId, vpcId, subnetId, chargeSpec, instanceName=None, parameterGroup=None):
        """
        :param instanceName: (Optional) 数据库实例名，名称的限制可参考[帮助中心文档](../../../documentation/Cloud-Database-and-Cache/RDS/Introduction/Restrictions/SQLServer-Restrictions.md)
        :param instanceClass:  实例规格代码，可以通过[describeInstanceClasses](../instance/describeInstanceClasses.md)接口获取
        :param instanceStorageGB:  磁盘大小，单位GB
        :param azId:  可用区ID， 第一个ID必须为主实例所在的可用区。如两个可用区一样，也需输入两个azId
        :param vpcId:  VPC的ID
        :param subnetId:  子网ID
        :param parameterGroup: (Optional) 参数组ID, 缺省系统会创建一个默认参数组<br>- 仅支持MySQL
        :param chargeSpec:  计费规格，包括计费类型，计费周期等
        """

        self.instanceName = instanceName
        self.instanceClass = instanceClass
        self.instanceStorageGB = instanceStorageGB
        self.azId = azId
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.parameterGroup = parameterGroup
        self.chargeSpec = chargeSpec
