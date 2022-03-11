<%! from django.utils.translation import ugettext as _ %>
<%inherit file="/base.mako"/>

<%block name='head'>
	<title>${ _("蓝鲸开发框架")}</title>
	${parent.head()}
</%block>

<%block name="content">
<div class="page_index">
	<!-- banner start -->
	<div class="getheadimg-box">
		<p class="guide-banner-title">${ _("开发指引")}</p>
		<p class="guide-banner-word">${ _("了解蓝鲸开发框架，从这里开始")}</p>

	</div>
	<!-- banner end -->
	<div class="container">
	<ul class="king-step3 king-step-primary">
	    <li class="process-doing mt50 clearfix">
	    	<span class="outer-circle"></span>
	        <div class="step-num step-num-top-line">1</div>
	        <div class="step-text step-text-top">
	            <h4>${ _("本地开发环境安装")}</h4>
		        <div class="mt10 mb20 wm lh2">
					<a href="https://docs.bk.tencent.com/blueapps/USAGE.html#2-%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA%EF%BC%88python%EF%BC%89" target="_blank">${ _("安装指南")}</a>
					<br>
					<p class="text-notice">${ _("注意：应用测试、正式部署时会自动安装运行环境，并部署应用")}
					</p>
				</div>
	        </div>
	    </li>
	    <li class="process-doing clearfix">
	    	<span class="outer-circle"></span>
	        <div class="step-num">2</div>
	        <div class="step-text">
	            <h4>${ _("开发项目")}</h4>
	            <div class="mt10 mb20 wm lh2">
					<strong>${ _("1.配置修改")}</strong><br>
					${ _("（1）config/__init__.py 文件：APP_CODE \ SECRET_KEY （对应 蓝鲸智云开发者中心 -&gt; 点击应用ID -&gt; 基本信息 中的应用ID和应用TOKEN）")}<br>
					${ _("（2）config/__init__.py 文件：BK_URL（蓝鲸智云开发者中心的域名，形如：http://paas.bking.com）")}<br>
					${ _("（3）config/dev.py 文件：DATABASES（请创建本地开发数据库，并修改配置信息）")}<br>
					${ _("（4）config/stag.py 文件：DATABASES（请创建测试数据库，并修改配置信息）")}<br>
					${ _("（5）config/prod.py 文件：DATABASES（请创建正式数据库，并修改配置信息）")}<br>
					<p class="text-notice">${ _("注意：测试环境 和 正式环境 的数据库需要对 AppServer 授权")}</p>
					<strong>${ _("2.celery 配置")}</strong><br>
					${ _("若需要使用 celery，请修改以下配置：（")}<a href="https://docs.bk.tencent.com/blueapps/USAGE.html#25-%E5%AE%89%E8%A3%85-celery%EF%BC%88%E9%9C%80%E8%A6%81%E4%BD%BF%E7%94%A8%E5%90%8E%E5%8F%B0%E4%BB%BB%E5%8A%A1%E7%9A%84%E9%A1%B9%E7%9B%AE%EF%BC%89" target="_blank">${ _("celery 开发指引")}</a>）<br>
					${ _("（1）config/default.py 文件：IS_USE_CELERY 的值设置为: ")}<span class="text-notice">True</span><br>
					${ _("（2）config/dev.py 文件：BROKER_URL（请创建本地开发的 celery消息队列，并修改配置信息，推荐使用 redis）")}<br>
					${ _("（3）config/default.py 文件：CELERY_IMPORTS（添加celery任务模块）")}<br>
                    <p class="text-notice"></p>
					<strong>${ _("3.数据库操作")}</strong><br>
					${ _("Django Migration的使用方法如下:")}<br>
					${ _("（1）执行 manage.py migrate（Django默认表创建）。")}<br>
					${ _('（2）执行 manage.py startapp yourappname、添加yourappname到config/default.py文件的"INSTALLED_APPS"变量中。')}<br>
					${ _("（3）在Application的models.py中建立数据库模型，执行manage.py makemigrations yourappname。")}<br>
					${ _("（4）执行manage.py migrate yourappname。")}<br>
				</div>
	        </div>
	    </li>
	    <li class="process-doing clearfix">
	    <span class="outer-circle"></span>
	        <div class="step-num">3</div>
	        <div class="step-text-button-line">
	            <h4>${ _("部署项目")}</h4>
	            <div class="mt10 mb20 wm lh2">
					<strong>${ _("通过蓝鲸智云开发者中心提供的“测试部署”、“正式部署”服务将应用部署到测试\正式环境中。")}</strong><br>
					${ _("操作入口：蓝鲸智云开发者中心 -&gt; 点击应用名称 -&gt; 应用部署。 ")}<br>
					${ _("（1）测试部署：将应用代码在测试环境上进行部署，部署成功后就可以在测试环境中使用您的应用。")}<br>
					${ _("（2）正式部署：将应用代码在正式环境上进行部署，部署成功后就可以在正式环境中使用您的应用。")}<br>
					${ _("（3）下架操作：系统将应用代码从您选择的环境上撤销部署，届时用户将无法访问该应用，但是该应用的数据库依然保留。")}<br>
				</div>
	        </div>
	    </li>
	</ul>
	</div>
</div>
</%block>
<%block name='footerline'>
    <hr class="guide-cutting-line">
</%block>
