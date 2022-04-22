<template>
    <section class="bk-layout-custom-component-wrapper container-gpbomhfl">
        <div class="bk-layout-row-gpbomhfl grid-58ec0c04">
            <div class="bk-layout-col-gpbomhfl" style="width: 100%">
                <bk-button
                    title=""
                    size="normal"
                    theme="primary"
                    :disabled="false"
                    :loading="isCreateLoading"
                    ext-cls=""
                    class="bk-layout-component-gpbomhfl button9c2a1239"
                    @click="handleCreateDeploy">新增部署
                </bk-button>
                <bk-button
                    title="hello world"
                    size="normal"
                    theme="default"
                    :loading="isRefreshing"
                    ext-cls=""
                    class="bk-layout-component-gpbomhfl button84557975"
                    @click="handleRefresh">刷新
                </bk-button>
                <bk-table
                    :stripe="false"
                    :border="false"
                    :outer-border="false"
                    :row-border="true"
                    :col-border="false"
                    size="medium"
                    :fit="true"
                    :show-header="true"
                    :highlight-current-row="false"
                    :show-pagination-info="true"
                    height=""
                    max-height=""
                    class="bk-layout-component-gpbomhfl"
                    v-bind:data="taskList"
                    v-bind:pagination="tablePagination">
                    <bk-table-column label="ID" prop="id" :sortable="false"></bk-table-column>
                    <bk-table-column label="任务名称" prop="task_name" :sortable="false"></bk-table-column>
                    <bk-table-column label="任务ID" prop="task_id" :sortable="false"></bk-table-column>
                    <bk-table-column label="业务ID" prop="bk_biz_id" :sortable="false"></bk-table-column>
                    <bk-table-column label="模板ID" prop="template_id" :sortable="false"></bk-table-column>
                    <bk-table-column label="状态" prop="status" :sortable="false"></bk-table-column>
                    <bk-table-column label="创建人" prop="created_by" :sortable="false"></bk-table-column>
                    <bk-table-column label="创建时间" prop="created_at" :formatter="timeFormatter" :sortable="false"></bk-table-column>
                    <bk-table-column label="操作" width="100">
                        <template slot-scope="props">
                            <bk-button
                                title="primary"
                                :text="true"
                                @click="handleClickShowTask(props.row)"
                            >
                                查看任务
                            </bk-button>
                        </template>
                    </bk-table-column>
                </bk-table>
            </div>
        </div>

        <bk-sideslider
            :is-show.sync="isShowTaskDetail"
            title="任务详情"
            :width="600"
            class="bk-layout-component-gpbomhfl">
            <template slot="content">
                <bk-form
                    :label-width="150"
                    :model="deployDetail"
                    v-bkloading="{ isLoading: isTaskDetailLoading }">
                    <bk-form-item
                        v-for="(field, index) in [...deployDetail.fields, ...deployDetail.dynamicFields]"
                        :key="index"
                        :label="field.name"
                    >
                        {{ field.value }}
                    </bk-form-item>
                    <bk-form-item>
                        <bk-link theme="primary" :href="deployDetail.task_url" target="_blank">查看详情</bk-link>
                    </bk-form-item>
                </bk-form>
            </template>
        </bk-sideslider>
        <bk-dialog
            v-model="isShowDialog"
            :transfer="false"
            title="新增部署"
            theme="primary"
            :mask-close="false"
            :close-icon="true"
            :fullscreen="false"
            :draggable="false"
            :scrollable="false"
            :width="600"
            :show-mask="true"
            ok-text="确定"
            cancel-text="取消"
            :auto-close="true"
            header-position="left"
            class="bk-layout-component-gpbomhfl"
            @confirm="handleSubmitCreate">
            <template slot="default">
                <bk-form :label-width="100" :model="newFormData" :rules="rules" ref="validateForm">
                    <bk-form-item label="任务名称" :required="true" :property="'task_name'">
                        <bk-input v-model="newFormData.task_name" placeholder="请输入3到10个以内的字符" style="width: 100%;"></bk-input>
                    </bk-form-item>
                    <bk-form-item label="业务选择" :required="true" :property="'bk_biz_id'">
                        <bk-select
                            v-model="newFormData.bk_biz_id"
                            searchable
                            :loading="isBizListLoading"
                            @toggle="handleToggleBizList"
                            @selected="handleSelectBiz">
                            <bk-option v-for="option in bizList"
                                :key="option.bk_biz_id"
                                :id="option.bk_biz_id"
                                :name="option.bk_biz_name">
                            </bk-option>
                        </bk-select>
                    </bk-form-item>
                    <bk-form-item label="模板选择" :required="true" :property="'template_id'">
                        <bk-select
                            v-model="newFormData.template_id"
                            searchable
                            :loading="isTempListLoading"
                            @selected="handleSelectTemp">
                            <bk-option v-for="option in templateList"
                                :key="option.template_id"
                                :id="option.template_id"
                                :name="option.template_name">
                            </bk-option>
                        </bk-select>
                    </bk-form-item>
                    <bk-form-item
                        v-for="renderParam in renderParams"
                        :key="renderParam.key"
                        :label="renderParam.name"
                        :property="`params.${renderParam.key}`">
                        <bk-input v-model="newFormData.params[renderParam.key]" style="width: 100%;"></bk-input>
                    </bk-form-item>
                </bk-form>
            </template>
        </bk-dialog>
    </section>
