const axios = require('axios')
const querystring = require('querystring')

const user = {
    async getUser (ctx) {
        try {
            const bkToken = ctx.cookies.get('bk_token')
            const params = querystring.stringify({
                bk_app_code: process.env.BKPAAS_APP_ID,
                bk_app_secret: process.env.BKPAAS_APP_SECRET,
                bk_token: bkToken
            })
            const response = await axios({
                withCredentials: true,
                url: `${process.env.BK_COMPONENT_API_URL}/api/c/compapi/v2/bk_login/get_user/?${params}`,
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    Cookie: ctx.cookies.request.headers.cookie || ''
                },
                responseType: 'json'
            })
            if (response.data.code > 0) {
                ctx.status = 401
                ctx.send(response.data)
                return
            } else {
                Object.assign(response.data.data, {
                    username: response.data.data.bk_username
                })
                ctx.send(response.data || {})
            }
        } catch (err) {
            ctx.throwError({
                message: err.message
            })
        }
    }
}

module.exports = user
