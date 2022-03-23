<template>
    <router-view class="page-container"></router-view>
</template>
<script>
    /**
     * 请先安装 bk-magic-vue 组件库、bkui-vue-complex 复合组件库
     * bk-magic-vue 组件库: https://magicbox.bk.tencent.com/static_api/v3/components_vue/2.0/example/index.html#/install
     * bkui-vue-complex 复合组件库: https://github.com/TencentBlueKing/lesscode-comp
     *
     * 如果页面使用了远程函数，单独使用本页面，需要确保项目 store 下有相应的方法，后端有相应的转发接口
     */

    export default {}
</script>
<style lang="css" scoped>
    .container-mbfjodmj {
        margin: 10px;
    }
    .bk-layout-row-mbfjodmj {
        display: flex;
    }
    .bk-layout-row-mbfjodmj:after {
        display: block;
        clear: both;
        content: '';
        font-size: 0;
        height: 0;
        visibility: hidden;
    }
    .bk-layout-col-mbfjodmj {
        float: left;
        position: relative;
        min-height: 1px;
    }
    .bk-free-layout-mbfjodmj {
        height: 500px;
        width: 100%;
        display: inline-block;
        position: relative;
        z-index: 10;
    }
    .bk-free-layout-item-inner-mbfjodmj {
        height: 100%;
        position: relative;
    }
    .bk-form-radio {
        margin-right: 20px;
    }
    .bk-form-checkbox {
        margin-right: 20px;
    }
    .echarts {
        width: 100%;
        height: 100%;
    }
    /* 设置 bk-exception 组件宽度为 100% */
    .bk-layout-col-mbfjodmj .bk-exception-img {
        width: 100%;
    }
    /* 每个组件之间默认外边距 5px */
    .bk-layout-component-mbfjodmj {
        margin: 5px;
        vertical-align: middle;
    }
    .bk-form-item {
        margin: 10px;
    }
    .bk-sideslider {
        margin: 0;
    }
    /* 设置 .bk-form-control 组件宽度为 auto */
    .bk-form-control {
        width: auto;
    }
    .bk-form-control .bk-input-text {
        font-size: 12px;
    }
    .bk-layout-custom-component-wrapper .page-container {
        margin: 0px;
    }
</style>
