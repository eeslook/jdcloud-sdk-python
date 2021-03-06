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


class AddCustomLiveStreamWatermarkTemplateRequest(JDCloudRequest):
    """
    添加直播水印模板
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AddCustomLiveStreamWatermarkTemplateRequest, self).__init__(
            '/watermarkCustoms:template', 'POST', header, version)
        self.parameters = parameters


class AddCustomLiveStreamWatermarkTemplateParameters(object):

    def __init__(self, offsetX, offsetY, width, height, template, url):
        """
        :param offsetX: x轴偏移量 单位：像素
        :param offsetY: y轴偏移量 单位：像素
        :param width: 宽
        :param height: 高
        :param template: 录制模板自定义名称
        :param url: 高
        """

        self.offsetX = offsetX
        self.offsetY = offsetY
        self.width = width
        self.height = height
        self.template = template
        self.url = url

