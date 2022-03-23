/**
 * @file app store
 * @author
 */

function getInitVariableValue (defaultValue, defaultValueType) {
    let val = defaultValue.all
    if (defaultValueType === 1) val = defaultValue[window.BKPAAS_ENVIRONMENT]
    return val
}

export default {
    namespaced: true,
    state: {
        example: getInitVariableValue({ all: 0, stag: 0, prod: 0 }, 0)
    },
    mutations: {
        setBkProjectVariable (state, { code, val }) {
            state[code] = val
        }
    },
    actions: {
        setBkProjectVariable ({ commit }, variableData) {
            commit('setBkProjectVariable', variableData)
        }
    }
}