</template>
<script>
    import dayjs from 'dayjs'

    export default {
        data () {
            function getInitVariableValue (defaultValue, defaultValueType) {
                let val = defaultValue.all
                if (defaultValueType === 1) val = defaultValue[window.BKPAAS_ENVIRONMENT]
                return val
            }
            return {
                taskList: getInitVariableValue({ all: [], prod: [], stag: [] }, 0),
                tablePagination: getInitVariableValue(
                    {
                        all: { current: 1, count: 0, limit: 10, limitList: [10, 20, 50, 100], showLimit: false },
                        prod: {},
                        stag: {}
                    },
                    0
                ),
                apiPerfix: getInitVariableValue(
                    { all: API_URL, prod: '', stag: '' },
                    0
                ),
                isShowTaskDetail: false,
                isShowDialog: false,
                newFormData: {
                    task_name: '',
                    bk_biz_id: '',
                    template_id: '',
                    params: {}
                },
                renderParams: [],
                bizList: [],
                templateList: [],
                rules: {
                    task_name: [
                        {
                            required: true,
                            message: '必填项',
                            trigger: 'blur'
                        },
                        {
                            min: 3,
                            message (val) {
                                return `${val}不能小于3个字符`
                            },
                            trigger: 'blur'
                        },
                        {
                            max: 10,
                            message: '不能多于10个字符',
                            trigger: 'blur'
                        }
                    ],
                    bk_biz_id: [
                        {
                            required: true,
                            message: '必填项',
                            trigger: 'blur'
                        }
                    ],
                    template_id: [
                        {
                            required: true,
                            message: '必填项',
                            trigger: 'blur'
                        }
                    ]
                },
                isBizListLoading: false,
                isTempListLoading: false,
                isTaskDetailLoading: false,
                deployDetail: {
                    fields: [
                        {
                            name: 'ID',
                            key: 'id',
                            value: ''
                        }, {
                            name: '任务ID',
                            key: 'task_id',
                            value: ''
                        }, {
                            name: '业务ID',
                            key: 'bk_biz_id',
                            value: ''
                        }, {
                            name: '模板ID',
                            key: 'template_id',
                            value: ''
                        }, {
                            name: '任务名称',
                            key: 'task_name',
                            value: ''
                        }, {
                            name: '状态',
                            key: 'status',
                            value: ''
                        }, {
                            name: '创建者',
                            key: 'created_by',
                            value: ''
                        }
                    ],
                    dynamicFields: [],
                    task_url: ''
                },
                isRefreshing: false,
                isCreateLoading: false
            }
        },

        mounted () {
            this.getRecordList()
        },
        
        methods: {
            getRecordList () {
                const params = {
                    page: this.tablePagination.current,
                    size: this.tablePagination.limit
                }
                this.$http.get(`${this.apiPerfix}api/v1/tasks/`, { params }).then((res) => {
                    const data = res.data || {}
                    this.taskList = data.info || []
                    this.tablePagination.count = data.count || 0
                })
            },

            handleCreateDeploy () {
                this.isCreateLoading = true
                this.$http.get(`${this.apiPerfix}api/v1/permissions/?action_id=task_create`).then((res) => {
                    if (res?.data?.is_allowed) {
                        this.isShowDialog = true
                    } else {
                        return this.$http.get(`${this.apiPerfix}api/v1/permissions/get_apply_url/?action_id=task_create`).then((res) => {
                            this.$bkInfo({
                                title: '暂无权限',
                                subTitle: '可以点击申请权限！',
                                theme: 'danger',
                                okText: '去申请权限',
                                confirmFn () {
                                    window.open(res?.data?.apply_url, '_blank')
                                }
                            })
                        })
                    }
                }).catch((err) => {
                    this.messageError(err.message || err)
                }).finally(() => {
                    this.isCreateLoading = false
                })
            },

            handleToggleBizList (isOpen) {
                if (isOpen) {
                    this.isBizListLoading = true
                    this.$http.get(`${this.apiPerfix}api/v1/bizs/`).then((res) => {
                        this.bizList = res.data || []
                    }).catch((err) => {
                        this.messageError(err.message || err)
                    }).finally(() => {
                        this.isBizListLoading = false
                    })
                }
            },

            handleSelectBiz (id) {
                this.isTempListLoading = false
                this.$http.get(`${this.apiPerfix}api/v1/templates/?bk_biz_id=${id}`).then((res) => {
                    this.templateList = res.data || []
                    // 清空选中的模板
                    this.newFormData.template_id = ''
                    // 清空动态表单
                    this.renderParams = []
                }).catch((err) => {
                    this.messageError(err.message || err)
                }).finally(() => {
                    this.isTempListLoading = false
                })
            },

            handleSelectTemp (id) {
                this.$http.get(`${this.apiPerfix}api/v1/templates/${id}/params/?bk_biz_id=${this.newFormData.bk_biz_id}`).then((res) => {
                    const params = res.data || []
                    this.renderParams = Object.values(params).map((param) => ({
                        key: param.key?.slice(2, -1),
                        name: param.name
                    }))
                }).catch((err) => {
                    this.messageError(err.message || err)
                })
            },

            handleSubmitCreate () {
                this.$refs.validateForm.validate().then(() => {
                    this.$http.post(`${this.apiPerfix}api/v1/tasks/`, this.newFormData).then(() => {
                        this.getRecordList()
                        this.messageSuccess('新增成功')
                    }).catch((err) => {
                        this.messageError(err.message || err)
                    })
                }, validator => {
                    this.messageError(validator.content)
                })
            },

            handleClickShowTask (row) {
                if (row.permission.task_view) {
                    this.handleShowTask(row)
                } else {
                    this.showPermissionDialog(row)
                }
            },

            handleShowTask (row) {
                this.isShowTaskDetail = true
                this.isTaskDetailLoading = true
                this.$http.get(`${this.apiPerfix}api/v1/tasks/${row.id}/`).then((res) => {
                    const data = res.data || {}
                    this.deployDetail.fields.forEach((field) => {
                        field.value = data[field.key]
                    })
                    this.deployDetail.dynamicFields = Object.keys(data.params).map((name) => ({ name, value: data.params[name] })) || []
                    this.deployDetail.task_url = data.task_url
                }).catch((err) => {
                    this.messageError(err.message || err)
                }).finally(() => {
                    this.isTaskDetailLoading = false
                })
            },

            showPermissionDialog (row) {
                this.$http.get(`${this.apiPerfix}api/v1/permissions/get_apply_url/?action_id=task_view&resource_type=task&resource_id=${row.id}`).then((res) => {
                    this.$bkInfo({
                        title: '暂无权限',
                        subTitle: '可以点击申请权限！',
                        theme: 'danger',
                        okText: '去申请权限',
                        confirmFn () {
                            window.open(res?.data?.apply_url, '_blank')
                        }
                    })
                }).catch((err) => {
                    this.messageError(err.message || err)
                })
            },

            handleRefresh () {
                this.isRefreshing = true
                this.$http.get(`${this.apiPerfix}api/v1/tasks/sync/`).then(() => {
                    this.getRecordList()
                }).catch((err) => {
                    this.messageError(err.message || err)
                }).finally(() => {
                    this.isRefreshing = false
                })
            },

            timeFormatter (obj, con, val) {
                return val ? dayjs(val).format('YYYY-MM-DD HH:mm:ss') : '--'
            }
        }
    }
</script>
<style lang="css" scoped>
    .container-gpbomhfl {
        margin: 10px;
    }
    .bk-layout-row-gpbomhfl {
        display: flex;
    }
    .bk-layout-row-gpbomhfl:after {
        display: block;
        clear: both;
        content: '';
        font-size: 0;
        height: 0;
        visibility: hidden;
    }
    .bk-layout-col-gpbomhfl {
        float: left;
        position: relative;
        min-height: 1px;
    }
    .bk-free-layout-gpbomhfl {
        height: 500px;
        width: 100%;
        display: inline-block;
        position: relative;
        z-index: 10;
    }
    .bk-free-layout-item-inner-gpbomhfl {
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
    .bk-layout-col-gpbomhfl .bk-exception-img {
        width: 100%;
    }
    /* 每个组件之间默认外边距 5px */
    .bk-layout-component-gpbomhfl {
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

    .button9c2a1239 {
        display: inline-block;
    }
    .button84557975 {
        display: inline-block;
    }
</style>
