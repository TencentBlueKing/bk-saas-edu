<%! from django.utils.translation import ugettext as _ %>
<%inherit file="/base.mako"/>

<%block name='head'>
	<title>${ _("蓝鲸开发框架")}</title>
	${parent.head()}

</%block>

<%block name="content">
	<div class="home-page">
    	<div class="page-arrow">
			<div class="container">
				<!-- 蓝鲸智云开发框架说明  Start -->
				<div class="tc title-word">
					<p>${ _("欢迎使用蓝鲸智云PaaS平台") }</p>
				</div>
				<div class="tc title-word-second">
					<p>${ _("蓝鲸智云开发框架") }<small class="pl10">${ _("助力你的自动化") }</small></p>
				</div>
				<hr class="cutting-line">
				<div class="tc frame-explain-text">
					<p>${ _("您现在打开的应用是由蓝鲸智云示例代码生成的，该示例代码称为“SaaS开发框架”。") }</p>
					<p>${ _("蓝鲸智云PaaS平台提供了完善的前后台开发框架、调度引擎、公共组件等模块，帮助业务的产品和技术人员快速构建低成本、免运维的支撑工具和运营系统。") }</p>
					<p>${ _("若想体验快速开发应用的功能，请前往") } <a class="developer-center" href="${BK_DEV_URL}" target="_blank">${ _("“开发者中心”") }</a>${ _("。")}</p>
				</div>
				<!-- 蓝鲸智云开发框架说明  End -->
			</div>
		</div>
    </div>
</%block>

