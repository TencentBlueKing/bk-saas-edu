<%! from django.utils.translation import ugettext as _ %>
<%inherit file="/base.mako"/>

<%block name='head'>
	<title>${ _("蓝鲸开发框架")}</title>
	${parent.head()}

</%block>

<%block name="content">
    <style type="text/css">
        #footer{
            position: relative;
            bottom: -40px;
        }
    </style>
    <div class="page-contactus">
        <!-- 内容 start-->
        <!--comtactus-detail -->
        <div class="container" >
            <div class="tc" id="contactus">
                <div class="weixin-img-arrow">
                    <div>
                        <img class="weixin-img " src="${STATIC_URL}open/img/weixin_icom.png">
                    </div>
                    <p>${ _("关注我们")}</p>
                </div>
                <div class="comtactus-way-arrow tc mt50">
                    <div class="dbi border-right tc" style="width: 280px; padding-left: 60px">
                        <div class="img-arrow">
                            <img  class="" src="${STATIC_URL}open/img/icom_01.png">
                        </div>
                        <p class="mt20">${ _("深圳市南山区腾讯大厦")}</p>
                    </div>
                    <div class="dbi border-right tc" style="width: 180px">
                        <div class="img-arrow">
                            <img src="${STATIC_URL}open/img/icom_02.png">
                        </div>
                        <p class="mt20">${ _("企业QQ：800802001")}</p>
                    </div>
                    <div class="dbi tc" style="width: 280px">
                        <div class="img-arrow">
                            <img src="${STATIC_URL}open/img/icom_03.png">
                        </div>
                        <p class="mt20">${ _("邮箱：contactus_bk@tencent.com")}</p>
                    </div>
                </div>
            </div>

        </div>
        <!-- 内容 start-->
    </div>
</%block>
